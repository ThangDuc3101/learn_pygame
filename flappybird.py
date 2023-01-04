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
YELLOW = (200,200,0)

# Tham so cua ong
TUBE_WIDTH = 50
TUBE_VELOCITY = 3
TUBE_GAP = 170

tube1_x = 500
tube2_x = 750
tube3_x = 1000

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

# Hinh chim
bird_image = pygame.image.load("redbird.png")
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH,BIRD_HEIGHT))

# Tham so tinh diem
score = 0
font = pygame.font.SysFont('sans',20)

tube1_pass = False
tube2_pass = False
tube3_pass = False

pausing = False

# Hinh nen
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (WIDTH,HEIGHT))

# Khoi tao dong ho
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(GREEN)
    screen.blit(background_image, (0,0))
    
    # Ve ong
    tube1_rect = pygame.draw.rect(screen, BLUE, (tube1_x,0,TUBE_WIDTH,tube1_height))
    tube2_rect = pygame.draw.rect(screen, BLUE, (tube2_x,0,TUBE_WIDTH,tube2_height))
    tube3_rect = pygame.draw.rect(screen, BLUE, (tube3_x,0,TUBE_WIDTH,tube3_height))
        
    # Di chuyen ong sang trai
    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY
    
    # Ve ong doi dien
    tube1_rect_inv = pygame.draw.rect(screen, BLUE, (tube1_x,tube1_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube1_height-TUBE_GAP))
    tube2_rect_inv = pygame.draw.rect(screen, BLUE, (tube2_x,tube2_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube2_height-TUBE_GAP))
    tube3_rect_inv = pygame.draw.rect(screen, BLUE, (tube3_x,tube3_height+TUBE_GAP,TUBE_WIDTH,HEIGHT-tube3_height-TUBE_GAP))
    
    # Ve chu
    score_txt = font.render("Score: "+str(score),True,BLACK)
    screen.blit(score_txt,(5,5))
    
    # Ve chim
    # bird_rect = pygame.draw.rect(screen, RED, (BIRD_X,bird_y,BIRD_WIDTH,BIRD_HEIGHT))
    bird_rect = screen.blit(bird_image,(BIRD_X,bird_y))
    # Ve cat
    sand_rect = pygame.draw.rect(screen, YELLOW, (0,580,400,20))
    
    # Tao ong moi
    if tube1_x < -TUBE_WIDTH:
        tube1_x = 650
        tube1_height = randint(100,400)
        tube1_pass = False
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 650
        tube2_height = randint(100,400)
        tube2_pass = False
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 650
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
    
    # Kiem tra va cham
    for tube in [tube1_rect,tube2_rect,tube3_rect,tube1_rect_inv,tube2_rect_inv,tube3_rect_inv,sand_rect]:
        if bird_rect.colliderect(tube):
            TUBE_VELOCITY = 0
            drop_velocity = 0
            pausing = True
            
            game_over_msg = font.render("Game over",True,BLACK)            
            your_score_msg = font.render("Your score:"+str(score),True,BLACK)
            continue_msg = font.render("Press SPACE to continue",True,BLACK)
            
            screen.blit(game_over_msg,(150,300))
            screen.blit(your_score_msg,(150,350))
            screen.blit(continue_msg,(150,400))
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_SPACE:
                 # Nhan nut SPACE => reset
                if pausing:
                    drop_velocity=0
                    TUBE_VELOCITY=3
                    BIRD_X = 50
                    bird_y = 400
                    tube1_x = 400
                    tube2_x = 600
                    tube3_x = 800
                    score = 0
                    pausing = False
                
            # Nhan nut SPACE => di chuyen chim đi len
                drop_velocity = 0
                drop_velocity -= 10
    pygame.display.flip()   

pygame.quit()            