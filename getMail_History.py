#!/usr/bin/python
#_*_coding:utf-8 _*_
#Auth:Qing.Yu
#Mail:1753330141@qq.com
# Ver:V1.1
#Date:2018-08-27
#检查用户邮件记录，增加数据库写入
#create table t_MailLog(域名 nvarchar(50),月份邮件 nvarchar(20),类型 nvarchar(50),标题 nvarchar(150),收件人 nvarchar(100),发件人 nvarchar(100),时间 datetime)

from  cls_qqMail import obj_qqMail
import json,time,cls_mssql

s_key={1:'发信',2:'收信'}

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt

#写入数据库
def db_wr(row):
    sql = cls_mssql.db_mssql()
    sql.sql_str = "insert into t_MailLog values('%s','%s','%s','%s','%s','%s','%s')"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6]) 
    sql.db_exec()

m = obj_qqMail()
#定义邮箱域名（获取登录密码等），查询时间，当月月末日期
co = m.setMailBox['och']
ym = '2018-08'
lastday = '31'
(m.corpid, m.corpsecret, m.deptRoot)=(co['corpid'], co['corpsecret_logQuery'], co['deptRoot'])
#定义用户访问时间
m.queryLoginId=""
m.begin_date = '%s-01'%(ym)
m.end_date = '%s-%s'%(ym,lastday)
#打印结果
strs = json.loads(m.getMailRecord())
for str in strs['list']:
    print('邮件类型# %s 标题# %s 发件人# %s 收件人# %s 时间# %s '%(s_key[str['mailtype']], str['subject'],str['sender'],str['receiver'],timestamp_datetime(str['time'])))
    db_wr([co['domain'],ym,s_key[str['mailtype']],str['subject'].replace("'","''"),str['sender'],str['receiver'],timestamp_datetime(str['time'])])
