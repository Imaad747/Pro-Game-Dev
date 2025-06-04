import pygame
import random
pygame.init()
screen=pygame.display.set_mode((1000,900))
class crude_oil(pygame.sprite.Sprite):
    def __init__(self,colour):
        super().__init__()
        self.image=pygame.Surface((10,10))
        self.image.fill(colour)
        self.rect=self.image.get_rect()
        self.pos()
    def pos(self):
        self.rect.x=random.randint(0,1000)
        self.rect.y=random.randint(-300,-20)
    def update(self):
        self.rect.y+=5
        if self.rect.y>900:
            self.pos()
oil_resevoir=pygame.sprite.Group()
for i in range(50):
    shocking_discovery=crude_oil("Black")
    oil_resevoir.add(shocking_discovery)
clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill("darkgoldenrod1")
    oil_resevoir.update()
    oil_resevoir.draw(screen)
    clock.tick(120)
    pygame.display.update()


    
