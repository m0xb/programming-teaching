from tkinter import *
from tkinter import ttk

# This is not actually used.
# Paste this into the program as an example of drawing something
def example_code():
    [
        canvas.create_rectangle(0, 0, 600, 600, fill="#000", outline=""),
        canvas.create_rectangle(0, 0, 600, 312, fill="#FFF", outline=""),
        canvas.create_rectangle(0, 0, 240, 168, fill="#22A"),
        canvas.create_rectangle(240, 0, 600, 24, fill="#D00", outline=""),
        canvas.create_rectangle(240, 48, 600, 72, fill="#D00", outline=""),
        canvas.create_rectangle(240, 96, 600, 120, fill="#D00", outline=""),
        canvas.create_rectangle(240, 144, 600, 168, fill="#D00", outline=""),
        canvas.create_rectangle(0, 192, 600, 216, fill="#D00", outline=""),
        canvas.create_rectangle(0, 240, 600, 264, fill="#D00", outline=""),
        canvas.create_rectangle(0, 288, 600, 312, fill="#D00", outline=""),
        create_star(canvas, 20, 25, 20, "#FFF"),
        create_star(canvas, 60, 25, 20, "#FFF"),
        create_star(canvas, 100, 25, 20, "#FFF"),
        create_star(canvas, 140, 25, 20, "#FFF"),
        create_star(canvas, 180, 25, 20, "#FFF"),
        create_star(canvas, 220, 25, 20, "#FFF"),

        create_star(canvas, 40, 45, 20, "#FFF"),
        create_star(canvas, 80, 45, 20, "#FFF"),
        create_star(canvas, 120, 45, 20, "#FFF"),
        create_star(canvas, 160, 45, 20, "#FFF"),
        create_star(canvas, 200, 45, 20, "#FFF"),

        create_star(canvas, 20, 65, 20, "#FFF"),
        create_star(canvas, 60, 65, 20, "#FFF"),
        create_star(canvas, 100, 65, 20, "#FFF"),
        create_star(canvas, 140, 65, 20, "#FFF"),
        create_star(canvas, 180, 65, 20, "#FFF"),
        create_star(canvas, 220, 65, 20, "#FFF"),

        create_star(canvas, 40, 85, 20, "#FFF"),
        create_star(canvas, 80, 85, 20, "#FFF"),
        create_star(canvas, 120, 85, 20, "#FFF"),
        create_star(canvas, 160, 85, 20, "#FFF"),
        create_star(canvas, 200, 85, 20, "#FFF"),

        create_star(canvas, 20, 105, 20, "#FFF"),
        create_star(canvas, 60, 105, 20, "#FFF"),
        create_star(canvas, 100, 105, 20, "#FFF"),
        create_star(canvas, 140, 105, 20, "#FFF"),
        create_star(canvas, 180, 105, 20, "#FFF"),
        create_star(canvas, 220, 105, 20, "#FFF"),

        create_star(canvas, 40, 125, 20, "#FFF"),
        create_star(canvas, 80, 125, 20, "#FFF"),
        create_star(canvas, 120, 125, 20, "#FFF"),
        create_star(canvas, 160, 125, 20, "#FFF"),
        create_star(canvas, 200, 125, 20, "#FFF"),

        create_star(canvas, 20, 145, 20, "#FFF"),
        create_star(canvas, 60, 145, 20, "#FFF"),
        create_star(canvas, 100, 145, 20, "#FFF"),
        create_star(canvas, 140, 145, 20, "#FFF"),
        create_star(canvas, 180, 145, 20, "#FFF"),
        create_star(canvas, 220, 145, 20, "#FFF"),
    ]

    canvas.create_polygon(20,5, 25,20, 40,25, 25,30, 34,46, 20,38, 6,46, 15,30, 0,25, 5,20, fill="#FFF", outline=""),
    canvas.create_rectangle(0, 0, 600, 600, fill="#000", outline=""),
    canvas.create_polygon(*list(map(lambda x: x, [5, 60, 30, 0, -30, 30, 30, 30, -30, 0, 0,60])), fill="#FFF", outline=""),
    [
        canvas.create_rectangle(0, 0, 600, 600, fill="#000", outline=""),
        canvas.create_polygon(
            hsz+cos(pi/2 - 0/5*pi)*hsz, hsz-sin(pi/2 - 0/5*pi)*hsz,
            hsz+cos(3/2*pi + 4/5*pi)*hsz/2.7, hsz-sin(3/2*pi + 4/5*pi)*hsz/2.7,
            hsz+cos(pi/2 - 2/5*pi)*hsz, hsz-sin(pi/2 - 2/5*pi)*hsz,
            hsz+cos(3/2*pi + 2/5*pi)*hsz/2.7, hsz-sin(3/2*pi + 2/5*pi)*hsz/2.7,
            hsz+cos(pi/2 - 4/5*pi)*hsz, hsz-sin(pi/2 - 4/5*pi)*hsz,
            hsz+cos(3/2*pi), hsz-sin(3/2*pi)*hsz/2.7,
            hsz+cos(pi/2 - 6/5*pi)*hsz, hsz-sin(pi/2 - 6/5*pi)*hsz,
            hsz+cos(3/2*pi - 2/5*pi)*hsz/2.7, hsz-sin(3/2*pi - 2/5*pi)*hsz/2.7,
            hsz+cos(pi/2 - 8/5*pi)*hsz, hsz-sin(pi/2 - 8/5*pi)*hsz,
            hsz+cos(3/2*pi - 4/5*pi)*hsz/2.7, hsz-sin(3/2*pi - 4/5*pi)*hsz/2.7,
            fill="#F00", outline=""),
    ]

