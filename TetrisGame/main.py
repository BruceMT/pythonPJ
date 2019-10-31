# @Author  : weibin Ma
# @Time    : 10/30/2019
# @title: pythonPJ
import sys
import pygame

def main():

    pygame.init()

    screen = pygame.display.set_mode((1200, 900) )  #resolution ratio 1200*900
    pygame.display.set_caption("TetrisGame")  #window title

#background color
    bg_color = (230, 230, 230)

#main body
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #close window
                sys.exit()   #esc  program

 #Fill in the screen background color
        screen.fill(bg_color)

          #redraw
        pygame.display.flip()

if __name__ == '__main__':
       main()