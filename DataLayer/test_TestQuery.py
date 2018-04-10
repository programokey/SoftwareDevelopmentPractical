from unittest import TestCase
import json
from  DataLayer.TestQuery import *

class TestTestQuery(TestCase):
    def test_get_all_test(self):
        userID = 0
        self.assertRaises(AssertionError, get_all_test, userID)

        userID = '0'
        expected_result = json.dumps({'code': 0, 'data': [
            {'id': 1, 'name': 'test测试1', 'description': '测试测试的测试', 'startTime': '20180101/01/18120000',
             'endTime': '20180404/01/18120000', 'duration': 7200, 'score': '22', 'state': '已结束'},
            {'id': 2, 'name': 'test测试2', 'description': '测试测试的测试', 'startTime': '20180404/01/18120000',
             'endTime': '20180505/01/18120000', 'duration': 5400, 'score': '22', 'state': '已结束'},
            {'id': 3, 'name': 'test测试3', 'description': '测试测试的测试', 'startTime': '20180505/01/18120000',
             'endTime': '20180606/01/18120000', 'duration': 5400, 'score': '22', 'state': '未开始'}]})
        self.assertEqual(get_all_test(userID), expected_result)

        userID = '1'
        expected_result = json.dumps({'code': 0, 'data': [
            {'id': 1, 'name': 'test测试1', 'description': '测试测试的测试', 'startTime': '20180101/01/18120000',
             'endTime': '20180404/01/18120000', 'duration': 7200, 'score': '22', 'state': '已结束'},
            {'id': 2, 'name': 'test测试2', 'description': '测试测试的测试', 'startTime': '20180404/01/18120000',
             'endTime': '20180505/01/18120000', 'duration': 5400, 'score': '22', 'state': '进行中'}]})
        self.assertEqual(get_all_test(userID), expected_result)

    def test_get_test_problem(self):
        id = '0'
        self.assertRaises(AssertionError, get_test_problem, id)

        id = 1
        r = redis.Redis()
        r.delete('test_problem_%d' % id)
        r.flushall()
        expected_result = {'single': [{'problemId': 1, 'problem': '测试测试的问题1',
                                       'choice': {1: '测试测试的问题1的答案1', 2: '测试测试的问题1的答案2', 3: '测试测试的问题1的答案3',
                                                  4: '测试测试的问题1的答案4'}, 'ponit': 20.0},
                                      {'problemId': 3, 'problem': '测试测试的问题3',
                                       'choice': {9: '测试测试的问题3的答案1', 10: '测试测试的问题3的答案2', 11: '测试测试的问题3的答案3',
                                                  12: '测试测试的问题3的答案4'}, 'ponit': 20.0}],
                           'multiple': [
                                    {'problemId': 2, 'problem': '测试测试的问题2',
                                     'choice': {5: '测试测试的问题2的答案1', 6: '测试测试的问题2的答案2', 7: '测试测试的问题2的答案3', 8: '测试测试的问题2的答案4'}, 'ponit': 20.0}]}
        self.assertEqual(get_test_problem(id), expected_result)
        self.assertEqual(get_test_problem(id), expected_result)

        id = 2333
        expected_result = None
        self.assertEqual(get_test_problem(id), expected_result)

    def test_get_test(self):
        id = 1
        userID = '0'
        expected_result = {'code': 404, 'data': '不在考试时间内'}
        res = json.loads(get_test(id, userID))
        self.assertEqual(res, expected_result)

        id = 3
        userID = '1'
        expected_result = {'code': 404, 'data': '你没有权限参加此考试'}
        res = json.loads(get_test(id, userID))
        self.assertEqual(res, expected_result)

        id = 2333
        userID = '1'
        expected_result = {'code': 404, 'data': 'No such test'}
        res = json.loads(get_test(id, userID))
        self.assertEqual(res, expected_result)

        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute("update TestParticipation  set beginTime = NULL  where userID = '1' and  testID = 1")
            cur.execute("update TestParticipation  set beginTime = NULL  where userID = '1' and  testID = 2")

        id = 2
        userID = '1'
        expected_result = {'code': 1000, 'data': {'single': [{'problemId': 1, 'problem': '测试测试的问题1',
                                                              'choice': {'1': '测试测试的问题1的答案1', '2': '测试测试的问题1的答案2',
                                                                         '3': '测试测试的问题1的答案3', '4': '测试测试的问题1的答案4'},
                                                              'ponit': 50.0}], 'multiple': [
            {'problemId': 2, 'problem': '测试测试的问题2',
             'choice': {'5': '测试测试的问题2的答案1', '6': '测试测试的问题2的答案2', '7': '测试测试的问题2的答案3', '8': '测试测试的问题2的答案4'},
             'ponit': 50.0}], 'remainingTime': None, 'selected': {'1': [3], '2': [6, 7]}}}
        res = json.loads(get_test(id, userID))
        res['data']['remainingTime'] = None
        self.assertEqual(res, expected_result)

    def test_submit(self):
        testID = 2
        userID = '0'
        answer = '{'
        res = submit(testID, userID, answer)
        expected_result = json.dumps({
            'code': 404,
            'data': 'invalid format!'
        })
        self.assertEqual(res, expected_result)


        testID = 2
        userID = '0'
        answer = json.dumps({
            1: [1, 3],
            2: [6, 7]
        })
        res = submit(testID, userID, answer)
        expected_result = json.dumps({
            'code': 1000,
            'data': 'submit answer succeeded!'
        })
        self.assertEqual(res, expected_result)

        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute("select problemID, choiceID from Answer where userID = %s and  testID = %s",(userID, testID))
            submitted = {}
            for item in cur.fetchall():
                if item[0] not in submitted:
                    submitted[item[0]] = []
                submitted[item[0]].append(item[1])

        self.assertEqual(submitted, {
            1: [1, 3],
            2: [6, 7]
        })

    def test_score_calculate(self):
        from threading import Thread
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute("update TestParticipation set score = NULL where userID = '0' and testID = 1")
            cur.execute("update TestParticipation set score = NULL where userID = '1' and testID = 1")

        score_calculation = Thread(target=score_calculate)
        score_calculation.setDaemon(True)
        score_calculation.start()
        time.sleep(10)
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            userID, testID = '0', 1
            cur.execute("select score from TestParticipation where userID = %s and  testID = %s", (userID, testID))
            self.assertEqual(cur.fetchone()[0], 30.0)

            userID, testID = '1', 1
            cur.execute("select score from TestParticipation where userID = %s and  testID = %s", (userID, testID))
            self.assertEqual(cur.fetchone()[0], 60.0)

        score_calculation.join(timeout=10)