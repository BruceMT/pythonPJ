'''
some constants
test push
'''

SCREEN_WIDTH = 1200    #width
SCREEN_HEIGHT = 900    #height
CELL_WIDTH = 40         #game area 20x10 every length is 40 pixles .
GAME_AREA_WIDTH = CELL_WIDTH * 10       #10 colums
GAME_AREA_HEIGHT = CELL_WIDTH * 20      #20 rowa
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2      #left blank
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT          #top blank
EDGE_COLOR = (0, 0, 0)          #edge color
CELL_COLOR = (100, 100, 100)    #block color
BG_COLOR = (230, 230, 230)      #background color

S_SHAPE_TEMPLATE = ['.OO.',
                    'OO..',
                    '....']

Z_SHAPE_TEMPLATE = ['OO..',
                     '.OO.',
                     '....']

I_SHAPE_TEMPLATE = ['.O..',
                     '.O..',
                     '.O..',
                     '.O..']

O_SHAPE_TEMPLATE = ['OO',
                     'OO']

J_SHAPE_TEMPLATE = ['..O.',
                     '..O.',
                     '.OO.']

L_SHAPE_TEMPLATE = ['.O..',
                     '.O..',
                     '.OO.']

T_SHAPE_TEMPLATE = ['.O..',
                     'OOO.',
                     '....']
PIECES = {'S':S_SHAPE_TEMPLATE,
          'Z':Z_SHAPE_TEMPLATE,
          'J':J_SHAPE_TEMPLATE,
          'L':L_SHAPE_TEMPLATE,
          'I':I_SHAPE_TEMPLATE,
          'O':O_SHAPE_TEMPLATE,
          'T':T_SHAPE_TEMPLATE}
