import random
import tkinter as tk
from dataclasses import dataclass

import tk_base


@dataclass
class DrawOptions:
    line_colors: list
    subtree_bounds: bool = False
    text_color_fn: any = None  # apparently if I don't add a type annotation here, dataclasses doesn't see it as an attribute?
    line_color_fn: any = None


class TreeNode:

    NODE_SIZE = 40
    FONT_SIZE = 20
    H_PAD = 5
    V_PAD = 5

    def __init__(self, value, left=None, right=None):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.value = value
        self.count = 1
        self.left = left
        self.right = right

    def clone(self):
        # call clone() on the left subtree to recursively clone it, if it is not none
        new_left = self.left.clone() if self.left else None
        # call clone() on the right subtree to recursively clone it, if it is not none
        new_right = self.right.clone() if self.right else None
        # create a new TreeNode which is the clone of self, and pass the left + right clones into it
        new_self = TreeNode(self.value, new_left, new_right)
        # and also copy the `count` variable over
        new_self.count = self.count
        # ... no need to clone x/y/width/height since they are recomputed in draw()
        # return the recursively cloned self
        return new_self

    def draw(self, canvas, opts: DrawOptions):
        self.calculate_size()
        self.calculate_child_positions()
        self._draw(canvas, opts)

    def calculate_child_positions(self):
        left_offset = self.left.width + self.H_PAD if self.left else self.NODE_SIZE + self.H_PAD
        if self.left:
            self.left.x = self.x
            self.left.y = self.y + self.NODE_SIZE + self.V_PAD
            self.left.calculate_child_positions()
        if self.right:
            self.right.x = self.x + left_offset
            self.right.y = self.y + self.NODE_SIZE + self.V_PAD
            self.right.calculate_child_positions()

    def calculate_size(self):
        if not self.left and not self.right:
            self.width = self.NODE_SIZE
            self.height = self.NODE_SIZE
        else:
            max_width = 0
            max_height = 0
            if self.left:
                self.left.calculate_size()
                max_width = self.left.width
                max_height = self.left.height
            if self.right:
                self.right.calculate_size()
                max_width = max(max_width, self.right.width)
                max_height = max(max_height, self.right.height)
            # balance the size
            # self.width = max_width * 2 + self.H_PAD
            # minimal size -- kinda broken
            self.width = \
                (self.left.width if self.left else self.NODE_SIZE) \
                + (self.right.width if self.right else self.NODE_SIZE) \
                + (self.H_PAD if self.left or self.right else 0)
            self.height = self.NODE_SIZE + max_height + self.V_PAD

    def _draw(self, canvas, opts: DrawOptions):
        half_width = self.width / 2
        half_size = self.NODE_SIZE / 2

        default_line_color = opts.line_colors[(self.tree_height() - 1) % len(opts.line_colors)]

        text_color = opts.text_color_fn(self) if opts.text_color_fn else '#FF0000'
        if opts.line_color_fn:
            node_line_color = opts.line_color_fn(self, 'node') or default_line_color
            left_line_color = opts.line_color_fn(self, 'left') or default_line_color
            right_line_color = opts.line_color_fn(self, 'right') or default_line_color
        else:
            node_line_color = default_line_color
            left_line_color = default_line_color
            right_line_color = default_line_color

        canvas.create_oval(self.x + half_width - half_size, self.y, self.x + half_width + half_size, self.y + self.NODE_SIZE, outline=node_line_color)
        canvas.create_text(self.x + half_width, self.y + half_size, text=str(self.value), fill=text_color, font=('serif', self.FONT_SIZE))
        if self.count > 1:
            canvas.create_text(self.x + half_width, self.y + half_size + int(self.FONT_SIZE * .6), text=str(self.count), fill=text_color, font=('serif', self.FONT_SIZE//2))
        if opts.subtree_bounds:
            canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, outline=default_line_color)
        if self.left:
            canvas.create_line(self.x + half_width, self.y + self.NODE_SIZE, self.left.x + self.left.width / 2, self.left.y, fill=left_line_color)
            self.left._draw(canvas, opts)
        if self.right:
            canvas.create_line(self.x + half_width, self.y + self.NODE_SIZE, self.right.x + self.right.width / 2, self.right.y, fill=right_line_color)
            self.right._draw(canvas, opts)

    def insert(self, node):
        if node.value == self.value:
            self.count += 1
        elif node.value < self.value:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

    def find_path(self, value):
        if value == self.value:
            return True, [self]
        if value < self.value:
            subtree = self.left
        else:
            subtree = self.right

        if subtree:
            subtree_res = subtree.find_path(value)
            return subtree_res[0], [self] + subtree_res[1]
        else:
            return False, [self]

    def balance(self):
        hl = self.left.tree_height() if self.left else 0
        hr = self.right.tree_height() if self.right else 0
        return hr - hl

    def size(self):
        sl = self.left.size() if self.left else 0
        sr = self.right.size() if self.right else 0
        return sl + sr + 1

    def balanced_insert(self, v):
        if v == self.value:
            self.count += 1
            return
        balance = self.balance()
        if balance == 0:
            if v < self.value:
                if self.left:
                    self.left.balanced_insert(v)
                else:
                    self.left = TreeNode(v)
            else:
                if self.right:
                    self.right.balanced_insert(v)
                else:
                    self.right = TreeNode(v)
        elif balance < 0:
            if v < self.value:
                # rotate right, insert left
                pass
            else:
                if self.right:
                    self.right.balanced_insert(v)
                else:
                    self.right = TreeNode(v)
        else:  # balance > 0
            if v < self.value:
                if self.left:
                    self.left.balanced_insert(v)
                else:
                    self.left = TreeNode(v)
            else:
                # no need to nullcheck self.right
                # since we are leaning right, there _must_ be a self.right
                assert self.right
                new_self = self.rotate_left()
                new_self.balanced_insert(v)
                # rotate left, insert right
                pass

    def rotate_left(self):
        b_temp = self
        a_left_temp = self.right.left
        root = self.right  # B = A
        root.left = b_temp
        root.left.right = a_left_temp
        return root

    def rotate_right(self):
        b_temp = self
        a_right_temp = self.left.right
        root = self.left  # B = A
        root.right = b_temp
        root.right.left = a_right_temp
        return root

    def tree_height(self):
        return max(
            self.left.tree_height() if self.left else 0,
            self.right.tree_height() if self.right else 0,
        ) + 1


class TreeUI:
    def __init__(self):
        def text_color_fn(node):
            if node.value == 20:
                return '#4040FF'
            elif node.value == 15:
                return '#8080FF'
            elif node.value == 10:
                return '#FF0000'
            elif node.value == 5:
                return '#FF8800'
            elif node.value == 1:
                return '#FFFF00'
            else:
                return '#A0A0A0'
        self.draw_options = DrawOptions(['#FFF'], subtree_bounds=False, text_color_fn=text_color_fn)
        self.colorful = False
        self.reset()

    _extra_ui_init = False
    def _init_extra_ui(self, app):
        if not app:
            #print("Not ready...")
            return
        if self._extra_ui_init:
            return
        self._extra_ui_init = True

        print("INIT EXTRA UI")
        master = app.canvas.master
        #print("master = {}".format(master))
        import tkinter.messagebox
        from tkinter import ttk
        # from tkinter import Entry
        #e = tk.Entry(master, bg="#FFFFFF")

        def line_color_fn_highlight_path(node_found, path):
            def fn(node, what):
                if node_found:
                    color = '#00FF00'
                else:
                    color = '#FF0000'
                if what == 'node' and node in path:
                    return color
                elif what == 'left' and node.left in path:
                    return color
                elif what == 'right' and node.right in path:
                    return color
                else:
                    return None
            return fn

        entry_str_var = tk.StringVar(master, '')
        def onclick():
            input_val = entry_str_var.get()
            if not input_val:
                return
            if not input_val.isdigit():
                tkinter.messagebox.showinfo("title??", message="Invalid value, must enter an integer.\n\nYou entered: '{}'".format(input_val))
                return
            print("FIND val='{}'".format(input_val))
            result = self.tree.find_path(int(input_val))
            print("RESULT = {}".format(result))
            self.draw_options.line_color_fn = line_color_fn_highlight_path(result[0], result[1])
            self.draw(app)
            #tkinter.messagebox.showinfo("title??", message="Why is this a folder icon??\n\nAnyways, you entered: '{}'".format(input_val))
        row_frame = ttk.Frame(master)
        row_frame.pack(side=tk.LEFT)
        e = ttk.Entry(row_frame, textvariable=entry_str_var)
        e.pack(side=tk.LEFT)
        b = ttk.Button(row_frame, text="Find Node", command=onclick)
        b.pack(side=tk.LEFT)

    def bigtree(self, app):
        self._init_extra_ui(app)
        def bigtreeinner(value, sz):
            self.tree.insert(TreeNode(value))
            if sz > 1:
                bigtreeinner(value - sz, sz//2)
                bigtreeinner(value + sz, sz//2)

        value = 32
        self.tree = TreeNode(value)
        bigtreeinner(value - value//2, value//4)
        bigtreeinner(value + value//2, value//4)

        self.draw(app)
    # b = ttk.Button(row_frame, text="Big Tree!", command=bigtree)
    # b.pack(side=tk.RIGHT)


    def reset(self, app=None):
        self._init_extra_ui(app)
        #self.tree = TreeNode(50)
        self.tree = TreeNode(10, # B
                             TreeNode(5, TreeNode(1), TreeNode(7)),  # A + children
                             TreeNode(15, TreeNode(12), TreeNode(20)))  # B.right
        self.prev_tree = None
        self.tree.x = 5
        self.tree.y = 5
        self.next_value = 1
        if app:
            self.draw(app)

    def toggle_bounds(self, app):
        self.draw_options.subtree_bounds = not self.draw_options.subtree_bounds
        self.draw(app)

    def toggle_colorful(self, app):
        if self.colorful:
            self.draw_options.line_colors = ['#FFF']
        else:
            self.draw_options.line_colors = ['#F00', '#F80', '#FF0', '#0F0', '#0F8', '#0FF', '#08F', '#00F']
        self.colorful = not self.colorful
        self.draw(app)

    def add_node(self, app):
        self.prev_tree = self.tree.clone()
        self.tree.insert(TreeNode(random.randint(1, 100)))
        # self.tree.insert(TreeNode(self.next_value))
        # self.tree.insert(TreeNode([1, 74, 47][self.next_value - 1]))
        # self.tree.insert(TreeNode([52, 54, 56, 58, 49, 51, 53, 55, 57, 59][self.next_value - 1]))
        self.next_value += 1
        self.draw(app)

    def rotate_right(self, app):
        self.prev_tree = self.tree.clone()
        self.tree = self.tree.rotate_right()
        self.draw(app)

    def rotate_left(self, app):
        self.prev_tree = self.tree.clone()
        self.tree = self.tree.rotate_left()
        self.draw(app)

    def draw(self, app):
        # tree = TreeNode(
        #     10,
        #     TreeNode(5, None, None),
        #     TreeNode(12, None, TreeNode(20, TreeNode(15), TreeNode(21))))
        # tree.x = 5
        # tree.y = 5

        app.canvas.delete("all")
        self.tree.x = 5
        self.tree.y = 5
        self.tree.draw(app.canvas, self.draw_options)
        if self.prev_tree:
            self.prev_tree.x = self.tree.x + self.tree.width + 25
            self.prev_tree.y = self.tree.y
            self.prev_tree.draw(app.canvas, DrawOptions(['#888'], text_color_fn=self.draw_options.text_color_fn))

        app.canvas.create_text(5, 800, anchor=tk.SW, fill="#FFF", text="Height: " + str(self.tree.tree_height()))
        app.canvas.create_text(100, 800, anchor=tk.SW, fill="#FFF", text="Balance: " + str(self.tree.balance()))
        app.canvas.create_text(200, 800, anchor=tk.SW, fill="#FFF", text="Size: " + str(self.tree.size()))


tree_ui = TreeUI()
tk_base.TkBaseApp({
    "Add Node": tree_ui.add_node,
    "Rotate Left": tree_ui.rotate_left,
    "Rotate Right": tree_ui.rotate_right,
    "Toggle Bounds": tree_ui.toggle_bounds,
    "Toggle Colors": tree_ui.toggle_colorful,
    "Bigtree!": tree_ui.bigtree,
    "Reset": tree_ui.reset,
}).run()
