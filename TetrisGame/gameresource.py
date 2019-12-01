# @Author  : weibin Ma
# @Time    : 12/01/2019
# @title: pythonPJ
# @ some resource for the game
import pygame
class GameResource():
    def __init__(self):
        self.img_path = 'images/'
        self.newgame_img = None
        self.pausing_img = None
        self.continue_img = None
        self.gameover_img = None

    def load_newgame_img(self):
        if not self.newgame_img:
            self.newgame_img = pygame.image.load(self.img_path + "start3.png").convert_alpha()
        return self.newgame_img

    def load_pausing_img(self):
        if not self.pausing_img:
            self.pausing_img = pygame.image.load(self.img_path + "pause.png").convert_alpha()
        return self.pausing_img

    def load_continue_img(self):

        if not self.continue_img:
            self.continue_img = pygame.image.load(self.img_path + "press-p-continue.png").convert_alpha()
        return self.continue_img

    def load_gameover_img(self):
        if not self.gameover_img:
            self.gameover_img = pygame.image.load(self.img_path + "over1.png").convert_alpha()

        return self.gameover_img