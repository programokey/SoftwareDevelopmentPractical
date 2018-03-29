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
            return redis_conn.get('departments')

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
    try:
        if redis_conn.exists('department_info_%s'%departmentName):
            return redis_conn.get('department_info_%s'%departmentName)
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital', charset='utf8') as cur:
            cur.execute('select name, location, basicStructure, function from Department')
            res = cur.fetchone()
            if len(res) != 1:
                return json.dumps({
                    "code": 404,
                    "data": "Department %s does not exists!"%departmentName
                })

            res = res[0]
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
            for item in res:
                department_info["data"][ "roles"].append(item[0])

            cur.execute('select id, name from Equipment where department = %s', (departmentName,))
            for item in res:
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
        if redis_conn.exists('equipment_info_%s'%equipmentId):
            return redis_conn.get('equipment_info_%s'%equipmentId)
        with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital', charset='utf8') as cur:
            cur.execute('select name, description, operationalApproach, location, flowID from Equipment')
            res = cur.fetchone()
            if len(res) != 1:
                return None

            res = res[0]
            equipment_info = {
                                 "error_code": 0,
                                "data": {
                                      "name":res[0],
                                     "description":res[1],
                                      "operateMethod":res[2],
                                      "location":res[3]
                                    }
                              }
            if res[4] is not  None:
                equipment_info['flow'] = res[4]

            equipment_info = json.dumps(equipment_info)
            redis_conn.set('equipment_info_%s'%equipmentId, value=equipment_info)
            return equipment_info
    except:
        raise Warning('Error during retrieving  equipment %s\'s information'%equipmentId)

def get_department_role_job(departmentName, roleName):
    try:
        if redis_conn.exists('department_role_job_%s_%s'%(departmentName, roleName)):
            return redis_conn.get('department_role_job_%s_%s'%(departmentName, roleName))
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

if __name__ == '__main__':
    with pymysql.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db='PetHospital', charset='utf8') as cur:
        cur.execute("insert into Department value('CT', 'gateway', 'funny', 'CT Scan', 332, 332, 0);")
        cur.execute("insert into Department value('血液科', '二楼楼梯口', '主任: 徳拉古拉·布拉德', '抽血', 233, 233, 0);")
        cur.execute("insert into Department value('精神科', '地下室车库旁', '科室主任:磁暴步兵杨永信', '你需要被电一下', 123, 123, 0);")
    print(get_departments())

'''
insert into Department value('CT', 'gateway', 'funny', 'CT Scan', 332, 332, 0);
insert into Department value('血液科', '二楼楼梯口', '主任: 徳拉古拉·布拉德', '抽血', 233, 233, 0);
insert into Department value('精神科', '地下室车库旁', '科室主任：磁暴步兵杨永信', '你需要被电一下', 123, 123, 0);
'''