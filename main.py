import pygame,sys
from grid import Grid
from blocks import *

pygame.init()
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")
background = (44, 44, 127)
clock = pygame.time.Clock()

game_grid = Grid()
block = ZBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(background)
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)