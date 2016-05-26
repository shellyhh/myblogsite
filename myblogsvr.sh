#!/bin/sh
#server script 
case $1 in
start)
	echo "server start"
	echo $0
	sudo /etc/init.d/nginx start
	uwsgi --ini ./myblogsite/uwsgi.ini
	;;
stop)
	echo "server stop"
	killall -9 nginx
	killall -9 uwsgi
	;;
restart)
	echo "server restart"
	$0 stop
	$0 start
	;;
*)
	echo "nothing"
	;;
esac
exit 0
