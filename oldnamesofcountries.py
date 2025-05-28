import pygame
pygame.init()
screen=pygame.display.set_mode((1000,900))
pygame.display.set_caption("Old country names match game! Match old country names with their modern flags!")
screen.fill("White")
ceylon_didnt_last_long=pygame.transform.scale(pygame.image.load("Ceylon.png"),(200,160))
persia_like_iran_ran_too_fast=pygame.transform.scale(pygame.image.load("Persia.png"),(200,160))
burma_got_hit_in_the_bum=pygame.transform.scale(pygame.image.load("Burma.png"),(200,160))
rhodesia_became_a_mess=pygame.transform.scale(pygame.image.load("Rhodesia.png"),(200,160))
screen.blit(ceylon_didnt_last_long,(100,50))
screen.blit(persia_like_iran_ran_too_fast,(100,260))
screen.blit(burma_got_hit_in_the_bum,(100,470))
screen.blit(rhodesia_became_a_mess,(100,680))
senwadedede=pygame.font.SysFont("Times New Roman",72)
textforceylon=senwadedede.render("Ceylon",True,(0,0,0))
screen.blit(textforceylon,(600,100))
textforpersia=senwadedede.render("Persia",True,(0,0,0))
screen.blit(textforpersia,(600,730))
textforburma=senwadedede.render("Burma",True,(0,0,0))
screen.blit(textforburma,(600,520))
textforrhodesia=senwadedede.render("Rhodesia",True,(0,0,0))
screen.blit(textforrhodesia,(600,310))





while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousegotcaughtbycat=pygame.mouse.get_pos()
            pygame.draw.circle(screen,"Black",mousegotcaughtbycat,10,0)
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            pull_up_terrain=pygame.mouse.get_pos()
            pygame.draw.circle(screen,"Black",pull_up_terrain,10,0)
            pygame.draw.line(screen,"Black",mousegotcaughtbycat,pull_up_terrain,3)
            pygame.display.update()

    pygame.display.update()