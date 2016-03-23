# -*- coding: utf-8 -*-

API_KEY = '3fd269fc978b1159373f8480211ffc81'
API_SECRET = '9SdqAcTYA273l5Nh1b71dD2RA82Fs8CQ'

# Import system libraries and define helper functions
# 导入系统库并定义辅助函数
import time
from pprint import pformat
def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(k): encode(v) for (k, v) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hint
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])


# 首先，导入SDK中的API类
from facepp import API

class Face():
    def __init__(self):
        API_KEY = '3fd269fc978b1159373f8480211ffc81'
        API_SECRET = '9SdqAcTYA273l5Nh1b71dD2RA82Fs8CQ'
        self.api = API(API_KEY, API_SECRET)
        self.persons = []
        self.faces = []

        pass


    def add_person(self,name,url):

        # 创建face
        self.faces = {name: self.api.detection.detect(url = url)}

        # 创建person
        for name, face in self.faces.iteritems():
            rst = self.api.person.create(
                    person_name = name, face_id = face['face'][0]['face_id'])
        pass


    def create_group(self,groupname):
        self.api.group.create(group_name = groupname)
        self.api.group.add_person(group_name = groupname, person_name = self.faces.iterkeys())
        pass

    def train(self,groupname):
        rst = self.api.train.identify(group_name = groupname)
        rst = self.api.wait_async(rst['session_id'])
        pass

    def recog(self,groupname,url):
        rst = self.api.recognition.identify(group_name = groupname, url = url)
        print_result('recognition result', rst)
        print '=' * 60
        print 'The person with highest confidence:', \
                rst['face'][0]['candidate'][0]['person_name']

    def del_info(self,groupname):
        self.api.group.delete(group_name = groupname)
        self.api.person.delete(person_name = self.faces.iterkeys())