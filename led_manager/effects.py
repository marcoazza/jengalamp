import unicornhat as unicorn
import styles
import threading


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.9)
width, height = unicorn.get_shape()


class Effect(threading.Thread):

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, args=(), kwargs=kwargs)
        self.data = kwargs.get('data')
        self.shutdown_flag = threading.Event()

    def run(self):
        style = self.data.get('style')
        color = self.data.get('color')
        print('data change for board style:{}  color: {}'.format(style, color))
        current_style = styles.available.get(style)
        if current_style:
            r, g, b = color
            try:
                current_instance = current_style(unicorn, height, width, int(r), int(g), int(b))
                print('set new instance with color {}-{}-{}'.format(r, g, b))
            except:
                current_instance = None
        if current_instance:
            while not self.shutdown_flag.is_set():
                try:
                    current_instance.render()
                except KeyboardInterrupt:
                    print('loading new data..')
            print('closing thread {}'.format(self.ident))
        return


def led_manager(conn):
    t = None
    while True:
        try:
            data = conn.recv()
            if t:
                print('Waiting for thread to be joined')
                t.shutdown_flag.set()
                t.join()
                t = None
            print('Creating new thread')
            t = Effect(data=data)
            t.start()
        except KeyboardInterrupt:
            pass
    unicorn.off()
