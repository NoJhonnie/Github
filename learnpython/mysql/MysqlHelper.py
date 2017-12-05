#encoding=utf-8
import MySQLdb

class MysqlHelper(object):
    #定义该类的属性
    def __init__(self, host, port, db, user, passwd, charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset
    #定义连接方法    
    def connect(self):
        self.conn = MySQLdb.connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
        self.cursor = self.conn.cursor()
    #定义关闭方法
    def close(self):
        self.cursor.close()
        self.conn.close()
    #定义增删改的初始方法    
    def _edit(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql,params)
            self.conn.commit()
            self.close()
        except Exception,e:
            print e.message
        return count
    #定义增加方法
    def insert(self, sql, params=()):
        return self._edit(sql,params)
    #定义修改方法
    def update(self, sql, params=()):
        return self._edit(sql,params)
    #定义增肌方法
    def delete(self, sql, params=()):
        return self._edit(sql,params)
    
    #定义查询一行数据方法    
    def get_one(self, sql, params=()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception,e:
            print e.message
        return result
    #定义查询多行数据方法    
    def get_all(self, sql, params=()):
        list = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            list = self.cursor.fetchall()
            self.close()
        except Exception,e:
            print e.message
        return list