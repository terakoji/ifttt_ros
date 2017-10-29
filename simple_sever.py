#!/usr/bin/env python
# vim:fileencoding=utf-8

import os
import sys
from flask import Flask
from flask import request
import rospy
from std_msgs.msg import String

app = Flask(__name__)
rospy.init_node('rest_node', disable_signals=True)
pub = rospy.Publisher('sentence', String, queue_size=1)

@app.route("/from_ifttt")
def debug():
    print('get method')
    return 'OK'

@app.route("/from_ifttt", methods=['POST'])
def send_ros():
    sentence = request.form['sentence']
    str = String(sentence)
    pub.publish(str)
    return sentence + "is Published \n"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
