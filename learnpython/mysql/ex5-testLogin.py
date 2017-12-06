#encoding=utf-8
from MysqlHelper import MysqlHelper
from hashlib import sha1
print '-------------------------------------'
print '----------welcome--------------------'

outflag = True  #标记外循环

#进入外循环
while outflag:
    print '[1] login in      [2]create account'
    choose = raw_input(">")
    #判断选择登陆还是注册
    if choose == '1' or choose == 'login in':
        
        isflag = True   #标记内循环
        
        #进入内循环
        while isflag:
            sname = raw_input("please input your account:")
            spwd = raw_input("please input your password:")
            
            #密码加密，使之与数据库内部密码对应
            s1 = sha1()
            s1.update(spwd)
            spwdSha1 = s1.hexdigest()
            #查询密码
            sql = "select upwd from userinfos where uname=%s"
            params = [sname]
            sqlHelper = MysqlHelper('192.168.1.107',3306,'db_name','root','root')
            upwd = sqlHelper.get_one(sql,params)
            #比对密码，对应无账号、密码正确、密码错误和错误
            if upwd == None:
                print 'no account!'
                isflag = False
                outflag = True
            elif upwd[0] == spwdSha1:
                print 'login in success!!!'
                isflag = False
                outflag = False
            elif upwd[0] != spwdSha1:
                print 'Password Error!'
                isflag = True
            else:
                print 'error!'
                isflag = True
                
    #选则注册
    elif choose == '2' or choose == 'create account':
        #标记内循环
        isflag = True
        #进入内循环
        while isflag:
            sname = raw_input("please input your account:")
          
            sql = "select * from userinfos where uname=%s"
            params = [sname]
            sqlHelper = MysqlHelper('192.168.1.107',3306,'db_name','root','root')
            userinfo = sqlHelper.get_one(sql,params)
            #查询账号是否存在    
            if userinfo == None:
                spwd = raw_input("please input your password:")
                #密码加密
                s1 = sha1()
                s1.update(spwd)
                spwdSha1 = s1.hexdigest()
                #写入数据库
                sql = "insert into userinfos(uname,upwd) values(%s,%s)"
                params = [sname,spwdSha1]
                sqlHelper = MysqlHelper('192.168.1.107',3306,'db_name','root','root')
                count = sqlHelper.insert(sql,params)
                if count == 1:
                    print 'create success!'
                    isflag = False
                    outflag = False
                else:
                    print 'error'
                    isflag = False
            #账号存在
            else:
                print 'there is a same user!Please input other username!'
                isflag = True
    #输入其他东西
    else:
        print 'please input number!'
        outflag = True