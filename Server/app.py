# -*- coding:utf8 -*-
import time
from flask import Flask,request, make_response
import hashlib

app = Flask(__name__)

@app.route('/wechat', methods = ['GET', 'POST'] )
def wechat_auth():

    if request.method == 'GET':
        token = 'xq123456' # your token
        query = request.args  # GET 方法附上的参数
        signature = query.get('signature', '')  # 微信加密签名
        timestamp = query.get('timestamp', '')  # 时间戳
        nonce = query.get('nonce', '')  # 随机数
        echostr = query.get('echostr', '') # 随机字符串
        s = [timestamp, nonce, token]
        # 1. 将token、timestamp、nonce三个参数进行字典序排序
        s.sort()
        # 2. 将三个参数字符串拼接成一个字符串进行sha1加密
        s = ''.join(s)
        # 3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
        key = hashlib.sha1(s).hexdigest()
        if (key == signature):
            return make_response(echostr)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)