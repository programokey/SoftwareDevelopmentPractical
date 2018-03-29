from flask import Flask, jsonify, request, abort, send_file
from flask_cors import CORS
import Backend.validate as validate

app = Flask(__name__, root_path='../frontEnd/dist/')
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return send_file('index.html')

@app.route('/api/department', methods=['GET', 'POST'])
def get_departments():
    pass

@app.route('/static/<path1>/<path2>')
def static_file(path1, path2):
    return send_file('static/%s/%s'%(path1, path2))

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        hash = request.form['hash']
        return validate.login(user, hash)
    else:
        return "Internal Error"


# @app.route('/login', methods=['POST', 'GET'])
# # @app.route('/login')
# def login():
#     token = ''
#     login_result = {'code':'403', 'data':{'result':False, 'token':token}}
#     return sha1('Hello, World'.encode()).hexdigest()


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post=<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == '__main__':
    app.run(host='0.0.0.0')


'''
$env:FLASK_APP="main.py"
python -m flask run
'''