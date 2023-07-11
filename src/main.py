import pygame,sys
from settings import *
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.SysFont("Roboto", 40)

score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Game Over", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

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
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.gameover == False:
                game.rotate()
        
        if event.type == GAME_UPDATE and game.gameover == False:
            game.move_down()

    #Screen Background
    screen.fill(Colors.dark_blue)

    #Score and Next
    score_surface_value = title_font.render(str(game.score), True, Colors.white)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (365, 180, 50, 50))

    #Game Over
    if game.gameover == True:    
        screen.blit(game_over_surface, (320, 450, 50, 50))
    
    #Draw Rectangles
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_surface_value, score_surface_value.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    
    #Draw Grid
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)