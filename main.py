import pygame
import math
import pygame.locals
from sys import exit

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

r1 = 40 #radius of 2D circle
r2 = 100 #radius of the donut/torus

x_offset = WIDTH / 2
y_offset = HEIGHT / 2

def draw(x, y):
    pygame.draw.circle(screen, WHITE, (x + x_offset, y + y_offset), 1)

while True:
    for T in range(0, 628, 15):
        cosT, sinT = math.cos(T / 100), math.sin(T / 100)
    
        x2 = r2 + r1 * cosT #x coordinate of 2D circle
        y2 = r1 * sinT #y coordinate of 2D circle
        
        for P in range(0, 628, 15):
            cosP, sinP = math.cos(P / 100), math.sin(P / 100)
            
            x = x2 * cosP
            y = y2
            draw(x, y)
    
    for event in pygame.event.get(): #close the window when the button is pressed
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update() #display changes
