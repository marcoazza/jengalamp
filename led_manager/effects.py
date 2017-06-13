import unicornhat as unicorn
import styles
from multiprocessing import Process, Pipe
import signal
import os


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.9)
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
                newdata = None
                if current_style:
                    r, g, b = color
                    try:
                        current_instance = current_style(unicorn, height, width, int(r), int(g), int(b))
                        print('set new instance with color {}-{}-{}'.format(r, g, b))
                    except:
                        current_instance = None
            if current_instance:
                current_instance.render()
        except KeyboardInterrupt:
            print('loading new data..')
            newdata = conn.recv()
    print('closing connection....')
    conn.close()


def led_manager(conn):
    parent_conn, child_conn = Pipe()
    p = Process(target=effect_daemon, args=(child_conn,))
    p.start()
    while True:
        try:
            data = conn.recv()
            os.kill(p.pid, signal.SIGINT)
            parent_conn.send(data)
        except KeyboardInterrupt:
            pass
    unicorn.off()
    parent_conn.close()
