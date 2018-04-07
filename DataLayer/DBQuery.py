# _*_coding:utf8_*_
import configparser
import json
import pymysql, redis

cf = configparser.ConfigParser()
cf.read('pethospital.conf')
mysql_user = cf.get('mysqldb', 'user')
mysql_passwd = cf.get('mysqldb', 'passwd')
mysql_host = cf.get('mysqldb', 'host')
redis_conn = redis.Redis()

def get_user(user):
    assert isinstance(user, str)
    try:
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital', charset='utf8') as cur:
            cur.execute('select * from PetHospital.User where name = %s', (user,))
            queryRes = cur.fetchall()[0]
            if queryRes is None:
                return None
            return {'id': queryRes[0],
                    'name': queryRes[1], 'passwd': queryRes[2],
                    'phoneNumber': queryRes[3], 'email': queryRes[4], 'gender': queryRes[5]}
    except:
        return None

def get_departments():
    try:
        if redis_conn.exists('departments'):
            return redis_conn.get('departments').decode('utf8')

        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital', charset='utf8') as cur:
            cur.execute('select name, x_pos, y_pos from Department')
            res = cur.fetchall()
            departments = {
                "code": 1000,
                "data": []
            }
            for item in res:
                departments["data"].append({'name': item[0], 'pos': '%d, %d' % (item[1], item[2])})
            departments = json.dumps(departments)
            redis_conn.set('departments', value=departments)
            return departments
    except:
        return json.dumps({
            "code": 233,
            "data": "Error while get departments list"
        })


def get_department_info(departmentName):
    assert isinstance(departmentName, str)
    try:
        if redis_conn.exists('department_info_%s'%departmentName):
            return redis_conn.get('department_info_%s'%departmentName).decode('utf8')
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital', charset='utf8') as cur:
            cur.execute('select name, location, basicStructure, function from Department where name = %s', (departmentName, ))
            res = cur.fetchone()
            if res is None:
                return json.dumps({
                                        "code": 404,
                                        "data": "Department %s does not exists!"%departmentName
                                    })
            department_info = {
                                    "code": 1000,
                                    "data": {
                                      "name": res[0],
                                      "location": res[1],
                                      "basicStructure": res[2],
                                      "function": res[3],
                                      "roles": [],
                                      "equipments": {}
                                    }
                        }
            cur.execute('select role from DepartmentRole where department = %s', (departmentName,))
            for item in cur.fetchall():
                department_info["data"][ "roles"].append(item[0])

            cur.execute('select id, name from Equipment where department = %s', (departmentName,))
            for item in cur.fetchall():
                department_info["data"]["equipments"][item[0]] = item[1]

            department_info = json.dumps(department_info)
            redis_conn.set('department_info_%s'%departmentName, value=department_info)
            return department_info
    except:
        return json.dumps({
            "code": 200,
            "data": "Error during getting information of Department %s!" % departmentName
        })

def get_equipment(equipmentId):
    try:
        try:
            equipmentId = int(equipmentId)
        except:
            return json.dumps({
                "code": 404,
                "data": "%s  is not a valid equipment ID!" % equipmentId
            })
        # if redis_conn.exists('equipment_info_%s'%equipmentId):
        #     return redis_conn.get('equipment_info_%s'%equipmentId).decode('utf8')
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital', charset='utf8') as cur:
            cur.execute('select name, description, operationalApproach, location, flowID from Equipment where id = %s', (equipmentId, ))
            res = cur.fetchone()
            if res is None:
                return json.dumps({
                                        "code": 404,
                                        "data": "equipment %d does not exists!"%equipmentId
                                    })

            equipment_info = {
                                 "error_code": 1000,
                                "data": {
                                      "name":res[0],
                                     "description":res[1],
                                      "operateMethod":res[2],
                                      "location":res[3]
                                    }
                              }
            if res[4] is not None:
                equipment_info['data']['flow'] = res[4]

            equipment_info = json.dumps(equipment_info)
            redis_conn.set('equipment_info_%s'%equipmentId, value=equipment_info)
            return equipment_info
    except:
        raise Warning('Error during retrieving equipment %s\'s information'%equipmentId)

def get_department_role_job(departmentName, roleName):
    assert isinstance(departmentName, str)
    assert isinstance(roleName, str)

    try:
        if redis_conn.exists('department_role_job_%s_%s'%(departmentName, roleName)):
            return redis_conn.get('department_role_job_%s_%s'%(departmentName, roleName)).decode('utf8')
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('select job from RoleJob where role = %s and department = %s ', (roleName, departmentName))
            res = cur.fetchall()
            jobs = {
                "code": 1000,
                "data": []
            }
            for item in res:
                jobs["data"].append(item[0])
            jobs = json.dumps(jobs)
            redis_conn.set('department_role_job_%s_%s'%(departmentName, roleName), value=jobs)
            return jobs
    except:
        return json.dumps({
            "code": 404,
            "data": "Error during getting jobs of Role %s in  Department %s!" %(roleName, departmentName)
        })

