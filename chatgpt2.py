# Prompt: Modify the previous Python program to draw pawns in the appropriate places

# Here's a modified version of the previous program to draw pawns in the appropriate places on the chess board:
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

            if row == 1 or row == 6:
                canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="black")

    root.mainloop()

if __name__ == "__main__":
    create_board()

# In this version of the code, an additional check is added inside the nested loop. If the row is equal to 1 or 6, a
# black oval is created on the square to represent a pawn. The oval is created with a 10 pixel margin on all sides to
# make sure it fits within the 50x50 pixel square.