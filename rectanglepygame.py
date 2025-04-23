import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
class rectangle_maker:
    def __init__ (self,colour,size):
        self.screen=screen
        self.colour=colour
        self.size=size
    def paint(self):
        self.draw_rect=pygame.draw.rect(self.screen,self.colour,self.size)
purchasingpowerofrectanglemoney=rectangle_maker("Red",(100,100,50,50))
rectanglemoneyglitchdetected=rectangle_maker("Blue",(200,200,70,70))
the_king_of_the_rectangles=rectangle_maker("Gold",(350,350,100,100))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    screen.fill("White")
    purchasingpowerofrectanglemoney.paint()
    rectanglemoneyglitchdetected.paint()
    the_king_of_the_rectangles.paint()






    pygame.display.update()