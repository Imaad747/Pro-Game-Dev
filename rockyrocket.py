import pygame
pygame.init()
pygame.display.set_caption("USA rocket filled with Keyhole satellites waiting to watch you >:)")
screen=pygame.display.set_mode((1000,900))
class KeyholeAndCORONA(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image=pygame.image.load("saturn_v.png")
        self.rect=self.image.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
    
sprites=pygame.sprite.Group()
rocket=KeyholeAndCORONA()
sprites.add(rocket)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.blit(pygame.image.load("starswow.png"),(100,100))
    sprites.draw(screen)
    oppressed_keys=pygame.key.get_pressed()
    rocket.update(oppressed_keys)
    pygame.display.update()
