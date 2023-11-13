import pygame,sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")
background = (44, 44, 127)
clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()
    
    screen.fill(background)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)