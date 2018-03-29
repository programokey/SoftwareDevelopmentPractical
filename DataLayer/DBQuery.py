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
            print(res)
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
        return 'Error during retrieving Departments information'

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