import time
import sys

from tkinter import *
from tkinter import ttk

from math import cos, pi, sin


def matrix_multiply(A, B):
    # check to see if the multiplication is legal
    # Number of cols in first must equal number of rows in second
    a_cols = len(A[0])
    b_rows = len(B)
    if a_cols == b_rows:
        # do multiplication
        result_matrix = []
        # pre-fill the result with the same number of rows as A
        a_rows = len(A)

        # Currently: Add an 1-item list for each row in the result matrix
        # BUT, we want this to be "flexible" and work with any number of b_cols
        # so: we actually want to add extra values in each sub-list
        # so, restate: Add an N-item list for each row in the result matrix where N=b_cols
        for current_row in range(a_rows):
            result_matrix.append([0]*len(B[0]))
            # for _ in range(len(B[0]) - 1):
            #     result_matrix[current_row].append(0)

        for b_col in range(len(B[0])):
            for b_idx, b_row in enumerate(B):
                for a_idx, a_row in enumerate(A):
                    val = b_row[b_col] * a_row[b_idx]
                    result_matrix[a_idx][b_col] += val
        return result_matrix
    else:
        raise Exception("Cannot multiply")


def execute():
    pass

# Define the GUI and various widgets
main_window = Tk()
# Create a container that belongs to the main window
container_frame = ttk.Frame(main_window, padding=10)
container_frame.grid()

#my_label1 = ttk.Label(container_frame, text="List:")
#my_label1.grid(column=0, row=1)

ttk.Button(container_frame, text="Quit", command=main_window.destroy).grid(column=0, row=0)
ttk.Button(container_frame, text="Execute", command=execute).grid(column=1, row=0)
canvas = Canvas(container_frame, bg="#000000", height=600, width=600)

## MATRIX BRAINSTORMING
"""
Identity matrix * vector
1 0 0   x   x + 0 + 0
0 1 0 * y = 0 + y + 0
0 0 1   1   0 + 0 + 1

Translation matrix
1 0 tx    x   x + 0 + tx
0 1 ty  * y = 0 + y + ty
0 0 1     1   0 + 0 +  1

Rotation matrix
1 0 0    x   x + 0 + 0
0 1 0  * y = 0 + y + 0
0 0 1    1   0 + 0 + 1

Rotation matrix (in same dimension, for simplicity)
1    p     x      1 * x + p * y
q    1  *  y =    x * q + 1 * y
Are q and p rotX and rotY???? Not sure....


1    p     1      1 * x + p * y   0
q    1  *  0 =    x * q + 1 * y = 1

Two eqs:
  1 * 1 + p * 0 = 0   --> 1 + 0 = 0
  1 * q + 1 * 0 = 1

Rotation matrix (a, b, c, d are UNKNOWN)
a    b     x      a * x + b * y = x`
c    d  *  y =    c * x + d * y = y`

ø = pi/2 (90 deg)
x = 1
y = 0

x = 1 --> matrix transform --> x` = 0

a * 1 + b * y = 0
a + by = 0 (simplify)
a = 0 (y=0)

sin(0) = 0
cos(pi/2) = 0 

cos(ø) * x + b * y = x`

Rotation matrix (b, c are UNKNOWN)
cos(ø)    b     x      cos(ø) * x + b * y = x`
c    sin(ø)  *  y =    c * x + sin(ø) * y = y`


c * x + sin(ø) * y = y`


Rotation matrix (maybe???)
cos(ø)  cos(ø)     x        cos(ø) * x + cos(ø) * y = x`
sin(ø)  sin(ø)  *  y   =    sin(ø) * x + sin(ø) * y = y`

ø=pi/6
x=1
y=0
sin(pi/6) * x + sin(pi/6) * y = y`
1/2 * 1 + 1/2 * 0 = 1/2

ø=pi/6
x=cos(7pi/4) = sqrt(2)/2
y=sin(7pi/4) = ''

x`=cos(7pi/4 + pi/6) = -0.258
x`=sin(7pi/4 + pi/6) = 0.965

cos(ø) * x + cos(ø) * y = -0.258
cos(pi/6) * cos(7pi/4) + cos(pi/6) * sin(7pi/4) = -0.258






"""


def rotate_points_with_matrix(points, angle):
    # for each x,y pair in `points`, apply the matrix transformation
    result = []
    for i in range(int(len(points)/2)):
        idx = 2 * i
        new_point = rotate_point_with_matrix(points[idx], points[idx+1], angle)
        result.append(new_point[0][0])
        result.append(new_point[1][0])
    return result


def rotate_point_with_matrix(x, y, angle):
    rot_matrix = [
        [cos(angle), -sin(angle)],
        [sin(angle), cos(angle)]
    ]
    transformed_point = matrix_multiply(rot_matrix, [[x], [y]])
    return transformed_point



rotate_degrees = 0
def animation():
    global rotate_degrees
    rotate_degrees += 2
    ## DRAWING CODE
    # https://www.tutorialspoint.com/how-to-clear-tkinter-canvas
    canvas.delete('all')
    canvas.create_rectangle(0, 0, 600, 600, fill="#000", outline="")
    canvas.create_rectangle(100, 100, 500, 500, fill="", outline="#00F")
    canvas.create_oval(100, 100, 500, 500, fill="", outline="#00F")

    points_global_coords = [
        (300 + cos(3 * pi / 4) * 200),(300 + -sin(3 * pi / 4) * 200),
        (300 + cos(pi/4) * 200),(300 + -sin(pi/4) * 200),
        (cos(7*pi/4) * 200 + 300),(-sin(7*pi/4) * 200 + 300),
        (cos(5*pi/4)*200+300),(300+-sin(5*pi/4)*200)
    ]
    points_local_coords = [
        (cos(3 * pi / 4) * 200), (-sin(3 * pi / 4) * 200),
        (cos(pi/4) * 200), (-sin(pi/4) * 200),
        (cos(7*pi/4) * 200), (-sin(7*pi/4) * 200),
        (cos(5*pi/4)*200), (-sin(5*pi/4)*200)
    ]

    # Rotate with a MATRIX
    rotated_local_coords = rotate_points_with_matrix(points_local_coords, rotate_degrees / 180 * pi)

    # Translate the points over by 300 pixels in X and Y
    points = []
    for point in rotated_local_coords:
        points.append(point + 300)

    canvas.create_polygon(points[0], points[1], points[2], points[3], points[4], points[5], points[6], points[7], fill="", outline="red")

    main_window.after(15, animation)

## END DRAWING CODE

#canvas.pack(fill=BOTH, expand=1)
canvas.grid(row=1, column=0)

# Trigger the animation
animation()

# Start the GUI application!
main_window.mainloop()
