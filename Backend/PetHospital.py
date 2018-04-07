import sys

sys.path.append("..")

from flask import Flask, jsonify, request, make_response, abort, send_file, redirect
from flask_cors import CORS
import Backend.validate as validate
import DataLayer.DBQuery as DBQuery

app = Flask(__name__, root_path='../frontEnd/dist/')
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return send_file('index.html')


@app.route('/department', methods=['GET', 'POST'])
def get_departments():
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_departments()
    else:
        return redirect('/login')


@app.route('/department/<departmentName>', methods=['GET', 'POST'])
def get_department_info(departmentName):
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_department_info(departmentName)
    else:
        return redirect('/login')


@app.route('/department/<departmentName>/roles/<roleName>', methods=['GET', 'POST'])
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
        return redirect('/login')


@app.route('/roles/<roleName>', methods=['GET', 'POST'])
def get_role_job(roleName):
    '''
    :param roleName:
    :return: the jobs the role should do
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_role_job(roleName)
    else:
        return redirect('/login')


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
        return redirect('/login')


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
        return redirect('/login')


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
        return redirect('/login')

@app.route('/api/case>', methods=['GET', 'POST'])
def get_disease_categories():
    '''
    :return: all disease categories
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_disease_categories()
    else:
        return redirect('/login')


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
        return redirect('/login')

@app.route('/api/examinationResult/<id>', methods=['GET', 'POST'])
def get_examination_result(id):
    '''
    :param caseId
    :return: the detail of the case
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_examination_result(id)
    else:
        return redirect('/login')

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
        return redirect('/login')

@app.route('/api/prescription/<id>', methods=['GET', 'POST'])
def get_prescription(id):
    '''
    :param id: prescription's id
    :return: the detail of the prescription
    '''
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        return DBQuery.get_prescription(id)
    else:
        return redirect('/login')

@app.route('/api/equipment/<equipmentId>', methods=['GET', 'POST'])
def get_equipment(equipmentId):
    token = request.cookies.get('token')
    if token is not None and validate.validate(token):
        res = DBQuery.get_equipment(equipmentId)
        if res is not None:
            return res
    else:
        return "Internal Error"


@app.route('/static/<path1>/<path2>')
def static_file(path1, path2):
    return send_file('static/%s/%s' % (path1, path2))


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        hash = request.form['hash']
        info, token = validate.login(user, hash)
        response = make_response(info)
        response.set_cookie('token', token)
        print('token', token)
        return response
    else:
        return "Internal Error"


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
