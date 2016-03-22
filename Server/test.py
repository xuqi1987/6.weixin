# from  wechatAPI import *
# from xml2json import *
#
# j2x = Xml2json()
# api = WechatAPI()
# #token =  api.get_token()
#
# #api.get_material_list()
#
# t  = Recv_reply_action()
#
# str = '''
# <xml>
#  <ToUserName><![CDATA[toUser]]></ToUserName>
#  <FromUserName><![CDATA[fromUser]]></FromUserName>
#  <CreateTime>1348831860</CreateTime>
#  <MsgType><![CDATA[text]]></MsgType>
#  <Content><![CDATA[this is a test]]></Content>
#  <MsgId>1234567890123456</MsgId>
#  </xml>
#  '''
# t.pre(str)
# print j2x.xml2json(t.reply())
# print j2x.xml2json('''<xml><MsgType>image</MsgType><Image><MediaId><![CDATA[ZmvGRjBvFSDzwiSzZeK_01sdvFXmnwkUeCUd281BrXo6SXAwWJrHijLOSncgUnjL]]></MediaId></Image><FromUserName>gh_23e52455439f</FromUserName><ToUserName>oBIAhwRBAwa3wMmnTHokqysK2cRM</ToUserName><CreateTime>1458580951</CreateTime></xml> ''')

import requests

f = requests.get("http://mmbiz.qpic.cn/mmbiz/NDuqv9w08JkqdM1mXtDibnX37mDib6P9ib44VhvzBk4NDqTib1ZJ47ESuxVsrBxN3v4LFL6oOT4BuHPd7QUKFoDSvA/0")

file = open("2.jpg","w")
file.write(f.content)
file.flush()
file.close()
