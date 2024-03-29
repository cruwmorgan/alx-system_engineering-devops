#!/bin/sh

PATH=/sbin:/usr/sbin:/bin:/usr/bin
PIDFILE=/var/run/haproxy.pid
CONFIG=/etc/haproxy/haproxy.cfg
HAPROXY=/usr/local/sbin/haproxy
EXTRAOPTS=
ENABLED=0

test -x $HAPROXY || exit 0

if [ -e /etc/default/haproxy ]; then
        . /etc/default/haproxy
fi

test -f "$CONFIG" || exit 0
test "$ENABLED" != "0" || exit 0

[ -f /etc/default/rcS ] && . /etc/default/rcS
. /lib/lsb/init-functions

clean()
{
    if [ -e "$tmp" ];then
        rm -f "$tmp"
    fi
}

trap clean EXIT

check_haproxy_config()
{
        $HAPROXY -c -f "$CONFIG" >/dev/null
        if [ $? -eq 1 ]; then
                log_end_msg 1
                exit 1
        fi
}

haproxy_start()
{
        check_haproxy_config

        start-stop-daemon --quiet --oknodo --start --pidfile "$PIDFILE" \
                --exec $HAPROXY -- -f "$CONFIG" -D -p "$PIDFILE" \
                $EXTRAOPTS || return 2
        return 0
}

haproxy_stop()
{
        tmp=$(tempfile -s .haproxy.init)

        if [ ! -f $PIDFILE ] ; then
                # This is a success according to LSB
                return 0
        fi

        ret=0
        for pid in $(cat $PIDFILE); do
                echo $pid > "$tmp"
                start-stop-daemon --quiet --oknodo --stop \
                        --retry 5 --pidfile "$tmp" --exec $HAPROXY || ret=$?
        done

        [ $ret -eq 0 ] && rm -f $PIDFILE

        return $ret
}

haproxy_reload()
{
        check_haproxy_config

        $HAPROXY -f "$CONFIG" -p $PIDFILE -D $EXTRAOPTS -sf $(cat $PIDFILE) \
                || return 2
        return 0
}

haproxy_status()
{
        if [ ! -f $PIDFILE ] ; then
                # program not running
                return 3
        fi

        for pid in $(cat $PIDFILE) ; do
                if ! ps --no-headers p "$pid" | grep haproxy > /dev/null ; then
                        # program running, bogus pidfile
                        return 1
                fi
        done

        return 0
}


case "$1" in
start)
        log_daemon_msg "Starting haproxy" "haproxy"
        haproxy_start
        ret=$?
        case "$ret" in
        0)
                log_end_msg 0
                ;;
        1)
                log_end_msg 1
                echo "pid file '$PIDFILE' found, haproxy not started."
                ;;
        2)
                log_end_msg 1
                ;;
        esac
        exit $ret
        ;;
stop)
        log_daemon_msg "Stopping haproxy" "haproxy"
        haproxy_stop
        ret=$?
        case "$ret" in
        0|1)
                log_end_msg 0
                ;;
        2)
                log_end_msg 1
                ;;
        esac
        exit $ret
        ;;
reload|force-reload)
        log_daemon_msg "Reloading haproxy" "haproxy"
        haproxy_reload
        ret=$?
        case "$ret" in
        0|1)
                log_end_msg 0
                ;;
        2)
                log_end_msg 1
                ;;
        esac
        exit $ret
        ;;
restart)
        log_daemon_msg "Restarting haproxy" "haproxy"
        haproxy_stop
        haproxy_start
        ret=$?
        case "$ret" in
        0)
                log_end_msg 0
                ;;
        1)
                log_end_msg 1
                ;;
        2)
                log_end_msg 1
                ;;
        esac
        exit $ret
        ;;
status)
        haproxy_status
        ret=$?
        case "$ret" in
        0)
                echo "haproxy is running."
                ;;
        1)
                echo "haproxy dead, but $PIDFILE exists."
                ;;
        *)
                echo "haproxy not running."
                ;;
        esac
        exit $ret
        ;;
*)
        echo "Usage: /etc/init.d/haproxy {start|stop|reload|restart|status}"
        exit 2
        ;;
esac

:
