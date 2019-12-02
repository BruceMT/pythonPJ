# @Author  : weibin Ma
# @Time    : 11/30/2019
# @title: pythonPJ
#
from settings import *

import pygame

class GameDisplay():
    @staticmethod
    def draw_cell(screen, row, column, color):

        cell_position = (column* CELL_WIDTH + GAME_AREA_LEFT + 1,
                             row* CELL_WIDTH + GAME_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(cell_position, cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)

    @staticmethod
    def draw_cell_rect(screen, left_top_anchor, color):
        left_top_anchor = (left_top_anchor[0] + 1, left_top_anchor[1] + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(left_top_anchor, cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)

    @staticmethod
    def draw_game_area(screen, game_state, game_resource):

        #for r in range(21):
        #       pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + r * CELL_WIDTH),
        #                        (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + r * CELL_WIDTH))
        #for c in range(11):
        #       pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP),
        #                       (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))

        #draw  boundary
        GameDisplay.draw_border(screen, GAME_AREA_LEFT - EDGE_WIDTH, GAME_AREA_TOP, LINE_NUM, COLUMN_NUM)
        GameDisplay.draw_wall(game_state.wall)
        GameDisplay.draw_score(screen, game_state.game_score)

        if game_state.stopped:
            if game_state.session_count > 0:
                GameDisplay.draw_game_over(screen, game_resource)
            GameDisplay.draw_start_prompt(screen, game_resource)
            GameDisplay.draw_title_prompt(screen, game_resource)
        if game_state.paused:
            GameDisplay.draw_pause_prompt(screen, game_resource)
        GameDisplay.draw_next_piece(screen, game_state.next_piece)
        GameDisplay.draw_mannual(screen)

    @staticmethod
    def draw_wall(game_wall):
        '''draw wall'''
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if game_wall.area[r][c] != WALL_BLANK_LABEL:
                    GameDisplay.draw_cell(game_wall.screen, r, c, PIECE_COLORS[game_wall.area[r][c]])

    @staticmethod
    def draw_score(screen, score):
        #draw the score
        score_label_font = pygame.font.SysFont('simhei', 30)

        score_label_surface = score_label_font.render(u'SCORE：', False, SCORE_LABEL_COLOR)
        score_label_position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + 100, GAME_AREA_TOP + 6 * CELL_WIDTH)
        screen.blit(score_label_surface, score_label_position)

        score_font = pygame.font.SysFont('arial', 36)
        score_surface = score_font.render(str(score), False, SCORE_COLOR)
        score_label_width = score_label_surface.get_width()
        score_position = (score_label_position[0] + score_label_width + 20, score_label_position[1])
        screen.blit(score_surface, score_position)

    @staticmethod
    def draw_start_prompt(screen, game_resource):
        start_tip_position = (GAME_AREA_LEFT - 3* CELL_WIDTH, GAME_AREA_TOP + 8* CELL_WIDTH)
        screen.blit(game_resource.load_newgame_img(), start_tip_position)

    @staticmethod
    def draw_title_prompt(screen, game_resource):
        title_tip_position = (GAME_AREA_LEFT - 1.3* CELL_WIDTH, GAME_AREA_TOP + 1 * CELL_WIDTH)
        screen.blit(game_resource.load_title_img(), title_tip_position)

    @staticmethod
    def draw_pause_prompt(screen, game_resource):

        '''pausing game'''

        pause_position = (GAME_AREA_LEFT - 2 * CELL_WIDTH, GAME_AREA_TOP + 6 * CELL_WIDTH)
        screen.blit(game_resource.load_pausing_img(), pause_position)
        resume_tip_position = (GAME_AREA_LEFT , GAME_AREA_TOP + 9 * CELL_WIDTH)
        screen.blit(game_resource.load_continue_img(), resume_tip_position)

    @staticmethod
    def draw_game_over(screen, game_resource):
        gameover_position = (GAME_AREA_LEFT -CELL_WIDTH, GAME_AREA_TOP + 4 * CELL_WIDTH)
        screen.blit(game_resource.load_gameover_img(), gameover_position)

    @staticmethod
    def draw_next_piece(screen, next_piece):

        '''draw next block'''
        # draw the hint area
        start_x = GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH * 2
        start_y = GAME_AREA_TOP
        GameDisplay.draw_border(screen, start_x, start_y, 4, 4)

        if next_piece:
            start_x += EDGE_WIDTH
            start_y += EDGE_WIDTH
            cells = []  # cells stores the table cell which filled with cells
            shape_template = PIECES[next_piece.shape]
            shape_turn = shape_template[next_piece.turn_times]
            for r in range(len(shape_turn)):
                for c in range(len(shape_turn[0])):
                    if shape_turn[r][c] == 'O':
                        cells.append((c, r, PIECE_COLORS[next_piece.shape]))
            #setting position of the hint block
            max_c = max([cell[0] for cell in cells])
            min_c = min([cell[0] for cell in cells])
            start_x += round((4 - (max_c - min_c + 1)) / 2 * CELL_WIDTH)
            max_r = max([cell[1] for cell in cells])
            min_r = min([cell[1] for cell in cells])
            start_y += round((4 - (max_r - min_r + 1)) / 2 * CELL_WIDTH)

            # draw blocks
            for cell in cells:
                color = cell[2]
                left_top = (start_x + (cell[0] - min_c) * CELL_WIDTH,
                            start_y + (cell[1] - min_r) * CELL_WIDTH)
                GameDisplay.draw_cell_rect(screen, left_top, color)

    @staticmethod
    def draw_border(screen, start_x, start_y, line_num, column_num):
        top_border = pygame.Rect(start_x, start_y, 2 * EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, top_border)

        left_border = pygame.Rect(start_x, start_y, EDGE_WIDTH, 2 * EDGE_WIDTH + line_num * CELL_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, left_border)

        right_border = pygame.Rect(start_x + EDGE_WIDTH + column_num * CELL_WIDTH, start_y, EDGE_WIDTH,
                                   2 * EDGE_WIDTH + line_num * CELL_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, right_border)

        bottom_border = pygame.Rect(start_x, start_y + EDGE_WIDTH + line_num * CELL_WIDTH,
                                    2 * EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, bottom_border)

    @staticmethod
    def draw_mannual(screen):
        base_position_x = 830
        base_position_y = GAME_AREA_TOP + 450
        title_font = pygame.font.SysFont('stkaiti', 30)
        title_surface = title_font.render(u'How to play:', True, TITLE_COLOR)
        title_position = (base_position_x, base_position_y)
        screen.blit(title_surface, title_position)

        base_position_y += 40
        gamectrl_label_font = pygame.font.SysFont('stkaiti', 24)
        gamectrl_label_surface = gamectrl_label_font.render(u'Game control:', True, TITLE_COLOR)
        gamectrl_label_position = (base_position_x, base_position_y)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)

        base_position_y += 40
        man_font = pygame.font.SysFont('stkaiti', 24)
        man_down_surface = man_font.render(u'Exit: q', False, HANZI_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit(man_down_surface, man_down_position)

        base_position_y += 40
        # man_font = pygame.font.SysFont('stkaiti', 20)
        man_pause_surface = man_font.render(u'Pause/Continue: p', False, HANZI_COLOR)
        man_pause_position = (base_position_x, base_position_y)
        screen.blit(man_pause_surface, man_pause_position)



        base_position_y += 40
        # man_font = pygame.font.SysFont('stkaiti', 20)
        man_music_surface = man_font.render(u'Pause/Continue musi: M', False, HANZI_COLOR)
        man_music_position = (base_position_x, base_position_y)
        screen.blit(man_music_surface, man_music_position)

        base_position_y += 60
        # gamectrl_label_font = pygame.font.SysFont('stkaiti', 24)
        gamectrl_label_surface = gamectrl_label_font.render(u'Square control:', True, TITLE_COLOR)
        gamectrl_label_position = (base_position_x, base_position_y)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)

        base_position_y += 40
        # man_font = pygame.font.SysFont('stkaiti', 20)
        man_down_surface = man_font.render(u'Flip direction: up key, '
                                           u'Move down: down key', False, HANZI_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit(man_down_surface, man_down_position)

        base_position_y += 40
        man_move_surface = man_font.render(u'Move left: left key, '
                                           u'Move right: right key', False, HANZI_COLOR)
        man_move_position = (base_position_x, base_position_y)
        screen.blit(man_move_surface, man_move_position)

        base_position_y += 40
        man_speed_surface = man_font.render(u'Rapid fall: f', False, HANZI_COLOR)
        man_speed_position = (base_position_x, base_position_y)
        screen.blit(man_speed_surface, man_speed_position)