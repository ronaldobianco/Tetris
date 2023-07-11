import pygame
import sys
from settings import *
from grid import Grid
from blocks import *
pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game_grid = Grid()

block = LBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Screen Background
    screen.fill(DARK_BLUE)
    game_grid.draw(screen)
    block.draw(screen)
    pygame.display.update()
    clock.tick(60)