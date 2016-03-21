from  wechatAPI import *


api = WechatAPI()
token =  api.get_token()

api.get_material_list()

t  = Recv_reply_action()

str = '''
<xml>
 <ToUserName><![CDATA[toUser]]></ToUserName>
 <FromUserName><![CDATA[fromUser]]></FromUserName>
 <CreateTime>1348831860</CreateTime>
 <MsgType><![CDATA[text]]></MsgType>
 <Content><![CDATA[this is a test]]></Content>
 <MsgId>1234567890123456</MsgId>
 </xml>
 '''
t.pre(str)
t.reply()