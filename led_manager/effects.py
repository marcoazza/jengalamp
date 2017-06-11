import unicornhat as unicorn
import styles
from multiprocessing import Process, Pipe

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width, height = unicorn.get_shape()


def effect_daemon(conn):
    initialized = False
    while True:
        try:
            data = conn.recv()
            style = data.get('style')
            current_style = styles.available.get(style)
            if not initialized and current_style:
                print('Initialize {}'.format(style))
                current_instance = current_style(unicorn, height, width)
                initialized = True
            current_instance.render()
        except KeyboardInterrupt:
            initialized = False
    conn.close()


def led_manager(conn):
    parent_conn, child_conn = Pipe()
    p = Process(target=effect_daemon, args=(child_conn,))
    p.start()
    while True:
        try:
            data = conn.recv()
            print('board received ===> ', data)
            parent_conn.send(data)
        except KeyboardInterrupt:
            pass
    parent_conn.close()
