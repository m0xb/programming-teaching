import math
import random
import tkinter as tk
from dataclasses import dataclass

import tk_base

class Tickable:
    def tick(self):
        pass

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

    def normalize(self):
        if self.width < 0:
            self.x += self.width
            self.width = -self.width
        if self.height < 0:
            self.y += self.height
            self.height = -self.height

    def get_bounds(self):
        return AABB(self.x, self.y, self.x + self.width, self.y + self.height)

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, **self.draw_options)


class MovingRect(Tickable):
    def __init__(self, rect: Rectangle, object_container):
        self.rect = rect
        self.object_container = object_container
        self.draw_options = rect.draw_options

    def draw(self, canvas):
        self.rect.draw(canvas)

    def get_bounds(self):
        return self.rect.get_bounds()

    def tick(self):
        self.rect.x += 3


class ObjectContainer:
    def __init__(self):
        self.objects = []

    def reset(self):
        self.objects = []

    def highlight_collisions(self, collide_against_object):
        collisions = self.check_collisions(collide_against_object)
        for object in self.objects:
            object.draw_options['fill'] = ''
        for object in collisions:
            object.draw_options['fill'] = '#FF0000'

    def check_collisions(self, collide_against_object):
        """
        Checks to see if any of the objects on the canvas collide with (or are entirely contained within)
        the object passed as a parameter
        :param collide_against_object:
        :return: A list of objects that collide with the given object
        """
        result = []
        a = collide_against_object.get_bounds()
        for object in self.objects:
            if object == collide_against_object:
                # No point to testing collision on the object against itself
                continue
            #print("Check for collision between {} and {}".format(collide_against_object, object))
            b = object.get_bounds()
            collide = False
            # if a.x2 > b.x1 or b.x2 >= a.x1:
            if a.x2 > b.x1 and a.y2 > b.y1:
                # At this point, we know that for both the x- and y-axis,
                # the object A's bounds exceed the starting point of B's
                if b.x2 > a.x1 and b.y2 > a.y1:
                    collide = True

            if collide:
                result.append(object)
        return result


class Tool:
    def on_press(self, event):
        return False

    def on_release(self, event):
        return False

    def on_mouse_move(self, event):
        return False


class SpawnTool(Tool):
    def __init__(self, object_container: ObjectContainer):
        self.object_container = object_container

    def on_release(self, event):
        print("Click (SpawnTool): {}, {}".format(event.x, event.y))
        self.object_container.objects.append(MovingRect(Rectangle(event.x, event.y, 10, 10, dict(fill="#FF0")), self.object_container))
        return True


class SelectTool(Tool):
    def __init__(self, object_container: ObjectContainer):
        self.object_container = object_container
        # the currently active selection box the user is drawing
        self.selection_box = None
        self.selection_start_pos = None

    def on_press(self, event):
        print("Press (SelectTool): {}, {}".format(event.x, event.y))
        self.selection_start_pos = (event.x, event.y)
        self.selection_box = Rectangle(event.x, event.y, 0, 0, dict(outline="#FFFFFF"))
        self.object_container.objects.append(self.selection_box)
        return True

    def on_release(self, event):
        print("Release (SelectTool): {}, {}".format(event.x, event.y))
        self.object_container.objects.remove(self.selection_box)
        self.selection_box = None
        self.selection_start_pos = None
        return True

    def on_mouse_move(self, event):
        if self.selection_start_pos:
            self.selection_box.x = self.selection_start_pos[0]
            self.selection_box.y = self.selection_start_pos[1]
            self.selection_box.width = event.x - self.selection_start_pos[0]
            self.selection_box.height = event.y - self.selection_start_pos[1]
            self.selection_box.normalize()
            self.object_container.highlight_collisions(self.selection_box)
            return True
        return False


class CollisionUI:

    TICK_INTERVAL = 100

    def __init__(self):
        self.app = None
        # The objects we'll simulate/draw
        self.object_container = ObjectContainer()

        # Tools
        self.select_tool = SelectTool(self.object_container)
        self.spawn_tool = SpawnTool(self.object_container)
        self.active_tool = self.select_tool

        # counter that keeps track of how long the app has been running (since last reset)
        self.time = 0

    def init_ui(self, app):
        app.canvas.bind('<Motion>', self.on_mouse_move)
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
        for object in self.object_container.objects:
            if isinstance(object, Tickable):
                object.tick()

        self.draw()

    def on_mouse_move(self, event):
        if self.active_tool.on_mouse_move(event):
            self.draw()

    def on_press(self, event):
        if self.active_tool.on_press(event):
            self.draw()

    def on_release(self, event):
        self.active_tool.on_release(event)
        self.draw()

    def set_active_tool(self, active_tool):
        print("Setting active tool to {}".format(active_tool))
        self.active_tool = active_tool

    def set_select_mode(self, app):
        self.set_active_tool(self.select_tool)

    def set_spawn_mode(self, app):
        self.set_active_tool(self.spawn_tool)

    def populate(self, app):
        # self.objects.append(Rectangle(300, 20, 100, 200, dict(outline="#FFFFFF")))
        # self.objects.append(Rectangle(50, 500, 30, 30, dict(outline="#FFFFFF")))
        for i in range(10):
            self.object_container.objects.append(Rectangle(5 + i * 100, 5 + i * 80, 30, 30, dict(outline="#FFFFFF")))
        for i in range(10):
            self.object_container.objects.append(Rectangle(random.randint(5, 1100), random.randint(5, 800), 30, 30, dict(outline="#FFFFFF")))
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


ui = CollisionUI()
tk_base.TkBaseApp({
        "Populate": ui.populate,
        "Select Mode": ui.set_select_mode,
        "Spawn Mode": ui.set_spawn_mode,
        "Reset": ui.reset
    }, ui.init_ui
).run()
