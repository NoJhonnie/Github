#encoding=utf-8
from MysqlHelper import *

sql = 'insert into students(sid,sname) values(%s,%s)'
name = raw_input("please input name:")
id = raw_input("please input id:")
params = [int(id),name]

mysqlHelper = MysqlHelper('192.168.1.107',3306,'db_name', 'root', 'root')

count = mysqlHelper.insert(sql,params)
if count == 1:
    print 'ok'
else:
    print 'error'
   
    
sql = 'select * from students order by sid desc'

all = mysqlHelper.get_all(sql)
print all