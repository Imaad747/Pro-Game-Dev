import pygame
import random
pygame.init()
screen=pygame.display.set_mode((1000,900))
colourpedia=["Red","Yellow","Orange","Green","White","Black","Purple","Dark Green","Pink","Blue","chocolate4"]
pygame.display.set_caption("3000 BC best quality painter - for the exotic egyptians, the indus peaceful guys, the greeeks of the island of con-crete, and the mesopotatoans")
thecraftsofmesopotatoes=False
egyptiansarchivesofthesacredpaintingposition=None
colourrecords="Black"
screen.fill("White")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                thecraftsofmesopotatoes=True
                egyptiansarchivesofthesacredpaintingposition=event.pos
                pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                thecraftsofmesopotatoes=False
                pygame.display.update()
        elif event.type==pygame.MOUSEMOTION:
            if thecraftsofmesopotatoes:
                greeksarchivesofthepositionofconcrete=event.pos
                pygame.draw.line(screen,colourrecords,egyptiansarchivesofthesacredpaintingposition,greeksarchivesofthepositionofconcrete)
                egyptiansarchivesofthesacredpaintingposition=greeksarchivesofthepositionofconcrete

                pygame.display.update()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_c:
                colourrecords=random.choice(colourpedia)
                pygame.display.update()

pygame.display.update()



            
