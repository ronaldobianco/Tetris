import pygame
import sys
from settings import *
pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Screen Background
    screen.fill(DARK_BLUE)
    pygame.display.update()
    clock.tick(60)