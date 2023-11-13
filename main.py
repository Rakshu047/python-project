import pygame,sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None,40)
scorecard = title_font.render('Score',True, Colors.white)
score_rect = pygame.Rect(330,50,150,70)
next_block = title_font.render('Next Block',True, Colors.white)
next_rect = pygame.Rect(330,215,150,160)
game_over_surface = title_font.render('GAME OVER',True, Colors.white)

screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.block_fits() == True:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.block_fits() == True:
                game.move_right()
            if event.key == pygame.K_DOWN and game.block_fits() == True:
                game.move_down()
            if event.key == pygame.K_UP and game.block_fits() == True:
                game.rotate()
        if event.type == GAME_UPDATE and game.block_fits() == True:
            game.move_down()
    
    score_value_surface = title_font.render(str(game.score),True,Colors.white)

    screen.fill(Colors.background)
    screen.blit(scorecard,(365,20,50,50))
    pygame.draw.rect(screen,Colors.light_blue,score_rect,0,5)

    screen.blit(score_value_surface,score_value_surface.get_rect(centerx=score_rect.centerx,centery=score_rect.centery))
    screen.blit(next_block,(340,170,50,50))
    pygame.draw.rect(screen,Colors.light_blue,next_rect,0,5)
    if game.game_over == True:
        screen.blit(game_over_surface,(325,450,50,50))
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)