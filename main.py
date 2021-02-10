import pygame
import sys
from pygame.locals import *
import cmath
import pygame.locals

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15)

clock = pygame.time.Clock()


background_colour = (200,200,200)
#(width, height) = (500, 500)
screen = pygame.display.set_mode((500, 500))#(0, 0), pygame.FULLSCREEN)#(width, height) (1535,800)
pygame.display.set_caption('Graph Builder')
screen.fill(background_colour)
#pygame.display.flip()
running = True

textsurface = myfont.render("INFO", False, (0, 0, 0))
screen.blit(textsurface, (5, 5))



color = (255,255,0)
radius = 20
nnode = 1
nedge = 0
listnodex = [0]*100
listnodey = [0]*100
listedge = [[0]*100]*100
listnodex1 = [0]*100
listnodey1 = [0]*100
listedge1 = [[0]*100]*100
nnode1 = 0

##############################
# Хранить данные будем в списке рёбер
#
#
#
#
# connect vertices (вершины / nodes / points) on shift + click on first + click on second
#
#
###############################



def drawnode (color, radius, mousepos, nnode):
    pygame.draw.circle(screen, color, (mousepos), radius, 0)  # draws circle
    pygame.draw.circle(screen, (0, 0, 0), (mousepos), radius + 1, 1)  # draws outline
    # nnode += 1
    textsurface = myfont.render(str(nnode), False, (0, 0, 0))
    screen.blit(textsurface, (mousepos[0] - 8, mousepos[1] - 10))
    listnodex[nnode] = mousepos[0]
    listnodey[nnode] = mousepos[1]


def drawline (color, start_node, end_node, width):
    global nnode, nedge
    nedge += 1

    end = (listnodex[end_node], listnodey[end_node])

    vector = (listnodex[end_node]-listnodex[start_node], listnodey[end_node]-listnodey[start_node])
    if vector[0] == 0:
        angle = cmath.atan(3.14159265/2)
    else:
        angle = cmath.atan(vector[1]/vector[0])


    sinus = cmath.sin(angle)
    cosinus = cmath.cos(angle)

    xproec = radius * sinus
    yproec = radius * cosinus

    x = listnodex[start_node] + xproec
    y = listnodey[start_node] + yproec
    start = (listnodex[start_node], listnodey[start_node])
    #start = (x, y)

    listedge[start_node][end_node] = 1
    listedge[end_node][start_node] = 1

    pygame.draw.line(screen, color, (start), (end), width)
    drawnode((255,255,0), 20, (start), start_node)
    drawnode((255, 255, 0), 20, (end), end_node)

node1 = 0
node2 = 0
nodetest = 0

def deletenode(radius, node):
    global nnode

    pygame.draw.circle(screen, background_colour, (listnodex[node],listnodey[node]), radius + 2, 0)  # draws circle
    for i in range(nnode + 1):
        if listedge[node][i] == 1:
            drawline(background_colour, node, i, 2)
            drawnode(color, 20, (listnodex[i], listnodey[i]), i)
            pygame.draw.circle(screen, background_colour, (listnodex[node], listnodey[node]), radius + 2, 0)
            listedge[node][i] = 0
    #listnodex[node] = -100
    #listnodey[node] = -100
    listnodex.remove(listnodex[node])
    listnodey.remove(listnodey[node])
    listedge.remove(listedge[node])
    #for _ in range(nnode):
    #    listedge.remove(listedge[node][_])
    nnode -= 1
    for i in range(nnode):
        if i != 0:
            drawnode(color, 20, (listnodex[i], listnodey[i]), i)





def update():
    global nnode
    screen.fill(background_colour)
    listedge[0][0] = 0
    for i in range(nnode):
        for j in range(nnode):
            if listedge[i][j] == 1 and i != j and i != 0 and j != 0:
                print(i,j)
                pygame.draw.line(screen, (0,0,0), (listnodex[i], listnodey[i]), (listnodex[j], listnodey[j]), 2)
    for i in range(nnode):
        if listnodex[i] != 0 and listnodey[i] != 0 and i != 0:
            drawnode (color, radius, (listnodex[i], listnodey[i]), i)


