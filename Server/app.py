# -*- coding:utf8 -*-
import time
from flask import Flask,request, make_response
from wechatAPI import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'] )
def wechat():
    resp = ''
    api = WechatAPI()
    try:
        if request.method == 'GET':
            # 用于接入微信
            resp = api.wechat_auth(request)
        else:
            # 取的access token
            api.get_token();
    except Exception as e:
        resp =  e.message
    finally:
        return make_response(resp)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)