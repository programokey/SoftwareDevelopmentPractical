import sys
sys.path.append("..")

from gevent import monkey
monkey.patch_all()
from gevent import pywsgi

from flask import Flask, jsonify, request, make_response, send_file, redirect
from flask_cors import CORS
import Backend.validate as validate
import DataLayer.DBQuery as DBQuery
import DataLayer.TestQuery as TestQuery
from threading import Thread
import json

app = Flask(__name__, root_path='../frontEnd/dist/')
CORS(app, supports_credentials=True)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return send_file('index.html')


@app.route('/api/department', methods=['GET', 'POST'])
def get_departments():
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_departments()
    else:
        return json.dumps({'code': 403, 'data': ''})

@app.route('/api/department/<departmentName>', methods=['GET', 'POST'])
def get_department_info(departmentName):
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_department_info(departmentName)
    else:
        return json.dumps({'code': 403, 'data': ''})


@app.route('/api/department/<departmentName>/roles/<roleName>', methods=['GET', 'POST'])
def get_department_role_job(departmentName, roleName):
    '''
    :param departmentName:
    :param roleName:
    :return: the jobs the role should do in the department
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_department_role_job(departmentName, roleName)
    else:
        return json.dumps({'code': 403, 'data': ''})


@app.route('/api/role/<roleName>', methods=['GET', 'POST'])
def get_role_job(roleName):
    '''
    :param roleName:
    :return: the jobs the role should do
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_role_job(roleName)
    else:
        return json.dumps({'code': 403, 'data': ''})


'''the parameter roleName is Unused'''
@app.route('/api/role/<roleName>/<jobName>', methods=['GET', 'POST'])
def get_job_detail(roleName, jobName):
    '''
    :param roleName:
    :param jobName
    :return: the details of the jobs that staffs in this role may care about
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_job_detail(jobName)
    else:
        return json.dumps({'code': 403, 'data': ''})

@app.route('/api/flow/<int:flowId>', methods=['GET', 'POST'])
def get_flow(flowId):
    '''
    :param flowId
    :return: the details of the flow
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_flow(flowId)
    else:
        return json.dumps({'code': 403, 'data': ''})

@app.route('/api/medicine/<approveNumber>', methods=['GET', 'POST'])
def get_medicine(approveNumber):
    '''
    :param approveNumber
    :return: the details of the medicine
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_medicine(approveNumber)
    else:
        return json.dumps({'code': 403, 'data': ''})

@app.route('/api/diseases-categories', methods=['GET', 'POST'])
def get_disease_categories():
    '''
    :return: all disease categories
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_disease_categories()
    else:
        return json.dumps({'code': 403, 'data': ''})

@app.route('/api/case/disease/<diseaseName>', methods=['GET', 'POST'])
def get_cases(diseaseName):
    '''
    :param diseaseName
    :return: all the cases of the disease
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_cases(diseaseName)
    else:
        return json.dumps({'code': 403, 'data': ''})

@app.route('/api/examinationResult/<int:id>', methods=['GET', 'POST'])
def get_examination_result(id):
    '''
    :param id
    :return: the detail of the examination result
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_examination_result(id)
    else:
        return json.dumps({'code': 403, 'data': ''})

@app.route('/api/operation/<operationName>', methods=['GET', 'POST'])
def get_operation(operationName):
    '''
    :param operationName
    :return: the detail of the operation
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_operation(operationName)
    else:
        return json.dumps({'code': 403, 'data': ''})


@app.route('/api/case/<int:caseId>', methods=['GET', 'POST'])
def get_case_detail(caseId):
    '''
    :param caseId
    :return: the detail of the case
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_case_detail(caseId)
    else:
        return json.dumps({'code': 403, 'data': ''})

@app.route('/api/prescription/<int:id>', methods=['GET', 'POST'])
def get_prescription(id):
    '''
    :param id: prescription's id
    :return: the detail of the prescription
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_prescription(id)
    else:
        return json.dumps({'code': 403, 'data': ''})

@app.route('/api/equipment/<int:equipmentId>', methods=['GET', 'POST'])
def get_equipment(equipmentId):
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        res = DBQuery.get_equipment(equipmentId)
        return res
    else:
        return json.dumps({'code': 403, 'data': ''})

@app.route('/api/test/id/<int:id>', methods=['GET', 'POST'])
def get_test(id):
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        user = validate.get_user_id(token)
        if user is not None:
            res = TestQuery.get_test(id, user)
            return res
    return json.dumps({'code': 403, 'data': ''})

@app.route('/api/test', methods=['GET', 'POST'])
def get_all_test():
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        userID = validate.get_user_id(token)
        if userID is not None:
            res = TestQuery.get_all_test(userID)
            return res
    return json.dumps({'code': 403, 'data': ''})
    # return redirect('/login')

@app.route('/api/test/submit', methods=['GET', 'POST'])
def submit():
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        testID = request.form['testId']
        answer = request.form['answer']
        userID = validate.get_user_id(token)
        if userID is not None:
            res = TestQuery.submit(testID, userID, answer)
            return res
    return redirect('/login')

@app.route('/static/<path1>/<path2>')
def static_file(path1, path2):
    return send_file('static/%s/%s' % (path1, path2))

@app.route('/media_file/<path1>/<path2>')
def media_file(path1, path2):
    return send_file('../../media/%s/%s' % (path1, path2))

@app.route('/api/login', methods=['POST'])
def login():
    if request.method == 'POST':
        userID = request.form['name']
        hash = request.form['hash']
        info, token = validate.login(userID, hash)
        response = make_response(info)
        if token is not None:
            response.set_cookie('token', token)
        return response
    else:
        return "Internal Error"


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


if __name__ == '__main__':
    score_calculation = Thread(target=TestQuery.score_calculate)
    score_calculation.start()
    # app.run(host='0.0.0.0')

    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()

'''
$env:FLASK_APP="main.py"
python -m flask run


gevent
'''