def get_role_job(roleName):
    assert isinstance(roleName, str)

    try:
        if redis_conn.exists('role_job_%s'%roleName):
            return redis_conn.get('role_job_%s'%roleName).decode('utf8')
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('select job from RoleJob where role = %s', (roleName,))
            res = cur.fetchall()
            jobs = {
                "code": 1000,
                "data": []
            }
            for item in res:
                jobs["data"].append(item[0])
            jobs = json.dumps(jobs)
            redis_conn.set('role_job_%s'%roleName, value=jobs)
            return jobs
    except:
        return json.dumps({
            "code": 404,
            "data": "Error during getting jobs of Role %s!" %roleName
        })

def get_job_detail(jobName):
    assert isinstance(jobName, str)

    try:
        if redis_conn.exists('job_%s' % jobName):
            return redis_conn.get('job_%s' % jobName).decode('utf8')
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('select description, dosAndDonots, jobFlowID from Job where name = %s', (jobName,))
            res = cur.fetchone()
            if res is None:
                return json.dumps({
                    'code': 404,
                    'data': 'No such job!'
                })
            detail = {
                        "code": 1000,
                        "data": {
                            "description": res[0],
                            "dosAndDonots": res[1]
                        }
                      }

            if res[2] is not None:
                detail['data']['jobflow'] = res[2]
            detail = json.dumps(detail)
            redis_conn.set('job_%s' % jobName, value=detail)
            return detail
    except:
        return json.dumps({
            "code": 404,
            "data": "Error during getting details of the jobs %s!" % jobName
        })

def get_flow(flowId):
    assert isinstance(flowId, int)

    try:
        if redis_conn.exists('flow_%d' % flowId):
            return redis_conn.get('flow_%d' % flowId).decode('utf8')
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('select content, `type`, description from Flow where id = %s order by `order`', (flowId,))
            res = cur.fetchall()
            if len(res) == 0:
                return json.dumps({
                    'code': 404,
                    'data': 'No such flow!'
                })
            flow = {
                "code": 1000,
                "data": []
            }
            for item in res:
                flow['data'].append({
                    'content': item[0],
                    'type': item[1],
                    'description': item[2]
                })
            flow = json.dumps(flow)
            redis_conn.set('flow_%d' % flowId, value=flow)
            return flow
    except:
        return json.dumps({
            "code": 404,
            "data": "Error during getting details of the flow %d!" % flowId
        })

def get_medicine(approveNumber):
    assert isinstance(approveNumber, str)
    try:
        if redis_conn.exists('medicine_%s' % approveNumber):
            return redis_conn.get('medicine_%s' % approveNumber).decode('utf8')

        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('select name, description, price from Medicine where ApprovalNumber = %s', (approveNumber,))
            res = cur.fetchone()
            if res is None:
                return json.dumps({
                    'code': 404,
                    'data': 'No such medicine!'
                })
            medicine = {
                "error_code": 1000,
                "data": {
                    "name": res[0],
                    "description": res[1],
                    "price": res[2]
                }
            }
            medicine = json.dumps(medicine)
            redis_conn.set('medicine_%s' % approveNumber, value=medicine)
            return medicine
    except:
        return json.dumps({
            "code": 404,
            "data": "Error during getting details of the medicine %s!" % approveNumber
        })

def get_disease_categories():
    try:
        if redis_conn.exists('disease_categories'):
            return redis_conn.get('disease_categories').decode('utf8')

        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('select diseaseCategory, name from Disease')
            res = cur.fetchall()
            disease_categories = {
                "code": 1000,

            }
            data = {}
            for item in res:
                if item[0] not in data:
                    data[item[0]] = []
                data[item[0]].append(item[1])
            disease_categories['data'] = data
            disease_categories = json.dumps(disease_categories)
            redis_conn.set('disease_categories', value=disease_categories)
            return disease_categories
    except:
        return json.dumps({
            "code": 404,
            "data": "Error during getting disease categories!"
        })


