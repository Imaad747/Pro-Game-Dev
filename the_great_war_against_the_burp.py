import pygame
pygame.init()
screen=pygame.display.set_mode((1000,900))
the_health_of_the_trench=100
the_health_of_the_burp=100
trench_ammunition=[]
burp_ammunition=[]
game_over=False
winner=""
pygame.display.set_caption("The Trench Colonial Empire vs The BURP Democratic Republic - Great Brutal War")
the_trench_yellow_class_spaceship=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("yellowspaceship.png"),(50,50)),90)
the_burp_red_spaceship=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("redspaceship.png"),(50,50)),270)
the_spice_of_space=pygame.image.load("spice.png")
yellow_rect=pygame.Rect(100,450,50,50)
red_rect=pygame.Rect(800,450,50,50)
def draw():
    screen.blit(the_spice_of_space,(0,0))
    border=pygame.Rect(475,0,30,900)
    pygame.draw.rect(screen,"black",border)
    font=pygame.font.SysFont("Arial",50)
    text_trench=font.render(f"TCE Health = {the_health_of_the_trench}",True,"White")
    #create the other font for the Beautiful Underworld Republic Palace (BURP)
    text_burp=font.render(f"BURP Health = {the_health_of_the_burp}",True,"White")
    screen.blit(the_trench_yellow_class_spaceship,(yellow_rect.x,yellow_rect.y))
    screen.blit(the_burp_red_spaceship,(red_rect.x,red_rect.y))
    screen.blit(text_trench,(100.5,10))
    screen.blit(text_burp,(550,10))
    for i in trench_ammunition:
        pygame.draw.rect(screen,"Yellow",i)
    for i in burp_ammunition:
        pygame.draw.rect(screen,"Red",i)
    if game_over==True:
        global i_drink_fonta,fonta
        screen.fill("Red")
        i_drink_fonta=pygame.font.SysFont("Arial",100)
        fonta=font.render(f"The winner of the dogfight was {winner}.",True,"White")
        screen.blit(fonta,(100,250))
def movement_ye(keys_pressed):
    if keys_pressed[pygame.K_a] and yellow_rect.x > -10:
        yellow_rect.x -= 1
    if keys_pressed[pygame.K_d] and yellow_rect.x < 435:
        yellow_rect.x += 1
    if keys_pressed[pygame.K_w] and yellow_rect.y > 0:
        yellow_rect.y -= 1
    if keys_pressed[pygame.K_s] and yellow_rect.y < 910:
        yellow_rect.y += 1
def movement_hoozah(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and red_rect.x > 505:
        red_rect.x -= 1
    if keys_pressed[pygame.K_RIGHT] and red_rect.x < 950:
        red_rect.x += 1
    if keys_pressed[pygame.K_UP] and red_rect.y > 0:
        red_rect.y -= 1
    if keys_pressed[pygame.K_DOWN] and red_rect.y < 900:
        red_rect.y += 1
def bullet_move(trench_ammunition,burp_ammunition):
    global the_health_of_the_burp,the_health_of_the_trench
    for i in trench_ammunition:
        i.x+=5
        if red_rect.colliderect(i):
            the_health_of_the_burp-=10
            trench_ammunition.remove(i)
        elif i.x>1000:
            trench_ammunition.remove(i)
    for i in burp_ammunition:
        i.x-=5
        if yellow_rect.colliderect(i):
            the_health_of_the_trench-=10
            burp_ammunition.remove(i)
        elif i.x<0:
            burp_ammunition.remove(i)
def itsdone():
    global game_over,winner
    if the_health_of_the_trench==0:
        game_over=True
        winner="the BURP"
    if the_health_of_the_burp==0:
        game_over=True
        winner="the Trench/TCE"


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_t:
                t_bullet=pygame.Rect(yellow_rect.x,yellow_rect.y + 20,10,10)
                trench_ammunition.append(t_bullet)
            if event.key == pygame.K_b:
                b_bullet=pygame.Rect(red_rect.x,red_rect.y + 20,10,10)
                burp_ammunition.append(b_bullet)

    draw()
    keys_pressed = pygame.key.get_pressed()
    movement_ye(keys_pressed)
    movement_hoozah(keys_pressed)
    bullet_move(trench_ammunition,burp_ammunition)
    itsdone()
    pygame.display.update()
    
