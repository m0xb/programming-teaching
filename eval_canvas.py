from tkinter import *
from tkinter import ttk

def execute_code():
    global textarea
    code = textarea.get("1.0", END)
    print("execute code '{}'!".format(code))
    print("eval result: {}".format(eval(code)))

# Define the GUI and various widgets
main_window = Tk()
# Create a container that belongs to the main window
container_frame = ttk.Frame(main_window, padding=10)
container_frame.grid()

# Create two label widgets and assign to variables
my_label1 = ttk.Label(container_frame, text="List:")
my_label1.grid(column=0, row=1)

ttk.Button(container_frame, text="Quit", command=main_window.destroy).grid(column=1, row=0)
ttk.Button(container_frame, text="Execute", command=execute_code).grid(column=2, row=0)
canvas = Canvas(container_frame, bg="#FF00FF", height=600, width=600)
#canvas.pack(fill=BOTH, expand=1)
canvas.grid(row=1, column=0)

textarea = Text(container_frame, bg="#666666", fg="#000000", height=30, width=60, font=("Consolas", 32))
textarea.grid(row=1, column=1)


# Start the GUI application!
main_window.mainloop()
