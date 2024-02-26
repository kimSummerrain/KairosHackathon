#!/bin/sh
export LANG=ko_KR.UTF-8
export LC_ALL=ko_KR.UTF-8
service ssh start
service mysql start
cd /usr/local/tomcat9
./bin/catalina.sh run &
while :; do sleep 1000000; done
