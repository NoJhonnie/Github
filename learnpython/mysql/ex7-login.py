#encoding = utf-8
import RedisHelper
import MysqlHelper
import hashlib

name = raw_input("please input your account:")
pwd = raw_input("please input your password:")

sha1 = hashlib.sha1()
sha1.update(pwd)
pwd1 = sha1.hexdigest()

try:
    
    redis = RedisHelper()
    
    if redis.get('uname') == name:
        print 'ok'
    else:
        mysql = MysqlHelper('192.168.1.107',3306,'db_name','root','root')
        upwd = mysql.get_one('select upwd from userinfos where uname=%s',[name])
        if upwd == None:
            print 'account error'
        elif upwd[0]==pwd1:
            redis.set('uname', name)
            print 'login success'
        else:
            print 'password error'
except Exception,e:
    print e.message