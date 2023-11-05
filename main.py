import pygame
import math
import pygame.locals
from sys import exit

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
font = pygame.font.SysFont("arial", 10, bold=True)

r1 = 48 #radius of 2D circle
r2 = 96 #radius of the donut/torus
A, B = 1, 1 #rotation angles x- & z-axis
K2 = 4096 #distance from viewer to donut
K1 = WIDTH * K2 * 3 / (8 * (r1 + r2)) #distance viewer to screen

x_offset = WIDTH / 2
y_offset = HEIGHT / 2

x_space = 4 #width of character
y_space = 8 #height of character
columns = int(WIDTH / x_space)
rows = int(HEIGHT / y_space)

chars = [".", ",", "-", "~", ":", ";", "=", "!", "*", "#", "$", "@"]


def draw(x, y, char):
    text = font.render(char, True, WHITE)
    screen.blit(text, (x, y))

pygame.display.set_caption("Spinning Donut")

while True:
    screen.fill((BLACK)) #erase previous donut
    cosB, sinB = math.cos(B), math.sin(B)
    cosA, sinA = math.cos(A), math.sin(A)

    #store characters
    output = []
    for i in range(rows):
        col1 = [" " for i in range(columns)]
        output.append(col1)

    #store z-values
    zbuffer = []
    for i in range(rows):
        col2 = [0 for i in range(columns)]
        zbuffer.append(col2)

    for T in range(0, 1024, 8):
        cosT, sinT = math.cos(T / 100), math.sin(T / 100)
    
        x2 = r2 + r1 * cosT #x coordinate of 2D circle
        y2 = r1 * sinT #y coordinate of 2D circle
        
        for P in range(0, 1024, 8):
            cosP, sinP = math.cos(P / 100), math.sin(P / 100)
            
            x = x2 * (cosB * cosP + sinA * sinB *sinP) - y2 * cosA * sinB
            y = x2 * (cosP * sinB - cosB * sinA *sinP) + y2 * cosA * cosB
            z = K2 + r1 * sinA * sinT + cosA * sinP * x2
            ooz = 1 / z

            #x and y protection on the screen
            xp = math.floor(x * K1 * ooz)
            yp = math.floor(-y * K1 * ooz)

            #lumiance
            l = cosP * cosT * sinB - cosA * cosT * sinP - sinA * sinT + cosB * (cosA * sinT - cosT * sinA * sinP)

            #check if point is pointing towards light source
            if l > -0.8:
                l = abs(l)
                yc = int((yp + y_offset) / y_space)
                xc = int((xp + x_offset) / x_space)
                if ooz > zbuffer[yc][xc]:
                    zbuffer[yc][xc] = ooz
                L = round(l * 8)
                output[yc][xc] = chars[L]
    for a in range(rows):
        for b in range(columns):
            draw(b * x_space, a * y_space, output[a][b])

    #prevent A and B to go up to infinity
    if A > 6.283 and A < 6.2831:
        A = 0
        B = 0
    else:
        A += 0.06
        B += 0.04

    for event in pygame.event.get(): #close the window when the button is pressed
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update() #display changes

