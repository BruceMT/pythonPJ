# @Author  : weibin Ma
# @Time    : 11/30/2019
# @title: pythonPJ
#

from settings import *
from gamedisplay import GameDisplay
class GameWall():

    def __init__(self, screen):
        '''when game begin,the game area fill with '-' '''
        self.screen = screen
        self.area = [ ]
        line = [WALL_BLANK_LABEL] * COLUMN_NUM
        for i in range(LINE_NUM):
            self.area.append(line[:])


    def print(self):
        '''print for test'''
        print(len(self.area), "rows", len(self.area[0]), "colums")
        for line in self.area:
            print(line)



    def set_cell(self, row,column, shape_label):

        self.area[row][column] = shape_label

    def add_to_wall(self, piece):
        '''add block to wall'''
        shape_turn = PIECES[piece.shape][piece.turn_times]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.set_cell(piece.y + r, piece.x + c, piece.shape)

    def is_wall(self, row, column):
        return self.area[row][column] != WALL_BLANK_LABEL


    def eliminate_lines(self):
        '''score when line elimination'''
        '''
        rule：
        eliminate 0 row：0
        eliminate 1 row：100
        eliminate 2 row：200
        eliminate 3 row：400
        eliminate 4 row：800
        '''
        # which eow need to elimination
        lines_eliminated = []
        for r in range(LINE_NUM):
            if self.is_full(r):
                lines_eliminated.append(r)

        # line elimination，and renew the wall matrix
        for r in lines_eliminated:
            self.copy_down(r)  # line r elimination，pull down the rest row
            for c in range(COLUMN_NUM):
                self.area[0][c] = WALL_BLANK_LABEL

        # get score
        eliminated_num = len(lines_eliminated)
        assert (eliminated_num <= 4 and eliminated_num >= 0)
        if eliminated_num < 3:
            score = eliminated_num * 100
        elif eliminated_num == 3:
            score = 400
        else:
            score = 800
        return score

    def is_full(self, row):
        #row full
        for c in range(COLUMN_NUM):
            if self.area[row][c] == WALL_BLANK_LABEL:
                return False

        return True

    def copy_down(self, row):
        # down rows
        for r in range(row, 0, -1):
            for c in range(COLUMN_NUM):
                self.area[r][c] = self.area[r - 1][c]

