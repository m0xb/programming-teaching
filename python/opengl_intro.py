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

px = 300
py = 300

xrot = 0
yrot = 0
zrot = 0

real_glColor3f = glColor3f
def cube(color):
    # HACK: Disable color
    if not color:
        real_glColor3f(1, 1, 1, 0)
        glColor3f = lambda x, y, z: None
    else:
        glColor3f = real_glColor3f

    glBegin(GL_QUADS)
    glColor3f(1.0,1.0,0.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glColor3f(0.0,1.0,0.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glColor3f(0.0,1.0,1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glColor3f(1.0,1.0,1.0)
    glVertex3f( 1.0, 1.0, 1.0)

    glColor3f(1.0,0.0,1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glColor3f(0.0,0.0,0.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glColor3f(1.0,0.0,0.0)
    glVertex3f( 1.0,-1.0,-1.0)

    glColor3f(1.0,1.0,1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glColor3f(0.0,1.0,1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glColor3f(1.0,0.0,1.0)
    glVertex3f( 1.0,-1.0, 1.0)

    glColor3f(1.0,0.0,0.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glColor3f(0.0,0.0,0.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glColor3f(0.0,1.0,0.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glColor3f(1.0,1.0,0.0)
    glVertex3f( 1.0, 1.0,-1.0)

    glColor3f(0.0,1.0,1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glColor3f(0.0,1.0,0.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glColor3f(0.0,0.0,0.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(-1.0,-1.0, 1.0)

    glColor3f(1.0,1.0,0.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glColor3f(1.0,1.0,1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glColor3f(1.0,0.0,1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glColor3f(1.0,0.0,0.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glEnd()


z = -5
h = -0.001
def drawPlayer():
    #glTranslatef(0.02, 0.0, 0.02)
    glScalef(0.5, 0.5, 0.5)

    global xrot, yrot, zrot
    #glRotatef(xrot, 1, 0, 0)
    # glRotatef(yrot, 0, 1, 0)
    glRotatef(30, 0, 1, 0)
    glRotatef(zrot, 0, 0, 1)
    xrot = xrot + 1
    yrot = yrot + .1
    zrot = zrot + 1

    # https://www.reddit.com/r/opengl/comments/bl3v02/drawing_wireframe_on_top_of_mesh/
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    cube(False)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    cube(True)

    # glColor3f(1,1,0)
    # glPointSize(8)
    # glBegin(GL_POINTS)
    # glVertex2i(px,py)
    # glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    drawPlayer()

    glutSwapBuffers()

def buttons(key, x, y):
    global px, py, xrot, yrot
    if key == b'a':
        px -= 5
    if key == b'd':
        px += 5
    if key == b'w':
        py -= 5
    if key == b's':
        py += 5
    if key == b'q':
        xrot -= 1
    if key == b'e':
        xrot += 1
    glutPostRedisplay()


def init():
    glEnable(GL_DEPTH_TEST)
    #return
    glClearColor(0.1, 0.1, 0.1, 0)
    return
    gluOrtho2D(0,1024,512,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1024, 512)
    window = glutCreateWindow("Python OpenGL controllable")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()

if __name__ == "__main__":
    main()
