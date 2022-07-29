# -*- coding: utf-8 -*-

import json
import datetime
import time
import gevent
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from uuid import UUID, uuid4
from flask import Flask, request, render_template
from flask_sockets import Sockets
from flask_sock import Sock

app = Flask(__name__)
app.config.from_object(__name__)

sock = Sock(app)
sock_list = []

@sock.route('/echo')
def echo(sock):
    sock_list.append(sock)
    print(sock_list)
    while True:
        print("1")
        message = sock.receive()
        print("2")
        if message is None:
            break
        remove = []
        for sockObj in sock_list:
            print("4")
            try:
                print("3")
                datetime_now = datetime.datetime.now()
                data = {
                    'time': str(datetime_now),
                    'message': message
                }
                print(data)
                sockObj.send(json.dumps(data))
            except Exception:
                remove.append(sockObj)
            for sockObj in remove:
                sock_list.remove(sockObj)

#list_of_clients = []

@app.route('/')
def index():
    return render_template('tmp.html')

"""
@app.route('/pipe')
def pipe():
    print('hello')
    ws_list = set()
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        ws_list.add(ws)
        #print(ws)
        while True:
            time.sleep(1)
            message = ws.receive()
            if message is None:
                break
            remove = set()
            for s in ws_list:
                try:
                    datetime_now = datetime.datetime.now()
                    data = {
                        'time': str(datetime_now),
                        'message': message
                    }
                    s.send(json.dumps(data))
                    #ws.send(json.dumps(data))
                except Exception:
                    remove.add(s)
                for s in remove:
                    ws_list.remove(s)

            print(message)
            print(data)
    return
"""

if __name__ == '__main__':
    app.run(port=80)
    """
    host = 'localhost'
    port = 8080
    host_port = (host, port)

    server = WSGIServer(
        host_port,
        app,
        handler_class=WebSocketHandler
    )
    server.serve_forever()
    """