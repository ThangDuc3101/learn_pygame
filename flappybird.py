import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 400,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Flappy Bird')
running = True

# Khoi tao mau
GREEN = (0,200,0)
BLUE = (0,0,200)
RED = (200,0,0)
BLACK = (0,0,0)

# Tham so cua ong
TUBE_WIDTH = 50
TUBE_VELOCITY = 3
TUBE_GAP = 150

tube1_x = 0
tube2_x = 200
tube3_x = 400

tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

# Tham so cua chim
BIRD_X = 50
bird_y = 400
BIRD_WIDTH = 35
BIRD_HEIGHT = 35

drop_velocity = 0
GRAVITY = 0.5

# Tham so tinh diem
score = 0
font = pygame.font.SysFont('sans',20)

tube1_pass = False
tube2_pass = False
tube3_pass = False

# Khoi tao dong ho
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(GREEN)
    
    # Ve ong
    pygame.draw.rect(screen, BLUE, (tube1_x,0,TUBE_WIDTH,tube1_height))
    pygame.draw.rect(screen, BLUE, (tube2_x,0,TUBE_WIDTH,tube2_height))
    pygame.draw.rect(screen, BLUE, (tube3_x,0,TUBE_WIDTH,tube3_height))
    
    # Di chuyen ong sang trai
    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY
    
    # Ve ong doi dien
    pygame.draw.rect(screen, BLUE, (tube1_x,tube1_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube1_height-TUBE_GAP))
    pygame.draw.rect(screen, BLUE, (tube2_x,tube2_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube2_height-TUBE_GAP))
    pygame.draw.rect(screen, BLUE, (tube3_x,tube3_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube3_height-TUBE_GAP))
    
    # Ve chu
    score_txt = font.render("Score: "+str(score),True,BLACK)
    screen.blit(score_txt,(5,5))
    
    # Ve chim
    pygame.draw.rect(screen, RED, (BIRD_X,bird_y,BIRD_WIDTH,BIRD_HEIGHT))
    
    # Tao ong moi
    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100,400)
        tube1_pass = False
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(100,400)
        tube2_pass = False
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100,400)  
        tube3_pass = False  
    
    # Chim roi
    bird_y += drop_velocity
    drop_velocity += GRAVITY
    
    # Cap nhat diem
    if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
        score += 1
        tube1_pass = True
    if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
        score += 1
        tube2_pass = True
    if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
        score += 1
        tube3_pass = True    
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:            
            # Nhan nut SPACE => di chuyen chim đi len
            if event.key == pygame.K_SPACE:
                drop_velocity = 0
                drop_velocity -= 10
    pygame.display.flip()   

pygame.quit()            