def create_star(canvas, x, y, sz, fill):
    from math import cos, pi, sin
    hsz = sz/2
    qsz = hsz/2.7
    canvas.create_polygon(
        x+cos(pi/2 - 0/5*pi)*hsz, y-sin(pi/2 - 0/5*pi)*hsz,
        x+cos(3/2*pi + 4/5*pi)*qsz, y-sin(3/2*pi + 4/5*pi)*qsz,
        x+cos(pi/2 - 2/5*pi)*hsz, y-sin(pi/2 - 2/5*pi)*hsz,
        x+cos(3/2*pi + 2/5*pi)*qsz, y-sin(3/2*pi + 2/5*pi)*qsz,
        x+cos(pi/2 - 4/5*pi)*hsz, y-sin(pi/2 - 4/5*pi)*hsz,
        x+cos(3/2*pi)*qsz, y-sin(3/2*pi)*qsz,
        x+cos(pi/2 - 6/5*pi)*hsz, y-sin(pi/2 - 6/5*pi)*hsz,
        x+cos(3/2*pi - 2/5*pi)*qsz, y-sin(3/2*pi - 2/5*pi)*qsz,
        x+cos(pi/2 - 8/5*pi)*hsz, y-sin(pi/2 - 8/5*pi)*hsz,
        x+cos(3/2*pi - 4/5*pi)*qsz, y-sin(3/2*pi - 4/5*pi)*qsz,
        fill=fill, outline=""),

def execute_code():
    from math import cos, pi, sin
    sz = 600
    hsz = sz/2


    #canvas.create_polygon(sz/2, 0, sz/2 + cos(2*pi/5)*sz, 300, 0, 100, fill="#FFF", outline=""),
    #return
    global textarea
    code = textarea.get("1.0", END)
    print("execute code '{}'!".format(code))
    print("eval result: {}".format(eval(code)))

# Define the GUI and various widgets
main_window = Tk()
# Create a container that belongs to the main window
container_frame = ttk.Frame(main_window, padding=10)
container_frame.grid()

#my_label1 = ttk.Label(container_frame, text="List:")
#my_label1.grid(column=0, row=1)

ttk.Button(container_frame, text="Quit", command=main_window.destroy).grid(column=0, row=0)
ttk.Button(container_frame, text="Execute", command=execute_code).grid(column=1, row=0)
canvas = Canvas(container_frame, bg="#000000", height=600, width=600)
#canvas.pack(fill=BOTH, expand=1)
canvas.grid(row=1, column=0)

textarea = Text(container_frame, bg="#666666", fg="#000000", height=26, width=50, font=("Consolas", 20))
textarea.insert("1.0", """[\ncanvas.create_rectangle(0, 0, 600, 600, fill="#000", outline=""),\n\n]""")
textarea.grid(row=1, column=1)


# Start the GUI application!
main_window.mainloop()