while running:
    pygame.display.flip()
    mousepos = pygame.mouse.get_pos()
    #pygame.display.update()
    for event in pygame.event.get():
        mods = pygame.key.get_mods()
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif pygame.key.get_pressed()[K_RSHIFT] or pygame.key.get_pressed()[K_LSHIFT]:
            #running1 = True
            mousepos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if node1 == 0:
                    nodetest = 0
                    for node in range(nnode):
                        nodetest += 1
                        x = listnodex[node]
                        y = listnodey[node]
                        mousepos = pygame.mouse.get_pos()
                        if (mousepos[0] - x)*(mousepos[0] - x) + (mousepos[1] - y)*(mousepos[1] - y) <= radius*radius:
                            node1 = nodetest - 1
                            drawnode("red",20,(x,y),node1)

                elif node2 == 0:
                    nodetest = 0
                    for node in range(nnode):
                        nodetest += 1
                        x = listnodex[node]
                        y = listnodey[node]
                        mousepos = pygame.mouse.get_pos()
                        if (mousepos[0] - x)*(mousepos[0] - x) + (mousepos[1] - y)*(mousepos[1] - y) <= radius*radius:
                            node2 = nodetest - 1
                #print(node1, node2)
                if node1 != 0 and node2 != 0:
                    drawline((0, 0, 0), node1, node2, 2)
                    node1 = 0
                    node2 = 0
                #drawnode(color, 20, (listnodex[node1], listnodey[node1]), node1)
                    #update()
                # print (listedge)
        elif pygame.key.get_pressed()[K_DELETE]:
            #running1 = True
            mousepos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if node1 == 0:
                    nodetest = 0
                    for node in range(nnode):
                        nodetest += 1
                        x = listnodex[node]
                        y = listnodey[node]
                        mousepos = pygame.mouse.get_pos()
                        if (mousepos[0] - x)*(mousepos[0] - x) + (mousepos[1] - y)*(mousepos[1] - y) <= radius*radius:
                            node1 = nodetest - 1
                            drawnode("red", 20, (x, y), node1)
                elif node2 == 0:
                    nodetest = 0
                    for node in range(nnode):
                        nodetest += 1
                        x = listnodex[node]
                        y = listnodey[node]
                        mousepos = pygame.mouse.get_pos()
                        if (mousepos[0] - x)*(mousepos[0] - x) + (mousepos[1] - y)*(mousepos[1] - y) <= radius*radius:
                            node2 = nodetest - 1
                #print(node1, node2)
                if node1 != 0 and node2 != 0 and node1 != node2:
                    drawline(background_colour, node1, node2, 4)
                    node1 = 0
                    node2 = 0
                    #update()
                # print (listedge)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # left button == 1
            if mousepos[0] < 40 and mousepos[1] < 40:
                screen.fill(background_colour)
                textsurface = myfont.render("EXIT", False, (0, 0, 0))
                screen.blit(textsurface, (5, 5))
                mousepos = pygame.mouse.get_pos()
                running5 = 1
                while running5 == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mousepos[0] < 40 and mousepos[1] < 40:
                        running5 = 0

                screen.fill(background_colour)
                textsurface = myfont.render("EXIT", False, (0, 0, 0))
                screen.blit(textsurface, (5, 5))
                '''for i in range(nnode):
                    for j in range(nnode):
                        if listedge[i][j] != 0 and i != j and i != 0 and j != 0:
                            print(listedge[i][j])
                            pygame.draw.line(screen, (0, 0, 0), (listnodex[i], listnodey[i]),(listnodex[j], listnodey[j]), 2)
                for i in range(nnode):
                    if listnodex[i] != 0 and listnodey[i] != 0 and i != 0:
                        drawnode(color, radius, (listnodex[i], listnodey[i]), i)'''
            else:
                nodetest = 0
                node1 = 0
                for node in range(nnode):
                    nodetest += 1
                    x = listnodex[node]
                    y = listnodey[node]
                    mousepos = pygame.mouse.get_pos()
                    if (mousepos[0] - x) * (mousepos[0] - x) + (mousepos[1] - y) * (mousepos[1] - y) <= 4*radius * radius+50:
                        node1 = nodetest - 1
                if node1 == 0:
                    drawnode (color, radius, mousepos, nnode)
                    nnode += 1
            #update()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: # right button == 2
            mousepos = pygame.mouse.get_pos()
            nodetest = 0
            node5 = 0
            for node in range(nnode):
                nodetest += 1
                x = listnodex[node]
                y = listnodey[node]
                mousepos = pygame.mouse.get_pos()
                if (mousepos[0] - x) * (mousepos[0] - x) + (mousepos[1] - y) * (mousepos[1] - y) <= radius * radius:
                    node5 = nodetest - 1
            if node5 != 0:
                deletenode(radius, node5)
        elif pygame.key.get_pressed()[K_BACKSPACE]:
            screen.fill(background_colour)
            listnodex = [0] * 100
            listnodey = [0] * 100
            listedge = [[0] * 100] * 100
            nnode = 1


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and mods & pygame.KMOD_CTRL:
                listedge1 = listedge
                listnodex1 = listnodex
                listnodey1 = listnodey
                #screen.fill(background_colour)
                listnodex = [0] * 100
                listnodey = [0] * 100
                listedge = [[0] * 100] * 100
                nnode1 = nnode


            elif event.key == pygame.K_o and mods & pygame.KMOD_CTRL:
                listedge = listedge1
                listnodex = listnodex1
                listnodey = listnodey1
                nnode = nnode1
                screen.fill(background_colour)
                #listedge[0][0] = 0
                for i in range(nnode):
                    for j in range(nnode):
                        if listedge[i][j] != 0 and i != j and i != 0 and j != 0:
                            print(listedge[i][j])
                            pygame.draw.line(screen, (0, 0, 0), (listnodex[i], listnodey[i]),(listnodex[j], listnodey[j]), 2)
                for i in range(nnode):
                    if listnodex[i] != 0 and listnodey[i] != 0 and i != 0:
                        drawnode(color, radius, (listnodex[i], listnodey[i]), i)
        clock.tick(60)