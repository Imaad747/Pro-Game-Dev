import pygame
pygame.init()
pygame.display.set_caption("USA rocket filled with Keyhole satellites waiting to watch you >:)")
screen=pygame.display.set_mode((1000,900))
class KeyholeAndCORONA(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image=pygame.image.load("saturn_v.png")
        self.rect=self.image.get_rect()
sprites=pygame.sprite.Group()
rocket=KeyholeAndCORONA()
sprites.add(rocket)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.blit(pygame.image.load("starswow.png"),(0,0))
    sprites.draw(screen)
    pygame.display.update()
