import os, sys
import pygame
from testlog import Logger

pygame.init()
width = 450
height = 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hello')
BLACK = (255,255,255)
start = (10,10)
end = (300,300)
thickness = 2
# def gLine(screen, BLACK, start, end, thickness):
#     return pygame.draw.line(screen, BLACK, start, end, thickness)
GREY = (100,100,100)
while True:
    screen.fill((100,100,100))
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos1 = pygame.mouse.get_pos()
        
        pygame.draw.line(screen, BLACK, pos1, end, thickness)
        pygame.display.flip()

pygame.quit()

# def gLine(surface, color, start, end, thickness):
#     return pygame.draw.line(surface, color, start, end, thickness)

# def gCircle():
#     pass