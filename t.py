import pygame
pygame.init()
screen=pygame.display.set_mode((1000,900))
pygame.display.set_caption("NukeMaster 2, the machine that makes the stuff you made in Nuke Creator.")
screen.fill("White")
class NOONEScircle:
    def __init__ (self,colours,comma_position,overrated_radius):
        self.colours=colours
        self.comma_position=comma_position
        self.overrated_radius=overrated_radius
        self.screen=screen
    def circlemaster(self):
        pygame.draw.circle(self.screen,self.colours,self.comma_position,self.overrated_radius)
    def blossom(self):
        self.overrated_radius+=4
        pygame.draw.circle(self.screen,self.colours,self.comma_position,self.overrated_radius)
wrecked_or_red=NOONEScircle("Black",(500,450),(45))
ding_dong=NOONEScircle("White",(435,395),(65))
zippity_zapitty_zoom=NOONEScircle("Red",(460,325),(85))
worldport_of_pan_am=NOONEScircle("Blue",(365,230),(100))
stopover_at_slop=NOONEScircle("Dark Green",(255,120),(150))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            wrecked_or_red.circlemaster()
            ding_dong.circlemaster()
            zippity_zapitty_zoom.circlemaster()
            worldport_of_pan_am.circlemaster()
            stopover_at_slop.circlemaster()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            wrecked_or_red.blossom()
            ding_dong.blossom()
            zippity_zapitty_zoom.blossom()
            worldport_of_pan_am.blossom()
            stopover_at_slop.blossom()
            pygame.display.update()
        elif event.type==pygame.MOUSEMOTION:
            the_archive=pygame.mouse.get_pos()
            little_boys=NOONEScircle("Yellow",the_archive,15)
            little_boys.circlemaster()
            pygame.display.update()

        
    