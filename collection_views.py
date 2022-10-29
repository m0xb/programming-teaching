# Import everything from the tkinter module
from tkinter import *
# Import the ttk module - not covered by the * above
from tkinter import ttk

n = 10
my_list = list(range(n))

def my_list_even_view():
    def is_even(n):
        return n % 2 == 0
    return list(filter(is_even, my_list))

def do_something():
    global n
    my_list.append(n)
    n += 1
    my_label1.configure(text="List: {}".format(my_list))
    my_label2.configure(text="List View: {}".format(my_list_even_view()))

# Define the GUI and various widgets
main_window = Tk()
# Create a container that belongs to the main window
container_frame = ttk.Frame(main_window, padding=10)
container_frame.grid()

# Create two label widgets and assign to variables
my_label1 = ttk.Label(container_frame, text="List: {}".format(my_list))
my_label1.grid(column=0, row=1)
my_label2 = ttk.Label(container_frame, text="List View: {}".format(my_list_even_view()))
my_label2.grid(column=0, row=2)

#ttk.Label(container_frame, text="Hello Tucker and Pearl!").grid()
ttk.Button(container_frame, text="DO SOMETHING", command=do_something).grid(column=0, row=0)
ttk.Button(container_frame, text="Quit", command=main_window.destroy).grid(column=1, row=0)


# Start the GUI application!
main_window.mainloop()
