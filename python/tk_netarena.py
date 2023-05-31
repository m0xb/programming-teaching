import select
import socket
import sys
import tkinter as tk
from dataclasses import dataclass

import tk_base


@dataclass
class Rectangle:
    x: int
    y: int
    width: int
    height: int
    draw_options: dict

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, **self.draw_options)


class ObjectContainer:
    def __init__(self):
        self.objects = []

    def reset(self):
        self.objects = []


class NetArenaUI:

    TICK_INTERVAL = 100

    def __init__(self, args):
        self.args = args

        self.app = None
        # The objects we'll simulate/draw
        self.object_container = ObjectContainer()

        # counter that keeps track of how long the app has been running (since last reset)
        self.time = 0

    def init_ui(self, app):
        host = self.args[1]
        port = int(self.args[2])
        self.start_server(host, port)

        app.main_window.after(self.TICK_INTERVAL, self.tick, app)
        self.app = app
        self.reset(app)

    def network_tick(self):
        # print("Network tick...")
        # setblocking(False) causes:
        #   BlockingIOError: [Errno 35] Resource temporarily unavailable
        # self.server_socket.setblocking(False)
        # conn, addr = self.server_socket.accept()
        # data = conn.recv(1024)

        readable, writable, errors = select.select([self.server_socket] + self.clients, [], [], 0) # timeout=0 to avoid blocking
        if readable:
            for s in readable:
                if s is self.server_socket:
                    # handle new connections (from server_socket)
                    conn, addr = s.accept()
                    self.clients.append(conn)
                    print(f"Got a new client: {addr}")
                else:
                    # handle data from a client connection
                    data = s.recv(2048)
                    if data:
                        self.process_client_command(data)

    def process_client_command(self, data: bytes):
        try:
            command = data.decode('ascii')
            x, y, w, h = map(int, command.split(' '))  # enter command like: 1 1 20 20
            self.object_container.objects.append(Rectangle(x, y, w, h, dict(fill="#FF0000")))
        except Exception as e:
            print(f"Bad command {data}")
            print(e)

    def start_server(self, host, port):
        print(f"Start server {host}:{port}")

        self.clients = []  # list of sockets for clients which are connected
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()

    def tick(self, app):
        self.network_tick()

        self.app.main_window.after(self.TICK_INTERVAL, self.tick, app)

        self.draw()

    def reset(self, app):
        self.object_container.reset()
        self.time = 0
        if self.app:
            self.draw()

    def draw(self):
        self.app.canvas.delete("all")

        for object in self.object_container.objects:
            object.draw(self.app.canvas)

        self.app.canvas.create_text(5, 795, anchor=tk.SW, fill="#FFFFFF", text=__file__+" | t = {}s".format(self.time / 1000))


ui = NetArenaUI(sys.argv)
tk_base.TkBaseApp({
        "Reset": ui.reset
    }, ui.init_ui
).run()
