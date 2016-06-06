# -*- coding:utf8 -*-
import time
from flask import Flask,request, make_response,render_template,request,flash,url_for
from face import Face
import time
import os
from facepp import File
face_api = Face()
app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/login.html', methods = ['GET'] )
def login():
    return render_template("login.html")

@app.route('/calendar.html', methods = ['GET'] )
def calendar():
    return render_template("calendar.html")

@app.route('/file-manager.html', methods = ['GET'] )
def file_manager():
    return render_template("file-manager.html")

@app.route('/form.html', methods = ['GET'] )
def form():
    return render_template("form.html")

@app.route('/gallery.html', methods = ['GET'] )
def gallery():
    return render_template("gallery.html")

@app.route('/messages.html', methods = ['GET'] )
def messages():
    return render_template("messages.html")


@app.route('/', methods = ['GET'] )
@app.route('/index.html', methods = ['GET'] )
def index():
    return render_template("index.html")


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
            ret = face_api.add_person(name,img=File(path=path))
            if ret:
                flash(u"添加成功")
            else:
                flash(u"添加失败")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)

