import pygame
pygame.init()
screen=pygame.display.set_mode((1000,900))
pygame.display.set_caption("The Trench Colonial Empire vs The BURP Democratic Republic - Great Brutal War")
the_trench_yellow_class_spaceship=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("yellowspaceship.png"),(50,50)),90)
the_burp_red_spaceship=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("redspaceship.png"),(50,50)),270)
the_spice_of_space=pygame.image.load("spice.png")
yellow_rect=pygame.Rect(100,450,50,50)
red_rect=pygame.Rect(800,450,50,50)
def draw():
    screen.blit(the_spice_of_space,(0,0))
    screen.blit(the_trench_yellow_class_spaceship,(yellow_rect.x,yellow_rect.y))
    screen.blit(the_burp_red_spaceship,(red_rect.x,red_rect.y))
    border=pygame.Rect(475,0,30,900)
    pygame.draw.rect(screen,"black",border)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    draw()
    pygame.display.update()
    
