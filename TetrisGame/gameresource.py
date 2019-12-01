# @Author  : weibin Ma
# @Time    : 12/01/2019
# @title: pythonPJ
# @ some resource for the game
import pygame
class GameResource():
    def __init__(self):
           self.img_path = 'images/'
           self.newgame_img = None

    def load_newgame_img(self):
           if not self.newgame_img:
            self.newgame_img = pygame.image.load(self.img_path + "start3.png").convert_alpha()
           return self.newgame_img