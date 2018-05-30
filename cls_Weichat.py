#!/usr/bin/python
#_*_coding:utf-8 _*_
#Auth:Qing.Yu
#Mail:1753330141@qq.com
# Ver:V1.0
#Date:2018-05-19

import requests as r,json

class obj_weiChat():
    def __init__(self):
        (self.corpid, self.corpsecret) = ('wxfeb9xxxxxxxxxx', 'N1yeQ-zh9fxxxxxxxxxx4avZ')
        ochLogo = 'https://p.qpic.cn/pic_wework/3119477880/a9afeba5102d88261xxxxxxxxxx/0?tp=webp'
        ccbLogo = 'http://mmbiz.qpic.cn/mmocbiz/uZYcwC4m9wmjn02vN1kKPFT3HFv9xxxxxxxxxxx/640'
        (self.touser, self.title,self.description, self.picurl) = ('Qing.Yu', '信息提示', 'test description', ochLogo)

    def getToken(self):
        url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s'%(self.corpid,self.corpsecret)
        return json.loads(r.get(url).content)['access_token']

    def getDeptList(self):
        self.arr_depts = []
        url='https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=%s'%(self.getToken())
        arr=json.loads(r.get(url).content)['department']
        for i in range(len(arr)):
            self.arr_depts.append(arr[i])
        return self.arr_depts

    def getUserList(self):
        self.arr_users = []
        self.department=1
        url='https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token=%s&department_id=%s&fetch_child=1'%(self.getToken(),self.department)
        arr=json.loads(r.get(url).content)['userlist']
        for i in range(len(arr)):
            self.arr_users.append(arr[i])
        return self.arr_users

    def getAppList(self):
        self.arr_apps = []
        url='https://qyapi.weixin.qq.com/cgi-bin/agent/list?access_token=%s'%(self.getToken())
        arr=json.loads(r.get(url).content)['agentlist']
        for i in range(len(arr)):
            self.arr_apps.append(arr[i])
        return self.arr_apps

    def sendMsg(self):
        url='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s'%(self.getToken())
        payload={
                "touser": self.touser,
                "toparty": "2",
                "agentid": 1,
                "msgtype": "news","news": {"articles":[{"title": self.title, "description": self.description, "picurl": self.picurl}]}
                }
        print(r.post(url,data=json.dumps(payload)).content)   
