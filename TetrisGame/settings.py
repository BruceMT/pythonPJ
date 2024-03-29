'''
some constants
test push
'''

SCREEN_WIDTH = 1200    #width
SCREEN_HEIGHT = 900    #height
CELL_WIDTH = 40         #game area 20x10 every length is 40 pixles .
LINE_NUM = 20           #game area have 20 rows
COLUMN_NUM = 10         #game area have 10 column
GAME_AREA_WIDTH = CELL_WIDTH * 10       #10 blocks
GAME_AREA_HEIGHT = CELL_WIDTH * 20      #20 rowa
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2      #left blank
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT  -50        #top blank
EDGE_COLOR = (0, 0, 0)          #edge color
CELL_COLOR = (100, 100, 100)    #block color
BG_COLOR = (230, 230, 230)      #background color
WALL_BLANK_LABEL = '-'
TIMER_INTERVAL = 1000
SCORE_LABEL_COLOR = (255, 255, 255)
SCORE_COLOR = (200, 0, 0)
EDGE_WIDTH = 5 #hint block width
MARGIN_WIDTH = 40 #distance between hint area and game area

TITLE_COLOR = (0, 0, 0)
HANZI_COLOR = (255, 255, 255)
PIECE_TYPES = ['S', 'Z', 'J', 'L', 'I', 'O', 'T']
PIECE_COLORS = {
    'S': (0, 255, 128),
    'Z': (255, 128, 255),
    'J': (41, 23, 91),
    'L': (0, 0, 255),
    'I': (50, 100, 50),
    'O': (190, 0, 90),
    'T': (255, 128, 0)
}

S_SHAPE_TEMPLATE = [['.OO.',
                    'OO..',
                    '....'],
                    ['.O..',
                     '.OO.',
                     '..O.']]

Z_SHAPE_TEMPLATE = [['OO..',
                     '.OO.',
                     '....'],
                    ['..O.',
                     '.OO.',
                     '.O..']]

I_SHAPE_TEMPLATE = [['.O..',
                     '.O..',
                     '.O..',
                     '.O..'],
                    ['....',
                     'OOOO',
                     '....',
                     '....']]

O_SHAPE_TEMPLATE = [['OO',
                    'OO']]

J_SHAPE_TEMPLATE = [['.O.',
                     '.O.',
                     'OO.'],
                    ['O..',
                     'OOO',
                     '....'],
                    ['OO.',
                     'O..',
                     'O..'],
                    ['OOO',
                     '..O',
                     '...']]
L_SHAPE_TEMPLATE = [['O..',
                     'O..',
                     'OO.'],
                    ['OOO',
                     'O..',
                     '...'],
                    ['OO.',
                     '.O.',
                     '.O.'],
                    ['..O',
                     'OOO',
                     '...']]

T_SHAPE_TEMPLATE = [['.O.',
                     'OOO',
                     '...'],
                    ['.O.',
                     '.OO',
                     '.O.'],
                    ['OOO',
                     '.O.',
                     '...'],
                    ['..O',
                     '.OO',
                     '..O']]
PIECES = {'S':S_SHAPE_TEMPLATE,
          'Z':Z_SHAPE_TEMPLATE,
          'J':J_SHAPE_TEMPLATE,
          'L':L_SHAPE_TEMPLATE,
          'I':I_SHAPE_TEMPLATE,
          'O':O_SHAPE_TEMPLATE,
          'T':T_SHAPE_TEMPLATE}
