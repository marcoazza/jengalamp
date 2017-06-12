import socketio
import eventlet
from flask import Flask
import os
from multiprocessing import Process, Pipe
import effects
import signal

sio = socketio.Server()
app = Flask(__name__)

parent_conn, child_conn = Pipe()
p = Process(target=effects.led_manager, args=(child_conn,))


@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)


@sio.on('change')
def message(sid, data):
    print("message ", data)
    if parent_conn:
        parent_conn.send(data)


@sio.on('command')
def command(sid, data):
    if data.get('command') == 'off':
        os.kill(p.pid, signal.SIGINT)
        parent_conn = None
    elif data.get('command') == 'on':
        parent_conn, child_conn = Pipe()
        p = Process(target=effects.led_manager, args=(child_conn,))
        p.start()


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    try:
        host = os.environ.get('LEDSERVICE_HOST')
        port = os.environ.get('LEDSERVICE_PORT')
        p.start()
        app = socketio.Middleware(sio, app)
        eventlet.wsgi.server(eventlet.listen((host, int(port))), app)
    except KeyError as e:
        print('Failling start Service reason: {}'.format(e))
