# # -*- coding:utf8 -*-
# from  wechatAPI import *
# from xml2json import *
# #
# # j2x = Xml2json()
# # api = WechatAPI()
# # #token =  api.get_token()
# #
# # #api.get_material_list()
#
#
# #
# str = '''
# <xml><ToUserName><![CDATA[gh_23e52455439f]]></ToUserName>
# <FromUserName><![CDATA[oBIAhwRBAwa3wMmnTHokqysK2cRM]]></FromUserName>
# <CreateTime>1458833072</CreateTime>
# <MsgType><![CDATA[image]]></MsgType>
# <PicUrl><![CDATA[http://mmbiz.qpic.cn/mmbiz/NDuqv9w08JkqdM1mXtDibnRBaVPYr0K24F5GeVJXuqibuvYiawFicLmd8SgJgKTYC1mqBQ8nO9F3iaknWRFBicq7IOFg/0]]></PicUrl>
# <MsgId>6265640334966857004</MsgId>
# <MediaId><![CDATA[0NQfsmPw4Idpa52nBIJKLgAvRFkXcBfkllQBIydQeLm1doVMpQAuENDg_-FcWEJ3]]></MediaId>
# </xml>
#  '''
# t  = Recv_reply_action(str)
# #print t.reply()
# #
# # #
# # str = '''
# # <xml><ToUserName><![CDATA[gh_23e52455439f]]></ToUserName>
# # <FromUserName><![CDATA[oBIAhwRBAwa3wMmnTHokqysK2cRM]]></FromUserName>
# # <CreateTime>1458833072</CreateTime>
# # <MsgType><![CDATA[image]]></MsgType>
# # <PicUrl><![CDATA[https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png]]></PicUrl>
# # <MsgId>6265640334966857004</MsgId>
# # <MediaId><![CDATA[0NQfsmPw4Idpa52nBIJKLgAvRFkXcBfkllQBIydQeLm1doVMpQAuENDg_-FcWEJ3]]></MediaId>
# # </xml>
# #  '''
# # t  = Recv_reply_action(str)
# # print t.reply()
#
# print t._do_face_check_reply("1e377d5a04728ba452964e588267ed00")
#
#
# # t.pre(str)
# # print j2x.xml2json(t.reply())
# # print j2x.xml2json('''<xml><MsgType>image</MsgType><Image><MediaId><![CDATA[ZmvGRjBvFSDzwiSzZeK_01sdvFXmnwkUeCUd281BrXo6SXAwWJrHijLOSncgUnjL]]></MediaId></Image><FromUserName>gh_23e52455439f</FromUserName><ToUserName>oBIAhwRBAwa3wMmnTHokqysK2cRM</ToUserName><CreateTime>1458580951</CreateTime></xml> ''')
#
# #
#
# # from face import Face as F
# #
# # gp = "ccc"
# # # 人名及其脸部图片
# # IMAGE_DIR = 'http://cn.faceplusplus.com/static/resources/python_demo/'
# # PERSONS = [
# #     ('s sdssas', IMAGE_DIR + '1.jpg'),
# #     ('b sdssss', IMAGE_DIR + '2.jpg'),
# #     ('c ssdssLdiu', IMAGE_DIR + '3.jpg')
# # ]
# # TARGET_IMAGE = IMAGE_DIR + '4.jpg'
# #
# # f = F()
# # for name,url in PERSONS:
# #     f.add_person(name,url)
# #
# # f.create_group(gp)
# #
# # f.train(gp)
# #
# # f.recog(gp,TARGET_IMAGE)
# # f.del_info(gp)
# #f.reg_face()
#
# #print f.recog(TARGET_IMAGE)
# #f.del_info()
API_KEY = '3fd269fc978b1159373f8480211ffc81'
API_SECRET = '9SdqAcTYA273l5Nh1b71dD2RA82Fs8CQ'
from facepp import API,File

api = API(API_KEY, API_SECRET)
# rst = api.group.create(group_name = 'family')
api.group.add_person(group_name = 'family',person_name='奶奶')
# api.detection.detect(img=File('/Users/xuqi/Documents/proj/6.weixin/Server/img/liudehua_1458996111.24.jpg'))
#
# dict = {"a" : "apple", "b" : "banana"}
# print dict
# dict2 = {"a" : "grape", "d" : "orange"}
# dict.update(dict2)
# print dict