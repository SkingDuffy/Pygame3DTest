import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# 初始化 Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# 定义一个简单的模型
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # 处理用户输入，例如键盘控制模型移动
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        glTranslatef(-0.1, 0, 0)
    if keys[pygame.K_RIGHT]:
        glTranslatef(0.1, 0, 0)
    if keys[pygame.K_UP]:
        glTranslatef(0, 0.1, 0)
    if keys[pygame.K_DOWN]:
        glTranslatef(0, -0.1, 0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Cube()
    pygame.display.flip()
    pygame.time.wait(10)
