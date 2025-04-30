import pygame
pygame.init()
screen=pygame.display.set_mode((1200,800))
pygame.display.set_caption("Bouncing Bomb")
#image=pygame.draw.circle(surface=screen,color="Red",center=[100,100],radius=60)
image=pygame.transform.scale(pygame.image.load("boingball.png"),(160,160))
the_invisible_force=pygame.Rect(0,0,80,80)
speed=[1.5,1.5]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill("Black")
    screen.blit(image,(the_invisible_force.x,the_invisible_force.y))
    the_invisible_force=the_invisible_force.move(speed)
    if the_invisible_force.left<0 or the_invisible_force.right>1200:
        speed[0]=-speed[0]
    if the_invisible_force.top<0 or the_invisible_force.bottom>800:
        speed[1]=-speed[1]


    #pygame.draw.circle(surface=screen,color="Red",center=the_invisible_force.center,radius=60)

    
    pygame.display.update()




    
