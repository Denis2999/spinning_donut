import pygame
import math
import pygame.locals
from sys import exit

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
font = pygame.font.SysFont("arial", 10, bold=True)

radius = 150 #radius of the circle
x_offset = WIDTH / 2
y_offset = HEIGHT / 2

def draw(x, y):
    pygame.draw.circle(screen, WHITE, (x + x_offset, y + y_offset), 1)


while True:
    for T in range(0, 628, 15):
        cosT, sinT = math.cos(T / 100), math.sin(T / 100)
        x = radius * cosT
        y = radius * sinT
        draw(x, y)

    for event in pygame.event.get(): #close the window when the button is pressed
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update() #display changes