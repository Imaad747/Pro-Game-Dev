import pygame
pygame.init()
screen=pygame.display.set_mode((864,900))
import random
pygame.display.set_caption("Flappy Bird")
city=pygame.image.load("C:\\Users\\imaad\\OneDrive\\Desktop\\Pro Game Dev\\flappy bird images\\background.png")
les_grass=pygame.image.load("C:\\Users\\imaad\\OneDrive\\Desktop\\Pro Game Dev\\flappy bird images\\grass.png")
flying_checks=False
ground_scroll=0
game_over=False
time_between_pipes_moving=1500
pipe_gap=150
last_pipe_generated=pygame.time.get_ticks()-time_between_pipes_moving
clock=pygame.time.Clock()

class birb(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        for i in range (1,4):
            img=pygame.image.load(f"C:\\Users\\imaad\\OneDrive\\Desktop\\Pro Game Dev\\flappy bird images\\flappy-{i}.png")
            self.images.append(img)
        self.index=0
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=x,y
        self.velocity=0
        self.counter=0
    def update(self):
        if flying_checks==True:
            self.velocity+=0.5
            if self.rect.bottom<732:
                self.rect.y+=self.velocity
        if game_over==False:
            if pygame.mouse.get_pressed()[0]==1:
                self.velocity=-8
            self.counter+=1
            if self.counter>5:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
                self.image=self.images[self.index]
            
                
            
            #elif pygame.mouse.get_pressed()[0]==0:
            



    

birb_goop=pygame.sprite.Group()
borb=birb(50,350)
birb_goop.add(borb)

class Pipe(pygame.sprite.Sprite):
    def __init__ (self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("C:\\Users\\imaad\\OneDrive\\Desktop\\Pro Game Dev\\flappy bird images\\pipes.png")
        self.rect=self.image.get_rect()
        if pos==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-75]
        elif pos==-1:
            self.rect.topleft=[x,y+75]
    def update(self):
        self.rect.x-=10
        if self.rect.x<0:
            self.kill()

sewage_system=pygame.sprite.Group()

while True:
    clock.tick(60)
    screen.blit(city,(0,0))
    sewage_system.draw(screen)
    screen.blit(les_grass,(ground_scroll,732))
    birb_goop.draw(screen)
    birb_goop.update()

    
    if flying_checks==True and game_over==False:
        time_now=pygame.time.get_ticks()
        if time_now-last_pipe_generated>time_between_pipes_moving:
            random_height=random.randint(-100,100)
            bot_pipe=Pipe(864,450+random_height,-1)
            tiptop_pipe=Pipe(864,450+random_height,1)
            sewage_system.add(bot_pipe)
            sewage_system.add(tiptop_pipe)
            last_pipe_generated=time_now
        sewage_system.update()

        ground_scroll-=4
        if ground_scroll<-36:
            ground_scroll=0

    if borb.rect.bottom>=732:
        game_over=True
        flying_checks=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and flying_checks==False:
            flying_checks=True
    pygame.display.update()
    
