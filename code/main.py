import pygame
from playerone import Playerone
pygame.init()




#genere la fenetre du jeu
pygame.display.set_caption("notre jeu")

#définir nom et taille de la fenetre
pygame.display.set_caption("Notre jeu")
screen = pygame.display.set_mode((1350,700))

#définit don d'écran
background=pygame.image.load("assets/fond.jpg")

#charge le joueur
playerone = Playerone()

running=True

#tant que c'est vrai
while running:
    #applique fond d'ecran
    screen.blit(background,(0,0))
    #applique l'image du joueur 1
    screen.blit(playerone.image,playerone.rect) #l'image aura une position qui varie

    #mettre à jour l'écran
    pygame.display.flip()



    #si on ferme la fenetre
    for event in pygame.event.get():
        #evenement = fermeture
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("Fermeture")


        #DEFINITION DES TOUCHES
        if event.type == pygame.KEYDOWN:
            pressed[event.key] = True

            if event.key == pygame.K_l:
                playerone.move_right()
