#-*-coding:utf-8 -*-
import MySQLdb
try:
    conn = MySQLdb.connect(host='192.168.1.107', port=3306,
            db='db_name', user='root', passwd='root', charset='utf8')
    cncs = conn.cursor()
    count = cncs.execute("insert into students(sid, sname) values(3,'Gogh')")
    print count
    conn.commit()
    cncs.close()
    conn.close()
except Exception,e:
    print e.message
    
try:
    conn = MySQLdb.connect(host='192.168.1.107', port=3306,
            db='db_name', user='root', passwd='root', charset='utf8')
    cncs = conn.cursor()
    count = cncs.execute("update students set sname='Cloud' where sid=1")
    print count
    conn.commit()
    cncs.close()
    conn.close()
except Exception,e:
    print e.message
    
try:
    conn = MySQLdb.connect(host='192.168.1.107', port=3306,
            db='db_name', user='root', passwd='root', charset='utf8')
    cncs = conn.cursor()
    count = cncs.execute("delete from students where sid=3")
    print count
    conn.commit()
    cncs.close()
    conn.close()
except Exception,e:
    print e.message
    
    
try:
    conn = MySQLdb.connect(host='192.168.1.107', port=3306,
            db='db_name', user='root', passwd='root', charset='utf8')
    cncs = conn.cursor()
    sname=raw_input("please input student's name:")
    params = [3,sname]
    count = cncs.execute('insert into students(sid,sname) values(%s,%s)', params)
    print count
    conn.commit()
    cncs.close()
    conn.close()
except Exception,e:
    print e.message
