# _*_coding:utf8_*_
import configparser
import json
import pymysql, redis
import time
from datetime import datetime, timedelta

cf = configparser.ConfigParser()
cf.read('pethospital.conf')
mysql_user = cf.get('mysqldb', 'user')
mysql_passwd = cf.get('mysqldb', 'passwd')
mysql_host = cf.get('mysqldb', 'host')
redis_conn = redis.Redis()
def get_all_test(userID):
    assert  isinstance(userID, str)
    try:
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('select id, name, description, startTime, endTime, duration, creator, score'
                        ' from Test inner join TestParticipation on Test.id = TestParticipation.testID'
                        ' where userID = %s', (userID,))
            res = cur.fetchall()
            all_test = {
                'code': 0,
                'data': []
            }
            for item in res:
                id = item[0]
                cur.execute('select beginTime from TestParticipation where userID = %s and testID = %s', (userID, id))
                begin_time = cur.fetchone()
                if begin_time is not None:
                    begin_time = begin_time[0]
                if begin_time is None:
                    begin_time = datetime.now()

                all_test['data'].append({
                    'id': item[0],
                    'name': item[1],
                    'description': item[2],
                    'startTime': item[3].strftime('%Y-%m-%d %H:%M:%S'),
                    'endTime': item[4].strftime('%Y-%m-%d %H:%M:%S'),
                    'duration': int(item[5].total_seconds()),
                    'score': item[6],
                    'state': '未开始' if datetime.now() < item[3] else
                    '进行中' if datetime.now() < item[4] and begin_time + item[5] > datetime.now() else '已结束'
                })
            return json.dumps(all_test)
    except:
        pass

def get_test_problem(id):
    assert isinstance(id, int)
    try:
        test_problem = {}
        if False and redis_conn.exists('test_problem_%d' % id):
            test_problem = json.loads(redis_conn.get('test_problem_%d' % id).decode('utf8'))
        else:
            with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                                 charset='utf8') as cur:
                cur.execute('select ProblemID, problem, multipleAnswer, point '
                            'from TestProblem inner join Problem on TestProblem.problemID = Problem.id '
                            'where TestProblem.testID = %s', (id))
                res = cur.fetchall()
                if len(res) == 0:
                    return None
                single = []
                multiple = []
                for item in res:
                    cur.execute('select id, choice from Choice where problemID = %s', (item[0],))
                    choice = {item[0]: item[1] for item in cur.fetchall()}
                    if item[2]:
                        multiple.append({
                            'problemId': item[0],
                            'problem': item[1],
                            'choice': choice,
                            'ponit': item[3]
                        })
                    else:
                        single.append({
                            'problemId': item[0],
                            'problem': item[1],
                            'choice': choice,
                            'ponit': item[3]
                        })
                    test_problem['single'] = single
                    test_problem['multiple'] = multiple
                    redis_conn.set('test_problem_%d' % id, value=json.dumps(test_problem))
            return test_problem
    except:
        return None

def get_test(id, userID):
    assert isinstance(id, int)
    assert isinstance(userID, str)

    test_problem = get_test_problem(id)
    try:
        if test_problem is None:
            return json.dumps({
                'code': 404,
                'data': 'No such test'
            })

        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('select startTime, endTime, duration from Test where id = %s', (id, ))
            res = cur.fetchone()
            start_time = res[0]
            end_time = res[1]
            duration = res[2]
            cur.execute('select beginTime from TestParticipation where userID = %s and testID = %s', (userID, id))
            res = cur.fetchone()
            if res is None:
                return json.dumps({
                    'code': 404,
                    'data': '你没有权限参加此考试'
                })
            elif res[0] is None:
                cur.execute('update TestParticipation set  beginTime = %s where userID = %s and testID = %s',
                            (datetime.now(), userID, id))
                begin_time = datetime.now()
            else:
                begin_time = res[0]

        if datetime.now() < start_time or datetime.now() > end_time or begin_time + duration < datetime.now():
            return json.dumps({
                'code': 404,
                'data': '不在考试时间内'
            })
        remaining_time = begin_time + duration - datetime.now()
        remaining_time = int(remaining_time.total_seconds())
        cur.execute('select problemID, choiceID from Answer where userID = %s and testID = %s', (userID, id))
        res = cur.fetchall()
        selected = {}
        for item in res:
            if item[0] not  in selected:
                selected[item[0]] = []
            selected[item[0]].append(item[1])
        test = {
            'code': 1000
        }
        data = test_problem
        data['remainingTime'] = remaining_time
        data['selected'] = selected
        test['data'] = data
        test = json.dumps(test)
        return test
    except:
        return json.dumps({
            "code": 404,
            "data": "Error during getting test %d of user %d" % (id, userID)
        })

def submit(testID, userID, answer):
    assert isinstance(answer, str)
    try:
        testID = int(testID)
        answer = json.loads(answer)
    except:
        return json.dumps({
            'code': 404,
            'data': 'invalid format!'
        })
    try:
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('delete from Answer where userID = %s and testID = %s', (userID, testID))
            for item in answer.items():
                problem_id = item[0]
                choices = item[1]
                for choice_id in choices:
                    cur.execute('insert into Answer value(%s, %s, %s, %s)', (userID, testID, problem_id, choice_id))
        return json.dumps({
            'code': 1000,
            'data': 'submit answer succeeded!'
        })
    except:
        return json.dumps({
         'code':400,
        'data': 'submit answer failed'
        })

def score_calculate():
    while True:
        try:
            with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                                 charset='utf8') as cur:
                cur.execute('select userID, testID from TestParticipation '
                            'where score is NULL and testID in (select id from Test where endTime <= %s); ',
                            (datetime.now(),))
                res = cur.fetchall()
                for item in res:
                    user_id = item[0]
                    test_id = item[1]
                    score = 0
                    cur.execute('select problemID, choiceID from Answer where userID = %s and testID = %s',
                                (user_id, test_id))
                    res = cur.fetchall()
                    selected = {}
                    for item in res:
                        if item[0] not in selected:
                            selected[item[0]] = []
                        selected[item[0]].append(item[1])
                    for item in selected.items():
                        problem_id = item[0]
                        cur.execute('select id from Choice where problemID = %s and isAnswer = true',
                                    (problem_id,))
                        res = cur.fetchall()
                        answer = {item[0] for item in res}
                        cur.execute('select point from TestProblem where testID = %s and problemID = %s',
                                    (test_id, problem_id))
                        point = cur.fetchone()[0]
                        correct = set(item[1])

                        if answer == correct:
                            score += point
                        elif correct.issubset(answer):
                            score += point / 2
                    cur.execute('update TestParticipation set score = %s where userID = %s and testID = %s ',
                                (score, user_id, test_id))
            time.sleep(30)
        except:
            raise ResourceWarning('error in score calculation')

'''

'''