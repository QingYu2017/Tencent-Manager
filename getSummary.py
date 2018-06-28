#!/usr/bin/python
#_*_coding:utf-8 _*_
#Auth:Qing.Yu
#Mail:1753330141@qq.com
# Ver:V1.1
#Date:2018-06-28

from cls_qqMail import obj_qqMail
import requests as r,json

def getSummary(m,year,month):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    url='https://api.exmail.qq.com/cgi-bin/log/mailstatus?access_token=%s'%(m.getToken())
    payload = {
        'domain': m.domain,
        'begin_date': '%s-%s-1'%(year,month), 
        'end_date': '%s-%s-31'%(year,month),
        }
    response=r.post(url,data=json.dumps(payload),headers=headers)
    return response.content

year='2018'
m = obj_qqMail()
#print(m.setMailBox)
for x in m.setMailBox:
    co = m.setMailBox[x]
    (m.domain,m.corpid, m.corpsecret)=(co['domain'],co['corpid'], co['corpsecret_logQuery'])
    print(m.domain)
    for j in range(4,7):
        s=getSummary(m,year,j)
        print('查询月份：%s-%02d'%(year,j))
        print(s)
        #print('查询月份：%s-%02d 发件数量：%s 收件数量：%s'%(year,j,s('sendsum'),s('recvsum')))
