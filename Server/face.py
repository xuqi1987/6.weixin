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

    def checkface(self,url):
        face = self.api.detection.detect(url = url)['face']

        if len(face) > 0:
            self.faces.append(face[0]['face_id'])
            return face[0]['face_id']
        return ""

    def getface(self,face_id):
        ret = self.api.info.get_face(face_id=face_id)
        print_result("face",ret)
        return ret

    def get_person_list(self):
        people = self.api.info.get_person_list()['person']
        for item in people:
                yield item['person_name']

    def add_person(self,name,url=None,img=None,id=None):
        print "add_person"
        facesinfo = {}
        faces = []

        if url != None or img != None:
            if url != None:
                # 创建face
                facesinfo = self.api.detection.detect(url = url)
            else:
                facesinfo =self.api.detection.detect(img = img)

            print facesinfo

            if facesinfo.has_key("face") == False:
                return False

            faces = facesinfo['face']

            if len(faces) <= 0:
                print "can not find a face in the pic"
                return False

            face = faces[0]['face_id']

        elif id != None:

            face = id
            pass
        else:
            print "param error"
            return False

        # 如果这个人没有了
        if name not in self.get_person_list():
            rst = self.api.person.create(
                person_name = name, face_id = face)
        # 如果有这个人
        else:
            rst = self.api.person.add_face(
                person_name = name, face_id = face)
        return True

    def add_person_2_group(self,name,groupname='family'):
        print 'add_person_2_group'
        self.api.group.add_person(person_name=name,group_name=groupname)
        print 'train group'
        sessionid = self.api.train.identify(group_name = groupname)
        print 'session id %s' %sessionid
        pass

    def identify(self,groupname='family',faceid=None,url=None):
        print 'identify start'
        rst = self.api.recognition.identify(group_name=groupname,url=url,async=False)
        print rst
        candidate = rst['face'][0]['candidate']
        name = []
        for c in candidate:
            if c['confidence'] > 90:
                name.append(c['person_name'])
        print 'identify end : %s' % ''.join(name)
        return name

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