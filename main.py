import pygame,sys

pygame.init()
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris")
background = (22,20,78)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(background)
    pygame.display.update()
    clock.tick(60)