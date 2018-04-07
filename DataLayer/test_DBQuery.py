from unittest import TestCase
from DataLayer.DBQuery import *
import json
import redis

class TestDBQuery(TestCase):
    def test_get_user(self):
        self.assertRaises(AssertionError, get_user, 233)
        self.assertEqual(get_user('2333'), None)
        self.assertEqual(get_user('test'), {'id': '0', 'name': 'test', 'passwd': 'test',
                                            'phoneNumber': '2333', 'email': 'test@test.com',
                                            'gender': 'male'})


    def test_get_departments(self):
        r = redis.Redis()
        r.delete('departments')
        r.flushall()
        expected_result = json.dumps({"code": 1000,
                                     "data": [
                                          {"name": "CT", "pos": "332, 332"},
                                          {"name": "精神科", "pos": "123, 123"},
                                          {"name": "血液科", "pos": "233, 233"}]})
        self.assertEqual(get_departments(), expected_result)

        # test get redis cache
        self.assertEqual(get_departments(), expected_result)

    def test_get_department_info(self):
        self.assertRaises(AssertionError, get_department_info, 233)
        departmentName = '滑稽科'
        self.assertEqual(get_department_info(departmentName), json.dumps({
                    "code": 404,
                    "data": "Department %s does not exists!"%departmentName
                }))
        r = redis.Redis()
        departmentName = '精神科'
        r.delete('department_info_%s'%departmentName)
        r.flushall()

        expected_result = json.dumps({'code': 1000,
                                               'data': {
                                                   'name': '精神科',
                                                   'location': '地下室车库旁',
                                                   'basicStructure': '科室主任：磁暴步兵杨永信',
                                                   'function': '你需要被电一下',
                                                   'roles': ['Professor X', '杨永信'],
                                                   'equipments': {'1': '电击治疗仪', '2': 'CT机', '3': '滑机', '4': '垃机'}}})
        self.assertEqual(get_department_info(departmentName), expected_result)

        # test get redis cache
        self.assertEqual(get_department_info(departmentName), expected_result)

    def test_get_equipment(self):
        equipmentId = 'one'
        expected_result = json.dumps({'code': 404,
                                      'data': 'one  is not a valid equipment ID!'})
        self.assertEqual(get_equipment(equipmentId), expected_result)

        equipmentId = '1'
        r = redis.Redis()
        r.delete('equipment_info_%s' % equipmentId)
        r.flushall()
        expected_result = json.dumps({'error_code': 1000,
                    'data': {
                        'name': '电击治疗仪',
                        'description': '用于电击小朋友',
                        'operateMethod': '',
                        'location': '精神科电击室'
                    }})
        self.assertEqual(get_equipment(equipmentId),  expected_result)
        # test get redis cache
        self.assertEqual(get_equipment(equipmentId), expected_result)

        equipmentId = '4'
        expected_result = json.dumps({'error_code': 1000,
                                      'data': {
                                          'name': '垃机',
                                          'description': '用于排除垃圾思想',
                                          'operateMethod': '',
                                          'location': '精神科排毒室',
                                          'flow': 1
                                      }
                                    })
        self.assertEqual(get_equipment(equipmentId), expected_result)


    def get_department_role_job(self):
        departmentName = 2333
        roleName = '杨永信'
        self.assertRaises(AssertionError, get_department_role_job, departmentName, roleName)

        departmentName = '精神科'
        roleName = 2333
        self.assertRaises(AssertionError, get_department_role_job, departmentName, roleName)

        departmentName = '精神科'
        roleName = '杨永信'
        r = redis.Redis()
        r.delete('department_role_job_%s_%s'%(departmentName, roleName))
        r.flushall()
        expected_result = json.dumps({'code': 1000, 'data': ['十万伏特', '我觉得你需要被电一下']})
        self.assertEqual(get_department_role_job(departmentName, roleName), expected_result)
        # test get redis cache
        self.assertEqual(get_department_role_job(departmentName, roleName), expected_result)






    def test_get_job_detail(self):
        jobName = '我觉得你需要被电一下'
        print(json.loads(get_job_detail(jobName)))

        jobName = '精神污染'
        print(json.loads(get_job_detail(jobName)))

    def test_get_flow(self):
        flowId = 0
        print(json.loads(get_flow(flowId)))

        flowId = 2333
        print(json.loads(get_flow(flowId)))

    def test_get_medicine(self):
        approveNumber = '滑稽准字FDA233'
        print(json.loads(get_medicine(approveNumber)))

        approveNumber = '滑稽准字FDA2333'
        print(json.loads(get_medicine(approveNumber)))

        approveNumber = '滑稽准字FFDA2333'
        print(json.loads(get_medicine(approveNumber)))

    def test_get_disease_categories(self):
        print(json.loads(get_disease_categories()))

    def test_get_cases(self):
        diseaseName = '先天性心眼不足'
        print(json.loads(get_cases(diseaseName)))

        diseaseName = '早上睡不醒'
        print(json.loads(get_cases(diseaseName)))

    def test_get_prescription(self):
        id = 1
        print(json.loads(get_prescription(id)))

        id = 2
        print(json.loads(get_prescription(id)))


    def test_get_operation(self):
        operationName = '精神污染术'
        print(json.loads(get_operation(operationName)))

        operationName = '2233'
        print(json.loads(get_operation(operationName)))

    def test_get_case_detail(selfs):
        id = 1
        print(json.loads(get_case_detail(1)))