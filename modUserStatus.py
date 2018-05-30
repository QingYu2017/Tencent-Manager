#!/usr/bin/python
#_*_coding:utf-8 _*_
#Auth:Qing.Yu
#Mail:1753330141@qq.com
# Ver:V1.0
#Date:2018-05-17

from  cls_qqMail import obj_qqMail

m = obj_qqMail()
co = m.setMailBox['och']
(m.corpid, m.corpsecret, m.deptRoot)=(co['corpid'], co['corpsecret'], co['deptRoot'])

users=['jtxxjsb@och.cn']
for i in range(len(users)):
    m.modUserAccount=users[i]
    m.modUserStatus=1
    print(m.setUserStatus())
