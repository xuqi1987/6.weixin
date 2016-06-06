# -*- coding:utf8 -*-
import os

def gethtmlfile():
    rootpath = "templates"
    for (root, dirs, files) in os.walk(rootpath):
        for file in files:
            path =  root + os.sep+file
            filetype =  file.split(".")[-1]
            if filetype == "html":
                yield os.getcwd() + os.sep + path

def getstaticfile():
    staticlist = {}
    rootpath = "static"
    for (root, dirs, files) in os.walk(rootpath):
        for file in files:
            path =  root  +os.sep+ file
            #print path
            path = path.replace(rootpath,"")[1:]
            abpath = path.split(os.sep)[0:-1]
            abpath = os.sep.join(abpath)
            staticlist[path] = [abpath,file]
    return staticlist

def replace_static_file(text,staticfiles):

    for key in staticfiles.keys():
        #print key
        text = text.replace(key,"{{url_for('static',filename='" + staticfiles[key][0] +os.sep +staticfiles[key][1] + "')}}")

    return text


staticlist = getstaticfile()
htmllist = gethtmlfile()

for file in htmllist:
    file_object = open(file,'r')
    #print file
    newfile = os.sep.join(file.split(os.sep)[0:-1]) + os.sep + os.sep.join(file.split(os.sep)[-1].split('.')[0:-1]) + "_new.html"
    fileHandle = open (newfile ,"a")
    try:
        all_the_text = file_object.read()
        all_the_text = replace_static_file(all_the_text,staticlist)
        fileHandle.write(all_the_text)
        print all_the_text

    except Exception,X:
        print X
    finally:

        file_object.close()
        fileHandle.close()
        os.remove(file)
        os.rename(newfile,file)


