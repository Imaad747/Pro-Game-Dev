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
pipe_passed=False
score=0
font=pygame.font.SysFont("Arial",50)
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
        if self.rect.right<0:
            self.kill()

sewage_system=pygame.sprite.Group()

class Button(pygame.sprite.Sprite):
    def __init__ (self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("C:\\Users\\imaad\\OneDrive\\Desktop\\Pro Game Dev\\flappy bird images\\restart-button.png")
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def draw(self):
        action=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                action=True
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action
buttaton=Button(432,450)

    

while True:
    clock.tick(100000000)
    screen.blit(city,(0,0))
    sewage_system.draw(screen)
    screen.blit(les_grass,(ground_scroll,732))
    birb_goop.draw(screen)
    birb_goop.update()

    if len(sewage_system)>0:
        if birb_goop.sprites()[0].rect.left>sewage_system.sprites()[0].rect.left\
            and birb_goop.sprites()[0].rect.right<sewage_system.sprites()[0].rect.right\
            and pipe_passed==False:
            pipe_passed=True
        if pipe_passed==True:
            if birb_goop.sprites()[0].rect.left>sewage_system.sprites()[0].rect.right:
                score+=1
                pipe_passed=False
    numnum=font.render(f"Score: {score}",True,"White")
    screen.blit(numnum,(432,50))
    if pygame.sprite.groupcollide(birb_goop,sewage_system,False,False):
        game_over=True
    if game_over==True:
        if buttaton.draw():
            game_over=False
            borb.rect.x=50
            borb.rect.y=350
            score=0
            sewage_system.empty()
    
            
                

            
            



    
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
    
