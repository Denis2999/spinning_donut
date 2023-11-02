import pygame
from pygame.locals import *

from OpenGL.GL import * #bad practice. Should be changed in future
from OpenGL.GLU import * #bad practice. Should be changed in future


vertices = (
    (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1),
    (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1)
)
edge = (
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 7), (7, 5), (5, 6), (6, 4),
    (3,6), (0, 4), (2, 5), (1, 7)
)
display = (800, 600)


def cube():
    glBegin(GL_LINES)
    for e in edge:
        for vertex in e:
            glVertex3fv(vertices[vertex])
    glEnd()

pygame.init()

pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("Sample OpenGL")

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, 0-5)

while True:
    for event in pygame.event.get(): #close the window when the button is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
    
    glRotatef(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    cube()
    # update display
    pygame.display.flip()
    # update loop sleep
    pygame.time.wait(15)
