# @Author  : weibin Ma
# @Time    : 10/30/2019
# @title: pythonPJ
# test push

from settings import *
import pygame

class Piece():
    def __init__(self, shape, screen):
            self.x = 4
            self.y = 0
            self.shape = shape
            self.turn_times = 0
            self.screen = screen
            self.is_on_bottom = False

    def paint(self):
        shape_template = PIECES[self.shape]
        shape_turn = shape_template[self.turn_times]

        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.draw_cell(self.x + c, self.y + r)

    def draw_cell(self, x, y):
        cell_position = (x * CELL_WIDTH + GAME_AREA_LEFT + 1,
                            y * CELL_WIDTH + GAME_AREA_TOP + 1)

        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(cell_position, cell_width_height)
        pygame.draw.rect(self.screen, PIECE_COLORS[self.shape], cell_rect)

    def can_move_right(self):

        shape_mtx = PIECES[self.shape][self.turn_times]
        # print(shape_mtx)
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':  # Omeans not empty
                    if self.x + c >= COLUMN_NUM - 1:
                        return False
        return True

    def can_move_down(self):

        shape_mtx = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':  # Omeans not empty
                    if self.y + r >= LINE_NUM - 1:
                        return False
        return True

    def can_move_rleft(self):

        shape_mtx = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':  # Omeans not empty
                    if self.x + c <= 0:
                        return False
        return True

    def move_down(self):
        if self.can_move_down():
            self.y += 1
        else:
            self.is_on_bottom = True

    def move_right(self):
        if self.can_move_right():
            self.x += 1

    def move_left(self):
        if self.can_move_rleft():
            self.x -= 1

    def turn(self):
        shape_list_len = len(PIECES[self.shape])
        if self.can_turn():
           self.turn_times = (self.turn_times + 1) % shape_list_len

    def can_turn(self):
        shape_list_len = len(PIECES[self.shape])
        turn_times = (self.turn_times + 1) % shape_list_len
        shape_mtx = PIECES[self.shape][turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if (self.x + c < 0 or self.x + c >= COLUMN_NUM) or (self.y + r < 0 or self.y + r >= LINE_NUM):
                        return False
        return True

    def move_down(self):
        if self.can_move_down():
            self.y += 1
        else:
            self.is_on_bottom = True



    def fall_down(self):

        while not self.is_on_bottom:
            self.move_down()