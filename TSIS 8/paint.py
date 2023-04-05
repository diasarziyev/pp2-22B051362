import pygame
pygame.init()
BLUE = (0,0,255)
screen = pygame.display.set_mode((600,400))
run = True 
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()