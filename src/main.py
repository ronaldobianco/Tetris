import pygame,sys
from settings import *
from game import Game
pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.gameover == True:
                game.gameover = False
                game.reset()
            if event.key == pygame.K_LEFT and game.gameover == False:
                game.move_left()    
            if event.key == pygame.K_RIGHT and game.gameover == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.gameover == False:
                game.move_down()
            if event.key == pygame.K_UP and game.gameover == False:
                game.rotate()
        
        if event.type == GAME_UPDATE and game.gameover == False:
            game.move_down()

    #Screen Background
    screen.fill(DARK_BLUE)

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)