# Note: Using python 3.10 venv (venv310), since Python 3.9 venv gets error:
# $ pip install PyOpenGL_accelerate
#   ...
#   src/wrapper.c:4:10: fatal error: 'Python.h' file not found
#
# Semi-related: https://github.com/pypa/pip/issues/6420, https://stackoverflow.com/questions/35778495/fatal-error-python-h-file-not-found-while-installing-opencv
#
# So, `source venv310/bin/activate` first

# Code based on https://stackoverflow.com/questions/66744140/pyopengl-taking-keyboard-input
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

px = 300; py = 300

def drawPlayer():

    glColor3f(1,1,0)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2i(px,py)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawPlayer()
    glutSwapBuffers()

def buttons(key,x,y):
    global px, py
    if key == b'a':
        px -= 5
    if key == b'd':
        px += 5
    if key == b'w':
        py -= 5
    if key == b's':
        py += 5
    glutPostRedisplay()


def init():
    glClearColor(0.3,0.3,0.3,0)
    gluOrtho2D(0,1024,512,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1024, 512)
    window = glutCreateWindow("Python OpenGL controllable")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()

if __name__ == "__main__":
    main()
