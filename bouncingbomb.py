import pygame
pygame.init()
screen=pygame.display.set_mode((1200,800))
pygame.display.set_caption("Bouncing Bomb")
how_he_made_the_bomb=pygame.draw.circle(surface=screen,color="Red",center=[100,100],radius=60)
speed=[1,1]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill("Black")
    how_he_made_the_bomb=how_he_made_the_bomb.move(speed)
    if how_he_made_the_bomb.left<0 or how_he_made_the_bomb.right>1200:
        speed[0]=-speed[0]
    if how_he_made_the_bomb.top<0 or how_he_made_the_bomb.bottom>800:
        speed[1]=-speed[1]


    pygame.draw.circle(surface=screen,color="Red",center=how_he_made_the_bomb.center,radius=60)
    
    pygame.display.update()




    
