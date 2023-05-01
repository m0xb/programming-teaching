# https://chat.openai.com/chat
# Prompt: Using Python and Tcl/Tk, write code to display a chess board

# Here's a sample implementation in Python using Tcl/Tk to display a chess board:
import tkinter as tk

def create_board():
    root = tk.Tk()
    root.title("Chess Board")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    size = 50
    for row in range(8):
        for col in range(8):
            x1 = col * size
            y1 = row * size
            x2 = x1 + size
            y2 = y1 + size
            color = "white" if (row + col) % 2 == 0 else "lightgray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    root.mainloop()

if __name__ == "__main__":
    create_board()

# This code uses the tkinter library to create a graphical user interface with a canvas that is 400x400 pixels in size.
# The create_board function then uses a nested loop to create 64 rectangles, each 50x50 pixels in size, to represent the
# squares of a chess board. The fill color of each rectangle alternates between white and light gray based on its
# position in the grid. Finally, the mainloop method is called to start the GUI event loop and display the chess board.