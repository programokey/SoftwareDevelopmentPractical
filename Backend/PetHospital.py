from flask import Flask, jsonify, request, abort
import json
from hashlib import sha1
import configparser
import redis
cf = configparser.ConfigParser()
cf.read('pethospital.conf')
mysql_user = cf.get('mysqldb', 'user')
mysql_passwd = cf.get('mysqldb', 'passwd')
mysql_host = cf.get('mysqldb', 'host')



app = Flask(__name__)
@app.route("/")
def  index():
    return 'Index Page'

@app.route('/login', methods=['POST'])
def login():
    login_data = request.get_json()
    user = login_data['name']
    hash_vale = login_data['hash']

    return 'Hello, World'
#
#
# @app.route('/bilibili')
# def bilibili():
#     return url_for('static', filename='bilibili.html')
#
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
#
# @app.route('/post=<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

'''
$env:FLASK_APP="main.py"
python -m flask run
'''

if __name__ == '__main__':
    # res = sha1('zhanghao_mima'.encode()).hexdigest()
    # print(res)
    # redis_coon = redis.Connection(host='localhost')
    r = redis.Redis()
    r.set(name='2333', value='2333', ex=20)
    # redis_coon.
    print(mysql_host, mysql_user, mysql_passwd)