# 6.weixin

**参考：**

[http://blog.csdn.net/linhan8/article/details/8746110]()

要通过微信配置，必须先服务器端配置好


### 第一步 服务器端配置

服务器接入指南：

[http://mp.weixin.qq.com/wiki/8/f9a0b8382e0b77d87b3bcc1ce6fbc104.html]()

开发者提交信息后，微信服务器将发送GET请求到填写的服务器地址URL上，GET请求携带四个参数：

参数	|	描述
------------- | -------------
signature	| 微信加密签名，signature结合了开发者填写的token参数和请求中的timestamp参数、nonce参数。
timestamp	 | 时间戳
nonce	| 随机数
echostr	| 随机字符串


开发者通过检验signature对请求进行校验（下面有校验方式）。若确认此次GET请求来自微信服务器，请原样返回echostr参数内容，则接入生效，成为开发者成功，否则接入失败。

```
加密/校验流程如下：
1. 将token、timestamp、nonce三个参数进行字典序排序
2. 将三个参数字符串拼接成一个字符串进行sha1加密
3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信

```

```
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
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp, nonce, token]
        # 1. 将token、timestamp、nonce三个参数进行字典序排序
        s.sort()
        # 2. 将三个参数字符串拼接成一个字符串进行sha1加密
        s = ''.join(s)
        # 3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
        key = hashlib.sha1(s).hexdigest()
        if (key == signature):
            return make_response(echostr)
```

**遇到小问题**

因为域名没有备案，所以无法通过域名设置，只能设置ip。

