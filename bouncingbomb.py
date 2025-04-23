import pygame
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Bouncing Bomb")
how_he_made_the_bomb=pygame.draw.circle(surface=screen,color="Red",center=[100,100],radius=60)
speed=[1,1]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    how_he_made_the_bomb.move(speed)
    pygame.draw.circle(surface=screen,color="Black",center=how_he_made_the_bomb.center,radius=60)
    
    pygame.display.update()




    
