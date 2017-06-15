import unicornhat as unicorn
import styles
from multiprocessing import Process, Pipe
from threading import Thread
import signal
import os


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.9)
width, height = unicorn.get_shape()


def effect_daemon(conn, data):
    style = data.get('style')
    color = data.get('color')
    print('data change for board style:{}   color: {}'.format(style, color))
    current_style = styles.available.get(style)
    if current_style:
        r, g, b = color
        try:
            current_instance = current_style(unicorn, height, width, int(r), int(g), int(b))
            print('set new instance with color {}-{}-{}'.format(r, g, b))
        except:
            current_instance = None
    if current_instance:
        while True:
            try:
                current_instance.render()
            except KeyboardInterrupt:
                print('loading new data..')
        print('closing thread....')
    return


def led_manager(conn):
    # parent_conn, child_conn = Pipe()
    # p = Process(target=effect_daemon, args=(child_conn,))
    # p.start()
    t = Thread(target=effect_daemon)
    while True:
        try:
            data = conn.recv()
            if t:
                print('Waiting for thread to be joined')
                os.kill(t.pid, signal.SIGINT, args=(data,))
                t.join()
            else:
                print('Creating new thread')
                t = Thread(target=effect_daemon)
                t.start()
            # parent_conn.send(data)
        except KeyboardInterrupt:
            pass
    unicorn.off()
    # parent_conn.close()
