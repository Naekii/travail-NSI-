import pygame
class Playerone(pygame.sprite.Sprite):
    #la classe sprite est la classe de base de tous les éléments visibles du jeu, elle va nous permettre
    # de mettre à jour l'écran, de déplacer l'objet en question, lui assigner une image...
       def __init__(self):
           super().__init__()
           #initialise la classe sprite
           self.velocity_x = 20
           self.image=pygame.image.load("assets/perso2.png")
           self.rect=self.image.get_rect()   #récupère la position de l'image
        #on définie la position initiale du joueur
           self.rect.x=500
           self.rect.y=500

        # attribue les images du pero en fonction de sa direction
       def move_right(self):


            self.rect.x += self.velocity_x