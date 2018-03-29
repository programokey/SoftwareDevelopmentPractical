from hashlib import sha1
import DataLayer.DBQuery as DBQuery
import redis
import json, random

redis_conn = redis.Redis()

def login(user, hash):
    token = ''
    if user is None or hash is None:
        return json.dumps({'code': '403', 'data': {'result': False}})
    else:
        if redis_conn.exists('user_%s'%user):
            try:
                res = redis_conn.get('user_%s'%user)
                user_info = json.loads(res)
            except:
                user_info = DBQuery.get_user(user)
                if user_info is None:
                    return json.dumps({'code': '403', 'data': {'result': False}})
                redis_conn.set('user_%s' % user, json.dumps(user_info))
        else:
            user_info = DBQuery.get_user(user)
            if user_info is None:
                return json.dumps({'code': '403', 'data': {'result': False}})
            redis_conn.set('user_%s' % user, json.dumps(user_info))

        validate_hash = sha1((user_info['name'] + '_' + user_info['passwd']).encode('utf8')).hexdigest()

        if validate_hash == hash:
            token = sha1(
                (str(random.getrandbits(64)) + user_info['name'] + '_' + user_info['passwd']).encode('utf8')
            ).hexdigest()
            redis_conn.set('token_%s'%token, value=token, ex=60*30) # expired after 30 min without any request
            return json.dumps({'code': '1000', 'data': {'result': True, 'token': token}})
        else:
            return json.dumps({'code': '403', 'data': {'result': False}})

def validate(token):
    if redis_conn.exists(token):
        return token == redis_conn.get(token)
    return False

if __name__ == '__main__':
    pass

