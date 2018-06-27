#!/usr/bin/python
#_*_coding:utf-8 _*_
#Auth:Qing.Yu
#Mail:1753330141@qq.com
# Ver:V1.0
#Date:2018-06-27

from cls_qqMail import obj_qqMail
import requests as r,json

m = obj_qqMail()
co = m.setMailBox['och']
(m.domain,m.corpid, m.corpsecret)=(co['domain'],co['corpid'], co['corpsecret_logQuery'])

def getSummary(m,year,month):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    url='https://api.exmail.qq.com/cgi-bin/log/mailstatus?access_token=%s'%(m.getToken())
    payload = {
        'domain': m.domain,
        'begin_date': '%s-%02d-01'%(year,month), 
        'end_date': '%s-%02d-31'%(year,month),
        }
    response=r.post(url,data=json.dumps(payload),headers=headers)
    return response.content

year='2018'
for j in range(6):
    print(getSummary(m,year,j))

