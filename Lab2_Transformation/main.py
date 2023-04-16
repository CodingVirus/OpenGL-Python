from OpenGL.GLUT import *
from OpenGL.GL import *


deg = 15.

def draw():
    global deg
    glClearColor(0., 0., 0., 0.)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1., 1., 1.)
    glPushMatrix()
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    glLineWidth(2.)

    # rect at (0.5, 0.5, 0.)
    for i in range(1, 25):
        glBegin(GL_LINE_LOOP)
        glVertex3f(0.6, 0.85, 0.0)
        glVertex3f(0.75, 0.85, 0.0)
        glVertex3f(0.75, 0.7, 0.0)
        glVertex3f(0.6, 0.7, 0.0)
        glEnd()

    # rotate 45 deg
        glPushMatrix()
        glTranslatef(0.5, 0.5, 0) # T^-1
        glRotatef(deg, 0, 0, 1) # R
        glTranslatef(-0.5, -0.5, 0) # T

    glPopMatrix()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(250, 250)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"My Second OpenGL Program")
glutDisplayFunc(draw)
glutMainLoop()
