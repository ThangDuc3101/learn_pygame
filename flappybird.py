import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 400,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Flappy Bird')
running = True

GREEN = (0,200,0)
BLUE = (0,0,200)

TUBE_WIDTH = 50
TUBE_VELOCITY = 3
TUBE_GAP = 150

tube1_x = 0
tube2_x = 200
tube3_x = 400

tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(GREEN)
    
    pygame.draw.rect(screen, BLUE, (tube1_x,0,TUBE_WIDTH,tube1_height))
    pygame.draw.rect(screen, BLUE, (tube2_x,0,TUBE_WIDTH,tube2_height))
    pygame.draw.rect(screen, BLUE, (tube3_x,0,TUBE_WIDTH,tube3_height))
    
    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY
    
    pygame.draw.rect(screen, BLUE, (tube1_x,tube1_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube1_height-TUBE_GAP))
    pygame.draw.rect(screen, BLUE, (tube2_x,tube2_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube2_height-TUBE_GAP))
    pygame.draw.rect(screen, BLUE, (tube3_x,tube3_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube3_height-TUBE_GAP))
    
    if tube1_x < - TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100,400)
    if tube2_x < - TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(100,400)
    if tube3_x < - TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100,400)    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.flip()   

pygame.quit()            