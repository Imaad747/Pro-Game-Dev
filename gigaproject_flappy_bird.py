import pygame
pygame.init()
screen=pygame.display.set_mode((864,900))
import random
pygame.display.set_caption("Flappy Bird")
city=pygame.image.load("C:\\Users\\imaad\\OneDrive\\Desktop\\Pro Game Dev\\flappy bird images\\background.png")
les_grass=pygame.image.load("C:\\Users\\imaad\\OneDrive\\Desktop\\Pro Game Dev\\flappy bird images\\grass.png")
flying_checks=False
ground_scroll=0

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
    def update(self):
        if flying_checks==True:
            self.velocity+=0.5
            if self.rect.bottom<732:
                self.rect.y+=self.velocity

birb_goop=pygame.sprite.Group()
borb=birb(50,350)
birb_goop.add(borb)



while True:
    screen.blit(city,(0,0))
    screen.blit(les_grass,(ground_scroll,732))
    birb_goop.draw(screen)
    birb_goop.update()

    ground_scroll-=4
    if ground_scroll<-36:
        ground_scroll=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and flying_checks==False:
            flying_checks=True
    pygame.display.update()
    
