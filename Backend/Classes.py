
class User(object):
    def __init__(self):
        self.id
        self.passwd
        self.phoneNumber
        self.email
        self.gender
        self.token

    def login(self, id, passwd):
        pass

    def getTests(self):
        '''
        :return: tests the user participate in
        '''
        pass

class TestParticipation:
    def __init__(self):
        self.user
        self.Test
        self.BeginTime
        self.answers
    def getScore(self):
        pass

class Test(object):
    def __init__(self):
        self.id
        self.name
        self.description
        self.startTime
        self.endTime
        self.Duration
        self.problems
        self.confidential
        self.creator

    def getProblems(self):
        pass

    def _getStatus(self):
        pass

class Problem(object):
    def __init__(self):
        self.problem
        self.choices
        self.multipleAnswer
        self.creator
        pass

    def mark(self, answers):
        return 0


class department(object):
    def __init__(self):
        self.name
        self.location # stt
        self.basicStructure
        self.function
        self.jobs # list<Job>
        self.equipments # list<Equipment>
        self.diseaseTreated #list<Disease>

'''
1. 请求医院导览图片：
    /hospitalguide

'''

'''
单元测试：
    Coverage
'''