def get_cases(diseaseName):
    try:
        if redis_conn.exists('cases_%s'%diseaseName):
            return redis_conn.get('cases_%s'%diseaseName).decode('utf8')

        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('select doctor, petType, petAge, petGender from `Case` where disease = %s', (diseaseName, ))
            res = cur.fetchall()
            if len(res) == 0:
                return json.dumps({
                    'code': 404,
                    'data': 'No such disease!'
                })

            cases = {
                "code": 1000,
            }
            data = []
            for item in res:
                data.append({
                    'doctor': item[0],
                    'petType': item[1],
                    'petAge': item[2],
                    'petGender': item[3]
                })
            cases['data'] = data
            cases = json.dumps(cases)
            redis_conn.set('cases_%s'%diseaseName, value=cases)
            return cases
    except:
        return json.dumps({
            "code": 404,
            "data": "Error during getting disease categories!"
        })

def get_examination_result(id):
    try:
        if redis_conn.exists('examination_result_%d'%id):
            return redis_conn.get('examination_result_%d'%id).decode('utf8')

        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('select examination, conclusion from CaseExamination where id = %s', (id,))
            res = cur.fetchone()
            if res is None:
                return json.dumps({
                    'code': 404,
                    'data': 'No such examination result!'
                })
            examination_result = {
                "code": 1000,
            }
            data = {}
            data['name'] = res[0]
            data['conclusion'] = res[1]
            graphic_result = []
            cur.execute(
                'select picture, description from GraphicMedicalExaminationResult where caseExaminationID = %s',
                (id,))
            res = cur.fetchall()
            for item in res:
                graphic_result.append({
                    'picture': item[0],
                    'description': item[1],
                })
            cur.execute(
                'select name, value, unit, description, low, high value '
                'from NumericalMedicalExaminationResult natural join NumericalIndex '
                'where caseExaminationID = %s',
                (id,))
            res = cur.fetchall()
            numerical_result = []

            for item in res:
                numerical_result.append({
                    'name': item[0],
                    'value': item[1],
                    'unit': item[2],
                    'description': item[3],
                    'low':item[4],
                    'hig': item[5]
                })
            data['graphicResult'] = graphic_result
            data['numercalResult'] = numerical_result
            examination_result['data'] = data
            examination_result = json.dumps(examination_result)
            redis_conn.set('examination_result_%d'%id, value=examination_result)
            return examination_result
    except:
        return json.dumps({
            "code": 404,
            "data": "Error during getting disease categories!"
        })



def get_prescription(id):
    try:
        if redis_conn.exists('prescription_%d'%id):
            return redis_conn.get('prescription_%d'%id).decode('utf8')

        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
                             charset='utf8') as cur:
            cur.execute('select description from Prescription where id = %s', (id,))
            res = cur.fetchone()
            if res is None:
                return json.dumps({
                    'code': 404,
                    'data': 'No such Prescription!'
                })
            description = res[0]
            cur.execute(
                'select medicineApprovalNumber, medicineName, unit from PrescriptionMedicine where PrescriptionID = %s',
                (id,))
            res = cur.fetchall()
            prescription = {
                "code": 1000,
            }
            medicine = []
            for item in res:
                medicine.append({
                    'approvalNumber': item[0],
                    'name': item[1],
                    'unit': item[2],
                })
            data = {}
            data['description'] = description
            data['medicine'] = medicine
            prescription['data'] = data
            prescription = json.dumps(prescription)
            redis_conn.set('disease_categories', value=prescription)
            return prescription
    except:
        return json.dumps({
            "code": 404,
            "data": "Error during getting disease categories!"
        })

def get_case_detail(caseId):
    pass


if __name__ == '__main__':
    # with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital',
    #                      charset='utf8') as cur:
    #     cur.execute("delete from Prescription")
    #     cur.execute("delete from PrescriptionMedicine")
    #
    #     cur.execute("insert into Prescription value(1, 1, '针对哈士奇先天性心眼不足的药物治疗');")
    #     cur.execute("insert into PrescriptionMedicine value(1, '滑稽准字FDA2333', '脑残片', 12);")
    #     cur.execute("insert into PrescriptionMedicine value(1, '滑稽准字FDA233', '伸腿瞪眼丸', 2);")
    #     cur.execute("insert into Prescription value(2, 1, '针对哈士奇先天性心眼不足的药物治疗的补充');")
    #     cur.execute("insert into PrescriptionMedicine value(2, '滑稽准字FDA2333', '脑残片', 12);")
    #     cur.execute("insert into PrescriptionMedicine value(2, '滑稽准字FDA233', '伸腿瞪眼丸', 2);")

    id = 1
    print(json.loads(get_prescription(id)))

    id = 2
    print(json.loads(get_prescription(id)))


'''
insert into Department value('CT', 'gateway', 'funny', 'CT Scan', 332, 332, 0);
insert into Department value('血液科', '二楼楼梯口', '主任: 徳拉古拉·布拉德', '抽血', 233, 233, 0);
insert into Department value('精神科', '地下室车库旁', '科室主任：磁暴步兵杨永信', '你需要被电一下', 123, 123, 0);
'''