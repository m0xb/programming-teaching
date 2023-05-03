import math
import random
import tkinter as tk
from dataclasses import dataclass

import tk_base

@dataclass
class AABB:
    x1: int
    y1: int
    x2: int
    y2: int

@dataclass
class Rectangle:
    x: int
    y: int
    width: int
    height: int
    draw_options: dict

    def get_bounds(self):
        return AABB(self.x, self.y, self.x + self.width, self.y + self.height)

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, **self.draw_options)


class CollisionUI:

    TICK_INTERVAL = 100

    def __init__(self):
        self.app = None
        # the list of objects we'll draw
        self.objects = []
        # the currently active selection box the user is drawing
        self.selection_box = None
        # counter that keeps track of how long the app has been running (since last reset)
        self.time = 0

    def init_ui(self, app):
        app.canvas.bind('<Motion>', self.on_mouse_move)
        app.canvas.bind('<Button-1>', self.on_click)
        app.canvas.bind('<ButtonPress-1>', self.on_press)
        app.canvas.bind('<ButtonRelease-1>', self.on_release)
        app.main_window.after(self.TICK_INTERVAL, self.tick, app)
        """
        Two ways to do this:
        1: ```main_window.after(self.TICK_INTERVAL, lambda: self.tick(app))```
        2: ```app.main_window.after(self.TICK_INTERVAL, self.tick, app)```
        """
        self.app = app
        self.reset(app)

    def tick(self, app):
        self.app.main_window.after(self.TICK_INTERVAL, self.tick, app)
        # print("Tick at {}".format(self.time))

        self.time += self.TICK_INTERVAL
        for object in self.objects:
            pass

        self.draw()

    def check_collisions(self, collide_against_object):
        """
        Checks to see if any of the objects on the canvas collide with (or are entirely contained within)
        the object passed as a parameter
        :param collide_against_object:
        :return:
        """
        a = collide_against_object.get_bounds()
        for object in self.objects:
            if object == collide_against_object:
                # No point to testing collision on the object against itself
                continue
            #print("Check for collision between {} and {}".format(collide_against_object, object))
            b = object.get_bounds()
            collide_x = False
            collide_y = False
            collide = False
            # if a.x2 > b.x1 or b.x2 >= a.x1:
            if a.x2 > b.x1 and a.y2 > b.y1:
                # At this point, we know that for both the x- and y-axis,
                # the object A's bounds exceed the starting point of B's
                if b.x1 > a.x1 and b.y1 > a.y1:
                    collide = True

            if collide:
                object.draw_options['fill'] = '#FF0000'
            else:
                object.draw_options['fill'] = ''
            #break

    def on_mouse_move(self, event):
        if self.selection_box:
            self.selection_box.width = event.x - self.selection_box.x
            self.selection_box.height = event.y - self.selection_box.y
            self.check_collisions(self.selection_box)
            self.draw()

    def on_click(self, event):
        print("Click: {}, {}".format(event.x, event.y))
        self.draw()

    def on_press(self, event):
        print("Press: {}, {}".format(event.x, event.y))
        self.selection_box = Rectangle(event.x, event.y, 0, 0, dict(outline="#FF0000"))
        self.objects.append(self.selection_box)
        self.draw()

    def on_release(self, event):
        print("Release: {}, {}".format(event.x, event.y))
        self.objects.remove(self.selection_box)
        self.selection_box = None
        self.draw()

    def populate(self, app):
        # self.objects.append(Rectangle(300, 20, 100, 200, dict(outline="#FFFFFF")))
        # self.objects.append(Rectangle(50, 500, 30, 30, dict(outline="#FFFFFF")))
        for i in range(10):
            self.objects.append(Rectangle(i * 100, i * 80, 30, 30, dict(outline="#FFFFFF")))
        for i in range(10):
            self.objects.append(Rectangle(random.randint(5, 1100), random.randint(5, 800), 30, 30, dict(outline="#FFFFFF")))
        self.draw()

    def reset(self, app):
        self.objects = []
        self.time = 0
        if self.app:
            self.draw()

    def draw(self):
        self.app.canvas.delete("all")

        for object in self.objects:
            object.draw(self.app.canvas)

        self.app.canvas.create_text(5, 795, anchor=tk.SW, fill="#FFFFFF", text=__file__+" | t = {}s".format(self.time / 1000))


ui = CollisionUI()
tk_base.TkBaseApp({
        "Populate": ui.populate,
        "Reset": ui.reset
    }, ui.init_ui
).run()
