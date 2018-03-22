from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def  index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/bilibili')
def bilibili():
    return url_for('static', filename='bilibili.html')


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post=<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

'''
$env:FLASK_APP="main.py"
python -m flask run
'''