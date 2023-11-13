import pygame,sys
from grid import Grid

pygame.init()
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")
background = (27, 24, 17)
clock = pygame.time.Clock()

game_grid = Grid()
game_grid.print_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(background)
    game_grid.draw(screen)
    pygame.display.update()
    clock.tick(60)