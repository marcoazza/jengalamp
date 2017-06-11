import unicornhat as unicorn
import styles
from multiprocessing import Process, Pipe
import signal
import os


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width, height = unicorn.get_shape()


def effect_daemon(conn):
    newdata = None
    current_instance = None
    while True:
        try:
            if newdata:
                style = newdata.get('style')
                color = newdata.get('color')
                print('data change for board style:{}   color: {}'.format(style, color))
                current_style = styles.available.get(style)
                if current_style:
                    r, g, b = color
                    current_instance = current_style(unicorn, height, width, r, g, b)
                    newdata = None
            if current_instance:
                current_instance.render()
        except KeyboardInterrupt:
            print('loading new data..')
            newdata = conn.recv()
    conn.close()


def led_manager(conn):
    parent_conn, child_conn = Pipe()
    p = Process(target=effect_daemon, args=(child_conn,))
    p.start()
    while True:
        try:
            data = conn.recv()
            print('board received ===> ', data)
            os.kill(p.pid, signal.SIGINT)
            parent_conn.send(data)
        except KeyboardInterrupt:
            pass
    parent_conn.close()
