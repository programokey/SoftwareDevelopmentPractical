from hashlib import sha1
import DataLayer.DBQuery as DBQuery
import redis
import json, random

redis_conn = redis.Redis()
LOGIN_EXPIRE_TIME = 60*60

def login(userID, hash):
    token = ''
    if userID is None or hash is None:
        return json.dumps({'code': 403, 'data': {'result': False}}), None
    else:
        if redis_conn.exists('user_%s'%userID):
            res = redis_conn.get('user_%s' % userID)
            user_info = json.loads(res)
        else:
            user_info = DBQuery.get_user(userID)
            if user_info is None:
                return json.dumps({'code': 403, 'data': {'result': False}}), None
            redis_conn.set('user_%s' % userID, json.dumps(user_info))

        validate_hash = sha1((user_info['id'] + '_' + user_info['passwd']).encode('utf8')).hexdigest()

        if validate_hash == hash:
            token = sha1(
                (str(random.getrandbits(64)) + user_info['name'] + '_' + user_info['passwd']).encode('utf8')
            ).hexdigest()

            redis_conn.set('token_%s'%token, value=userID, ex=LOGIN_EXPIRE_TIME) # expired after LOGIN_EXPIRE_TIME seconds  without any request
            if redis_conn.exists('user_token_%s' % userID):
                old_token = redis_conn.get('user_token_%s' % userID).decode('utf8')
                redis_conn.delete('token_%s'%old_token)
            redis_conn.set('user_token_%s' % userID, value=token, ex=LOGIN_EXPIRE_TIME)  # expired after 30 min without any request

            return json.dumps({'code': 1000, 'data': {'result': True, 'token': token}}), token
        else:
            return json.dumps({'code': 403, 'data': {'result': False}}), None

def validate(token):
    if redis_conn.exists('token_%s'%token):
        redis_conn.expire('token_%s'%token, LOGIN_EXPIRE_TIME)
        userID = redis_conn.get('token_%s'%token).decode('utf8')
        redis_conn.expire('user_token_%s' % userID, LOGIN_EXPIRE_TIME)
        return True
    return False

def get_user_id(token):
    if redis_conn.exists('token_%s' % token):
        return redis_conn.get('token_%s' % token).decode('utf8')
    return None

