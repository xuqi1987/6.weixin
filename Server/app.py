# -*- coding:utf8 -*-
import time
from flask import Flask,request, make_response,render_template,request,flash,url_for
from wechatAPI import *
from face import Face
import time
import os
from facepp import File
face_api = Face()
app = Flask(__name__)
app.secret_key = 'some_secret'
@app.route('/', methods = ['GET', 'POST'] )
def wechat():
    resp = make_response('')
    api = WechatAPI()
    try:
        if request.method == 'GET':
            # 用于接入微信
            resp = make_response(api.wechat_auth(request))
        else:
            # 取的access token
            # api.get_token();

            # 被动回复用户消息
            replydata = api.recv_reply(request.data)

            resp = make_response(replydata)
            resp.content_type = 'application/xml'
    except Exception as e:
        resp =  make_response(e.message)
    finally:
        return resp

@app.route('/addface', methods = ['Get','POST'])
def addface():
    if request.method == 'POST':
        imagefile  = request.files['imagefile']

        name = request.form['name']
        if len(name)==0:
            flash(u"请填写称呼")
            pass
        else:
            path = os.getcwd() +"/img/" + imagefile.filename
            imagefile.save(path)
            face_api.add_person(name,img=File(path=path))
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug=True)