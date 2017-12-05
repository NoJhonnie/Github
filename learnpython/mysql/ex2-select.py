#encoding=utf-8
import MySQLdb

try:
    conn = MySQLdb.connect(host='192.168.1.107', port=3306, db='db_name',
         user='root', passwd='root', charset='utf8')
    cur = conn.cursor()
    cur.execute('select * from students where sid=1')
    result = cur.fetchone()
    print result
    cur.close()
    conn.close()
except Exception,e:
    print e.message
    
try:
    conn = MySQLdb.connect(host='192.168.1.107', port=3306, db='db_name',
         user='root', passwd='root', charset='utf8')
    cur = conn.cursor()
    cur.execute('select * from students')
    result = cur.fetchall()
    print result
    cur.close()
    conn.close()
except Exception,e:
    print e.message