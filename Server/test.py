# -*- coding:utf8 -*-
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
# <xml>
#  <ToUserName><![CDATA[toUser]]></ToUserName>
#  <FromUserName><![CDATA[fromUser]]></FromUserName>
#  <CreateTime>1348831860</CreateTime>
#  <MsgType><![CDATA[text]]></MsgType>
#  <Content><![CDATA[hello]]></Content>
#  <MsgId>1234567890123456</MsgId>
#  </xml>
#  '''
# t  = Recv_reply_action(str)
# print t.reply()
#
# # t.pre(str)
# # print j2x.xml2json(t.reply())
# # print j2x.xml2json('''<xml><MsgType>image</MsgType><Image><MediaId><![CDATA[ZmvGRjBvFSDzwiSzZeK_01sdvFXmnwkUeCUd281BrXo6SXAwWJrHijLOSncgUnjL]]></MediaId></Image><FromUserName>gh_23e52455439f</FromUserName><ToUserName>oBIAhwRBAwa3wMmnTHokqysK2cRM</ToUserName><CreateTime>1458580951</CreateTime></xml> ''')
#
#

from face import Face as F

gp = "ccc"
# 人名及其脸部图片
IMAGE_DIR = 'http://cn.faceplusplus.com/static/resources/python_demo/'
PERSONS = [
    ('s sdssas', IMAGE_DIR + '1.jpg'),
    ('b sdssss', IMAGE_DIR + '2.jpg'),
    ('c ssdssLdiu', IMAGE_DIR + '3.jpg')
]
TARGET_IMAGE = IMAGE_DIR + '4.jpg'

f = F()
for name,url in PERSONS:
    f.add_person(name,url)

f.create_group(gp)

f.train(gp)

f.recog(gp,TARGET_IMAGE)
f.del_info(gp)
#f.reg_face()

#print f.recog(TARGET_IMAGE)
#f.del_info()