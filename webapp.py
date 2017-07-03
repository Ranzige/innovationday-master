# -*- coding:utf-8 -*-
import port as port
from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import rpi.sensortag
import time
import json
import sys
import a
import os

reload(sys)

sys.setdefaultencoding('utf-8')



app = Flask(__name__)
port = int(os.getenv('PORT', 8080))



@app.route('/', methods=['GET','POST'])



def func():
    res = {
        'data': {
            'data1': [],
            'data2': []
        }
    }

    callback = request.values.get('callback')
    return ''.join([
        callback,
        '(',
        json.dumps(res),
        ');'
    ])

def start():
    if request.method == 'GET':
        return render_template('index.html')




if __name__ =='__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=port)


