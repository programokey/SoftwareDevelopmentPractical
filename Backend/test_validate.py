from unittest import TestCase
from Backend.validate import  *

class TestValidate(TestCase):
    def test_validate(self):
        self.assertFalse(validate(''))

        userID, hash = None, None
        res, token = login(userID, hash)
        expected_result = {'code': 403, 'data': {'result': False}}
        res = json.loads(res)
        self.assertEqual(res, expected_result)
        self.assertEqual(token, None)

        userID = '2333'
        passwd = 'test'
        hash = ''
        redis_conn.delete('user_%s' % userID)
        redis_conn.flushall()
        res, token = login(userID, hash)
        res = json.loads(res)
        expected_result = {'code': 403, 'data': {'result': False}}
        self.assertEqual(res, expected_result)
        self.assertEqual(token, None)

        userID = '0'
        passwd = 'test'
        hash = ''
        redis_conn.delete('user_%s' % userID)
        redis_conn.flushall()
        res, token = login(userID, hash)
        res = json.loads(res)
        expected_result = {'code': 403, 'data': {'result': False}}
        self.assertEqual(res, expected_result)
        self.assertEqual(token, None)

        hash = sha1((userID + '_' + passwd).encode('utf8')).hexdigest()
        res, token = login(userID, hash)
        res = json.loads(res)
        expected_result = {'code': 1000, 'data': {'result': True, 'token': token}}
        self.assertEqual(res, expected_result)

        old_token = token
        res, token = login(userID, hash)
        res = json.loads(res)
        expected_result = {'code': 1000, 'data': {'result': True, 'token': token}}
        self.assertEqual(res, expected_result)

        self.assertFalse(validate(old_token))
        self.assertTrue(validate(token))

        print(type(get_user_id(token)))
        self.assertEqual(get_user_id(token), '0')
        self.assertEqual(get_user_id(old_token), None)
