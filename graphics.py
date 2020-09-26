import os, sys
import pygame
from testlog import Logger
import constants

pygame.init()
width = 450
height = 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Painter demo')
BLACK = (255,255,255)
start = (10,10)
end = (300,300)
thickness = 2

mousePos = []

def gLine(surface, color, start, end, thickness):
    return pygame.draw.line(surface, color, start, end, thickness)
GREY = (100,100,100)
screen.fill((100,100,100))
count = 0

while True:
    pygame.time.Clock().tick(100)
    screen.fill((100,100,100))
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    sys.exit()

    start_pos = pygame.mouse.get_pos()

    if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONUP:
        if count % 2 == 1:
            end_pos = event.pos
            pygame.draw.line(screen, (255, 255, 255), start_pos, end_pos, 1)

  
    pygame.display.flip()
print(mousePos)
pygame.quit()