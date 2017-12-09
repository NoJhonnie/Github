import redis

try:
    r=redis.StrictRedis(host='192.168.1.107', port=6379)
    print 'success!'
except Exception,e:
    print e.message
    
r.set('name','hello')
name = r.get('name')
print 'test'


pipe = r.pipeline()
pipe.set('name','world')
pipe.get('name')
pipe.execute()