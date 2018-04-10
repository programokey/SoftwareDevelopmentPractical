from unittest import TestCase
from DataLayer.DBQuery import *
import json
import redis

class TestDBQuery(TestCase):
    def test_get_user(self):
        self.assertRaises(AssertionError, get_user, 233)
        self.assertEqual(get_user('2333'), None)
        self.assertEqual(get_user('0'), {'id': '0', 'name': 'test', 'passwd': 'test',
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

        print(json.loads(get_department_info(departmentName)))
        self.assertEqual(get_department_info(departmentName), expected_result)

        # test get redis cache
        self.assertEqual(get_department_info(departmentName), expected_result)

    def test_get_equipment(self):
        equipmentId = 5
        expected_result = json.dumps({'code': 404,
                                      'data': 'equipment 5 does not exists!'})
        self.assertEqual(get_equipment(equipmentId), expected_result)

        equipmentId = 1
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

        equipmentId = 4
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


    def test_get_department_role_job(self):
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

    def test_get_role_job(self):
        roleName = 233
        self.assertRaises(AssertionError, get_role_job, roleName)

        roleName = '杨永信'
        r = redis.Redis()
        r.delete('role_job_%s'%roleName)
        r.flushall()
        expected_result = json.dumps({'code': 1000, 'data': ['十万伏特', '我觉得你需要被电一下']})
        self.assertEqual(get_role_job(roleName), expected_result)
        # test get redis cache
        self.assertEqual(get_role_job(roleName), expected_result)

    def test_get_job_detail(self):
        jobName = 233
        self.assertRaises(AssertionError, get_user, jobName)

        jobName = '吟唱'
        expected_result = json.dumps({'code': 404, 'data': 'No such job!'})
        self.assertEqual(get_job_detail(jobName), expected_result)

        expected_result = json.dumps({'code': 1000, 'data': {'description': '判断病患是否需要点击', 'dosAndDonots': '注意观察'}})
        jobName = '我觉得你需要被电一下'
        r = redis.Redis()
        r.delete('job_%s' % jobName)
        r.flushall()
        self.assertEqual(get_job_detail(jobName), expected_result)
        self.assertEqual(get_job_detail(jobName), expected_result)


        expected_result = json.dumps({'code': 1000, 'data': {'description': '污染患者精神', 'dosAndDonots': '每天早晚各一次', 'jobflow': 0}})
        jobName = '精神污染'
        self.assertEqual(get_job_detail(jobName), expected_result)

    def test_get_flow(self):
        flowId = '233'
        self.assertRaises(AssertionError, get_flow, flowId)

        flowId = 0
        r = redis.Redis()
        r.delete('flow_%d' % flowId)
        r.flushall()
        expected_result = json.dumps(
            {'code': 1000, 'data': [{'content': '/flow/1.jpg', 'type': 'Picture', 'description': '展示Doge图片'},
                                    {'content': '/flow/2.avi', 'type': 'Video', 'description': '播放Doge视频'}]})
        self.assertEqual(get_flow(flowId), expected_result)
        self.assertEqual(get_flow(flowId), expected_result)

        flowId = 2333
        expected_result = json.dumps(
            {'code': 404, 'data': 'No such flow!'})
        self.assertEqual(get_flow(flowId), expected_result)

    def test_get_medicine(self):
        approveNumber = 2333
        self.assertRaises(AssertionError, get_medicine, approveNumber)

        approveNumber = '滑稽准字FDA233'
        r = redis.Redis()
        r.delete('medicine_%s' % approveNumber)
        r.flushall()
        expected_result = json.dumps(
            {'error_code': 1000,
             'data': {'name': '伸腿瞪眼丸', 'description': '不论男女老幼,疑难杂症,服用此药后,即刻痊愈,只溶在口,不溶在手', 'price': 2.33}})
        self.assertEqual(get_medicine(approveNumber), expected_result)
        self.assertEqual(get_medicine(approveNumber), expected_result)

        approveNumber = '滑稽准字FDA2333'
        expected_result = json.dumps({'error_code': 1000, 'data': {'name': '脑残片', 'description': '用于提高智商', 'price': 250.0}})
        self.assertEqual(get_medicine(approveNumber), expected_result)

        approveNumber = '滑稽准字FFDA2333'
        expected_result = json.dumps({'code': 404, 'data': 'No such medicine!'})
        self.assertEqual(get_medicine(approveNumber), expected_result)

    def test_get_disease_categories(self):
        r = redis.Redis()
        r.delete('disease_categories')
        r.flushall()
        expected_result = json.dumps({'code': 1000, 'data': {'嗜睡': ['上课睡觉', '早上睡不醒'], '缺心眼': ['先天性心眼不足']}})
        self.assertEqual(get_disease_categories(), expected_result)
        self.assertEqual(get_disease_categories(), expected_result)

    def test_get_cases(self):
        diseaseName = 2333
        self.assertRaises(AssertionError, get_cases, diseaseName)

        diseaseName = '先天性心眼不足'
        r = redis.Redis()
        r.delete('cases_%s'%diseaseName)
        r.flushall()
        expected_result = json.dumps({'code': 1000, 'data': [
            {'doctor': '杨永信', 'petType': '哈士奇', 'petAge': '2.333岁', 'petGender': 'unknown'},
            {'doctor': '杨永信', 'petType': '阿拉斯加', 'petAge': '3岁', 'petGender': 'unknown'}]})
        self.assertEqual(get_cases(diseaseName), expected_result)
        self.assertEqual(get_cases(diseaseName), expected_result)


        diseaseName = '持续性混吃等死'
        expected_result = json.dumps({'code': 404, 'data': 'No such disease!'})
        self.assertEqual(get_cases(diseaseName), expected_result)

    def test_get_prescription(self):
        id = '2333'
        self.assertRaises(AssertionError, get_prescription, id)


        id = 1
        r = redis.Redis()
        r.delete('prescription_%d'%id)
        r.flushall()
        expected_result = json.dumps({'code': 1000, 'data': {'description': '针对哈士奇先天性心眼不足的药物治疗', 'medicine': [
            {'approvalNumber': '滑稽准字FDA233', 'name': '伸腿瞪眼丸', 'unit': 2.0},
            {'approvalNumber': '滑稽准字FDA2333', 'name': '脑残片', 'unit': 12.0}]}})
        self.assertEqual(get_prescription(id), expected_result)
        self.assertEqual(get_prescription(id), expected_result)


        id = 0
        expected_result = json.dumps({'code': 404, 'data': 'No such Prescription!'})
        self.assertEqual(get_prescription(id), expected_result)



    def test_get_operation(self):
        operationName = 2333
        self.assertRaises(AssertionError, get_operation, operationName)

        operationName = '精神污染术'
        r = redis.Redis()
        r.delete('operation_%s'%operationName)
        r.flushall()
        expected_result = json.dumps({'code': 1000,
                                      'data': {'name': '精神污染术', 'description': '对患者进行精神污染', 'dosAndDonots': '需反复治疗',
                                               'price': 2333.3,
                                               'medicines': {'滑稽准字FDA233': '伸腿瞪眼丸', '滑稽准字FDA2333': '脑残片'},
                                               'equipments': {'3': '滑机', '4': '垃机'}}})
        self.assertEqual(get_operation(operationName), expected_result)
        self.assertEqual(get_operation(operationName), expected_result)

        operationName = '2233'
        expected_result = json.dumps({'code': 404, 'data': 'No such operation!'})
        self.assertEqual(get_operation(operationName), expected_result)


    def test_get_case_detail(self):
        id = '2333'
        self.assertRaises(AssertionError, get_case_detail, id)

        id = 1
        r = redis.Redis()
        r.delete('case_%d'%id)
        r.flushall()
        expected_result = json.dumps({'code': 1000, 'data': {'doctor': '杨永信', 'petType': '哈士奇', 'petAge': '2.333岁',
                                                             'petGender': 'unknown', 'disease': '先天性心眼不足',
                                                             'symptoms': '时常犯二', 'diagnosis': '经诊断为典型的先天性缺心眼',
                                                             'treatment': '使用脑残片进行药物治疗', 'expense': 2.333, 'flow': 1,
                                                             'examinationResult': {'1': '脑部MR'},
                                                             'operations': {'1': '精神污染术'}, 'prescriptions': [1, 2]}})
        self.assertEqual(get_case_detail(id), expected_result)
        self.assertEqual(get_case_detail(id), expected_result)


        id = 2333
        expected_result = json.dumps({'code': 404, 'data': 'No such case!'})
        self.assertEqual(get_case_detail(id), expected_result)

    def test_get_examination_result(self):
        id = '2333'
        self.assertRaises(AssertionError, get_examination_result, id)

        id = 1
        r = redis.Redis()
        r.delete('examination_result_%d'%id)
        r.flushall()
        expected_result = json.dumps({'code': 1000, 'data': {'name': '脑部MR', 'conclusion': '轻度脑残', 'graphicResult': [
            {'picture': '/ExaminationResult/BrainMR/husky1.jpg', 'description': '脑洞过大'},
            {'picture': '/ExaminationResult/BrainMR/husky2.jpg', 'description': ''}], 'numercalResult': [
            {'name': '智商', 'value': 233.0, 'unit': '', 'description': '智商值', 'low': 60.0, 'hig': 100.0},
            {'name': '脑洞数量', 'value': 5.0, 'unit': '个', 'description': '脑洞数量', 'low': 0.0, 'hig': 3.0}]}})
        self.assertEqual(get_examination_result(id), expected_result)
        self.assertEqual(get_examination_result(id), expected_result)

        id = 2333
        expected_result = json.dumps({'code': 404, 'data': 'No such examination result!'})
        self.assertEqual(get_examination_result(id), expected_result)