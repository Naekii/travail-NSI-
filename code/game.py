import pygame
#import du composant
from playerone import Playerone
#création de la classe représentant le jeu
class Game(pygame.sprite.Sprite):
    def init(self):
        super().init()
        #genere le joueur
        self.playerone=Playerone()
        #touche appuyée, le dictionnaire associe une une touche à
        self.touche_appuyee={}
