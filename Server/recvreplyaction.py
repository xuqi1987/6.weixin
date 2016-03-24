 # -*- coding:utf8 -*-
import requests

from ct import *
import time
import xml.etree.cElementTree as ET
from xml2json import Xml2json as x2j
import json
from face import Face


 # 用户处理用户的信息
class Recv_reply_action():
    def __init__(self,data):
        self.xml_recv = ET.fromstring(data)
        # 处理的函数
        self.f_do = {
            text : self._do_text_reply,# 回复文本,并且回复原文
            image : self._do_image_reply # 回复图片
        }
        # 回复的xml
        self.f_xml = {
            text : self._create_reply_xml_text,
            image : self._create_reply_xml_img,
        }
        # 收到的消息类型
        self.type = self.xml_recv.find(MsgType).text

        self.face_api = Face()
        pass

    def g(self,param):
        return  self.xml_recv.find(param).text


    def reply(self):
        # 根据Type选择处理函数
        xdata = self.f_do.get(self.type)(self.xml_recv)
        print "Reply %s "% xdata
        return xdata

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
    def _do_text_reply(self,data):
        key = data.find(Content).text
        # 通过图灵得到回复
        context = self._get_tuling_ans(key)
        #  调用_create_reply_xml_text 生成文本回复模版
        t = self.f_xml.get(self.type)()
        # 格式化消息
        t = t % context
        return  t


    def _do_image_reply(self,data):
        mediaid = data.find(MediaId).text
        picurl = data.find(PicUrl).text
        self.face_api.checkface(picurl)
        # 调用_create_reply_xml_img
        t = self.f_xml.get(self.type)()

        t = t % mediaid
        return t

    def _create_reply_xml_text(self):
        jdata = { 'xml':{
            ToUserName:self.g(FromUserName),
            FromUserName:self.g(ToUserName),
            CreateTime:str(int(time.time())),
            MsgType: text,
            Content:"<![CDATA[%s]]>",
        },
        }
        rdata = x2j().json2xml(jdata)
        rdata =rdata.replace('&lt;','<')
        rdata = rdata.replace('&gt;','>')
        return rdata

    def _create_reply_xml_img(self):
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
        rdata = x2j().json2xml(jdata)
        rdata =rdata.replace('&lt;','<')
        rdata = rdata.replace('&gt;','>')
        return rdata

    def _get_image(self,url,name):
        f = requests.get(url)
        file = open(name,"w")
        file.write(f.content)
        file.flush()
        file.close()
        return f.content