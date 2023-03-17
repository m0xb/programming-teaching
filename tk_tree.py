import random

import tk_base

class TreeNode:

    NODE_SIZE = 30
    H_PAD = 5
    V_PAD = 5

    def __init__(self, value, left=None, right=None):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.value = value
        self.left = left
        self.right = right

    def draw(self, canvas):
        self.calculate_size()
        self.calculate_child_positions()
        self._draw(canvas)

    def calculate_child_positions(self):
        half_width = self.width / 2
        if self.left:
            self.left.x = self.x
            self.left.y = self.y + self.NODE_SIZE + self.V_PAD
            self.left.calculate_child_positions()
        if self.right:
            self.right.x = self.x + half_width + self.H_PAD/2
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
            self.width = max_width * 2 + self.H_PAD
            # minimal size -- broken :-(
            #self.width = self.left.width if self.left else 0 + self.right.width if self.right else 0 + self.H_PAD
            self.height = self.NODE_SIZE + max_height + self.V_PAD

    def _draw(self, canvas):
        half_width = self.width / 2
        half_size = self.NODE_SIZE / 2
        canvas.create_oval(self.x + half_width - half_size, self.y, self.x + half_width + half_size, self.y + self.NODE_SIZE, outline="#FF0")
        canvas.create_text(self.x + half_width, self.y + half_size, text=str(self.value))
        if self.left:
            canvas.create_line(self.x + half_width, self.y + self.NODE_SIZE, self.left.x + self.left.width / 2, self.left.y)
            self.left._draw(canvas)
        if self.right:
            canvas.create_line(self.x + half_width, self.y + self.NODE_SIZE, self.right.x + self.right.width / 2, self.right.y)
            self.right._draw(canvas)

    def insert(self, node):
        if node.value < self.value:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node


class TreeUI:
    def __init__(self):
        self.tree = TreeNode(50)
        self.next_value = 51

    def draw(self, app):
        # tree = TreeNode(
        #     10,
        #     TreeNode(5, None, None),
        #     TreeNode(12, None, TreeNode(20, TreeNode(15), TreeNode(21))))
        # tree.x = 5
        # tree.y = 5

        app.canvas.delete("all")
        self.tree.insert(TreeNode(random.randint(1, 100)))
        # self.tree.insert(TreeNode(self.next_value))
        self.next_value += 1
        self.tree.draw(app.canvas)


tk_base.TkBaseApp({"Draw": TreeUI().draw}).run()
