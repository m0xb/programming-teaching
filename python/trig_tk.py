from tkinter import *
from tkinter import ttk

def default_text():
    return """
    canvas.create_rectangle(0, 0, 600, 600, fill="#000", outline="")
    canvas.create_rectangle(100, 100, 500, 500, fill="#0F0", outline="")
    canvas.create_polygon((300 + cos(3 * pi / 4) * 200),(300 + -sin(3 * pi / 4) * 200), (300 + cos(pi/4) * 200),(300 + -sin(pi/4) * 200), (cos(7*pi/4) * 200 + 300),(-sin(7*pi/4) * 200 + 300), (cos(5*pi/4)*200+300),(300+-sin(5*pi/4)*200), fill="", outline="red")

    
    """
# canvas.create_text(300, 50, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))

class Dyno:
    pass

def execute_code():
    from math import cos, pi, sin
    sz = 600
    hsz = sz/2
    ns = Dyno()

    global textarea
    code = textarea.get("1.0", END)
    print("execute code '{}'!".format(code))
    statements = code.split('\n')
    for statement in statements:
        if statement:
            try:
                print("eval(): {} -> {}".format(statement, eval(statement)))
            except:
                pass

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

textarea = Text(container_frame, bg="#aaaaaa", fg="#000000", height=26, width=50, font=("Consolas", 20))
textarea.insert("1.0", default_text())
textarea.grid(row=1, column=1)


# Start the GUI application!
main_window.mainloop()
