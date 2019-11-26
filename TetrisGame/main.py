# @Author  : weibin Ma
# @Time    : 10/30/2019
# @title: pythonPJ
# test push
import sys
import pygame
from settings import *
from piece import Piece

def main():

    pygame.init()

    screen = pygame.display.set_mode((1200, 900) )  #resolution ratio 1200*900
    pygame.display.set_caption("TetrisGame")  #window title

#background color
    bg_color = (230, 230, 230)

#create blocks
    piece = Piece('S', screen)
#main body
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #close window
                sys.exit()   #esc  program

 #Fill in the screen background color
        screen.fill(bg_color)

        #draw the line
        draw_game_area(screen)

        #draw block with method
        piece.paint()
        #draw block
        draw_cell(screen, GAME_AREA_LEFT, GAME_AREA_TOP)
        # make draw visible
        pygame.display.flip()

# dtaw the game area
def draw_game_area(screen):
        #color(rgb), start node, end node

        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP),
                         (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP))
        # bottom
        for i in range(21):
            pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + i* CELL_WIDTH),
                         (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + i* CELL_WIDTH))
        # left
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP),
                         (GAME_AREA_LEFT, GAME_AREA_TOP + 20 * CELL_WIDTH))
        # right
        for i in range(11):
           pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT + i * CELL_WIDTH, GAME_AREA_TOP),
                         (GAME_AREA_LEFT + i * CELL_WIDTH, GAME_AREA_TOP + 20 * CELL_WIDTH))

def draw_cell(screen,left,top):
    '''
        left: the length from the window left
        top: the length from the window top
    '''
    cell_left_top = (left+ 4*CELL_WIDTH, top)  # block left top

    cell_width_height = (CELL_WIDTH, CELL_WIDTH)  # width and height of bolck

    cell_rect = pygame.Rect(cell_left_top , cell_width_height)  # draw the left-top rect

    pygame.draw.rect(screen, CELL_COLOR, cell_rect)  # draw rect

if __name__ == '__main__':
       main()