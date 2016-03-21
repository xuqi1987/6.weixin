 # -*- coding:utf8 -*-
import requests

from ct import *
import time
import xml.etree.cElementTree as ET
from xml2json import Xml2json as x2j
import json

 # 用户处理用户的信息
class Recv_reply_action():
    def __init__(self):
        self.xml_recv = ""
        pass

    def g(self,param):
        return self.xml_recv.find(param).text

    def pre(self,data):
        self.xml_recv = ET.fromstring(data)


    def reply(self):
        xdata = ''
        if self.g(MsgType) == text:
            # 回复文本,并且回复原文
            #xdata = self._do_text_reply(self.g(Content))

            #
            xdata = self._do_image_reply('ZmvGRjBvFSDzwiSzZeK_01sdvFXmnwkUeCUd281BrXo6SXAwWJrHijLOSncgUnjL')

        print "Reply %s "% xdata
        return xdata

    # 根据type创建回复消息格式
    def _create_reply_xml(self,type):
        jdata =  ''
        if type == text:
            jdata = { 'xml':{
                ToUserName:self.g(FromUserName),
                FromUserName:self.g(ToUserName),
                CreateTime:str(int(time.time())),
                MsgType:text,
                Content:"<![CDATA[%s]]>",
                },
            }

        elif type == image:

            jdata = {'xml':{
                ToUserName:self.g(FromUserName),
                FromUserName:self.g(ToUserName),
                CreateTime:str(int(time.time())),
                MsgType:image,
                'Image':{
                    MediaId:"<![CDATA[%s]]>",
                },
                },
            }
        else:
            pass
        rdata = x2j().json2xml(jdata)
        rdata =rdata.replace('&lt;','<')
        rdata = rdata.replace('&gt;','>')

        return rdata

    # 图灵机器人回复
    def _get_tuling_ans(self,context):
        url='http://www.tuling123.com/openapi/api'
        data={'key':'fa78fe2fbb85c914c7126d42bc7c3ebb','info':context,'userid':str(self.g(FromUserName))}
        r = requests.post(url,data=data)
        ans = json.loads(r.text)
        ret = ''
        if ans['code'] == 100000:
            ret = ans['text']
        elif ans['code'] == 200000:
            ret = ans['text'] + '\n' + ans['url']
        elif ans['code'] == 302000:
            ret = ans['text'] + '\n'
            for i in  ans['list']:
                ret = ret + i['article'] + '\n' + i['detailurl'] + '\n\n'
        elif ans['code'] == 308000:
            print ans['text']

        else:
            ret = 'error'

        return ret

    # 回复Text
    def _do_text_reply(self,context):
        # 通过图灵得到回复
        context = self._get_tuling_ans(context)
        # 生成text类型的回复模版
        t = self._create_reply_xml(text)
        # 格式化消息
        t = t % context
        return  t


    def _do_image_reply(self,mediaid):
        t = self._create_reply_xml(image)

        t = t %mediaid
        return t