import requests as r,json

class obj_qqMail():
    #配置corpid和corpsecret信息
    def __init__(self):
        self.corpid = "TBD"
        self.corpsecret = "TBD"
        self.deptRoot = "TBD"
        self.modUserAccount = 'TBD'
        self.modUserName = 'TBD'
        self.modUserDept = 'TBD'
        self.modUserStatus = 1
        self.fetch_child = 1
        self.dropUserAccount = 'TBD'
        self.setMailBox={
            'och':{
                'corpid':'wm45b65xxxxxxxxxxx',
                'corpsecret':'x7M95AyqAS6nZBxxxxxxxxxxtAgrbcWg0dR0',
                'deptRoot':'55492xxxxx35'},
            }

    #获取token信息
    def getToken(self):
        self.getToken_url = "https://api.exmail.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s"%(self.corpid,self.corpsecret)
        self.token = json.loads(r.get(self.getToken_url).content)['access_token']
        return self.token

    #获取部门列表
    def getDeptList(self):
        self.getToken()
        arr_depts = []
        getDept_url = " https://api.exmail.qq.com/cgi-bin/department/list?access_token=%s"%(self.token)
        deptlist = json.loads(r.get(getDept_url).content)['department']
        for i in range(len(deptlist)):
            arr_depts.append(deptlist[i])
            #print(("部门ID：%s 部门名称：%s")%(arr_info[i]['id'],arr_info[i]['name']))
        return arr_depts

    #获取用户列表（摘要信息）
    def getUserList(self):
        self.getToken()
        arr_users = []
        getUser_url = "https://api.exmail.qq.com/cgi-bin/user/simplelist?access_token=%s&department_id=%s&fetch_child=%d"%(self.token,self.deptRoot,self.fetch_child)
        userlist = json.loads(r.get(getUser_url).content)['userlist']
        for i in range(len(userlist)):
            arr_users.append(userlist[i])
            #print("邮箱地址：%s 邮箱姓名：%s "%(userlist[i]['userid'],userlist[i]['name']))
        return arr_users

    #获取用户列表（详细信息）
    def getUserListDetail(self):
        self.getToken()
        arr_users = []
        getUser_url = "https://api.exmail.qq.com/cgi-bin/user/list?access_token=%s&department_id=%s&fetch_child=1"%(self.token,self.deptRoot)
        userlist = json.loads(r.get(getUser_url).content)['userlist']
        for i in range(len(userlist)):
            arr_users.append(userlist[i])
            #print("邮箱地址：%s 邮箱姓名：%s "%(userlist[i]['userid'],userlist[i]['name']))
        return arr_users

    #用户创建
    def setUserCreate(self):
        self.getToken()
        url="https://api.exmail.qq.com/cgi-bin/user/create?access_token=%s"%(self.token)
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            'userid': self.modUserAccount,
            'name': self.modUserName, 
            'department': [self.modUserDept],
            'password': '1734Abcd'
            }
        #print(payload)
        response=r.post(url,data=json.dumps(payload),headers=headers)
        return response.content

    #用户操作（启用/禁用）
    def setUserStatus(self):
        self.getToken()
        url="https://api.exmail.qq.com/cgi-bin/user/update?access_token=%s"%(self.token)
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload={'userid':self.modUserAccount,"enable":self.modUserStatus}
        #print(payload)
        response=r.post(url,data=json.dumps(payload),headers=headers)
        return response.content

    #用户操作（删除）
    def setUserDrop(self):
        self.getToken()
        url="https://api.exmail.qq.com/cgi-bin/user/delete?access_token=%s&userid=%s"%(self.token,self.dropUserAccount)
        response=r.get(url)
        return response.content

    #用户未读邮件数
    def getUnread(self):
        self.getToken()
        url="https://api.exmail.qq.com/cgi-bin/mail/newcount?access_token=%s&userid=%s"%(self.token,self.modUserAccount)
        response=r.get(url)
        return response.content

        
