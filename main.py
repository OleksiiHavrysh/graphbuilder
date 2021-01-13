import pygame
import sys
from pygame.locals import *
import cmath
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)

clock = pygame.time.Clock()
clock.tick(10)

background_colour = (150,150,150)
#(width, height) = (500, 500)
screen = pygame.display.set_mode((500, 500))#(0, 0), pygame.FULLSCREEN)#(width, height) (1535,800)
pygame.display.set_caption('Graph Builder')
screen.fill(background_colour)
#pygame.display.flip()
running = True

color = (255,255,0)
radius = 20
nnode = 0
nedge = 0
class Node:
    x: float
    y: float
listnodex = [0]*100
listnodey = [0]*100
listedge = [[0]*100]*100



##############################
# Хранить данные будем в списке рёбер
#
#
#
#
# connect vertices (вершины / nodes / points) on shift + click on first + click on second
#
#
#
###############################



def drawnode (color, radius, mousepos):
    global nnode
    pygame.draw.circle(screen, color, (mousepos), radius, 0)  # draws circle
    pygame.draw.circle(screen, (0, 0, 0), (mousepos), radius + 1, 1)  # draws outline
    nnode += 1
    textsurface = myfont.render(str(nnode), False, (0, 0, 0))
    screen.blit(textsurface, (mousepos[0] - 8, mousepos[1] - 10))
    listnodex[nnode] = mousepos[0]
    listnodey[nnode] = mousepos[1]


def drawline (color, start_node, end_node):
    global nnode, nedge
    nedge += 1
    start = (listnodex[start_node], listnodey[start_node])
    end = (listnodex[end_node], listnodey[end_node])

    vector = (listnodex[end_node]-listnodex[start_node], listnodey[end_node]-listnodey[start_node])
    angle = cmath.atan(vector[1]/vector[0])

    sinus = cmath.sin(angle)
    cosinus = cmath.cos(angle)

    xproec = radius * sinus
    yproec = radius * cosinus

    x = listnodex[start_node] + xproec
    y = listnodey[start_node] + yproec

    #start = (x, y)

    listedge[start_node][end_node] = 1
    listedge[end_node][start_node] = 1
    pygame.draw.line(screen, (0, 0, 255), (start), (end))

node1 = 0
node2 = 0
nodetest = 0

while running:
    pygame.display.flip()
    mousepos = pygame.mouse.get_pos()
    #pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif pygame.key.get_pressed()[K_RSHIFT] or pygame.key.get_pressed()[K_LSHIFT]:
            running1 = True


            mousepos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if node1 == 0:

                    nodetest = 0
                    for node in range(10):
                        nodetest += 1
                        x = listnodex[node]
                        y = listnodey[node]
                        mousepos = pygame.mouse.get_pos()
                        if (mousepos[0] - x)*(mousepos[0] - x) + (mousepos[1] - y)*(mousepos[1] - y) <= radius*radius:
                            node1 = nodetest - 1
                elif node2 == 0:
                    nodetest = 0
                    for node in range(10):
                        nodetest += 1
                        x = listnodex[node]
                        y = listnodey[node]
                        mousepos = pygame.mouse.get_pos()
                        if (mousepos[0] - x)*(mousepos[0] - x) + (mousepos[1] - y)*(mousepos[1] - y) <= radius*radius:
                            node2 = nodetest - 1

                print(node1, node2)
                if node1 != 0 and node2 != 0:
                    drawline(color, node1, node2)
                    node1 = 0
                    node2 = 0


        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # left button == 1
            drawnode (color, radius, mousepos)

