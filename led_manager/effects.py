import unicornhat as unicorn
import styles
from multiprocessing import Process, Pipe
import threading
import signal
import os


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.9)
width, height = unicorn.get_shape()


class Effect(threading.Thread):

    def __init__(self, data):
        threading.Thread.__init__(self)
        self.shutdown_flag = threading.Event()

    def run(self):
        print('Thread #%s started' % self.ident)
        style = self.data.get('style')
        color = self.data.get('color')
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
            print('closing thread {}'.format(self.ident))


def effect_daemon(conn, data):
    return


def led_manager(conn):
    # parent_conn, child_conn = Pipe()
    # p = Process(target=effect_daemon, args=(child_conn,))
    # p.start()
    # t = Thread(target=effect_daemon)
    t = None
    while True:
        try:
            data = conn.recv()
            if t:
                print('Waiting for thread to be joined')
                t.shutdown_flag.set()
                t.join()
            else:
                print('Creating new thread')
                t = Effect(args=(data,))
                t.start()
            # parent_conn.send(data)
        except KeyboardInterrupt:
            pass
    unicorn.off()
    # parent_conn.close()
