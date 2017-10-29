# ifttt_ros

iftttのWebFookをROSに渡す簡単なサンプル

現状セキリティの考慮ゼロ

使い方
------

$ source /opt/ros/kinetic/setup.bash
$ ./simple_server.py

してIFTTTのwebhookで

URL: http://hogehoge:5000/from_ifttt

Method: POST

Content Type: appllixation x-www-for-urlencode

Body: Sentence=TextField

でOK