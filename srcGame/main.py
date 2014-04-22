'''
@author: Chris
@author: Sofanah
@author: Shibani
'''

import pygame

import GameScreen
import GameBoard


"""
TODO: Import settings from a text file
        : game screen 
            - width
            - height
        : game server
            - IP
            - port
            - player list ?  (if persistent player list is decided)
                
        : debug mode
            - game board rows, columns = 4 x 4
            - number of players = 2
"""

######################################################################
def gameInit():
    pygame.init()
    
    global GAMECLOCK
    GAMECLOCK = pygame.time.Clock()
    global FRAMERATE
    FRAMERATE = 40
    
    """
        Program State overview:
            0 = loading
            1 = main screen
            2 = game
            3 = game lobby
            4 = online game
    """
    global PROG_STATE
    PROG_STATE = 0
    
    #create display
    dims = 800, 720
    RGB = 100, 150, 150
    global SCREEN
    SCREEN = GameScreen.GameScreen(dims, RGB)
    
    global g
    g = GameBoard.GameBoard(4,4,SCREEN)
    
    g.create_dots()
    g.create_lines()
    
    global GAME_STATE
    GAME_STATE = 1;
        
######################################################################
def drawGame():
    """
    Draw screen, then dots, then lines, then boxes
    """
    SCREEN.draw()
    g.draw_lines()
    g.draw_dots()
    g.define_boxes()
    pygame.display.update()
    #g.run()
    
######################################################################
def processInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if PROG_STATE == 1:
                return
            else:
                g.choose_line(event.pos)
    return

######################################################################

gameInit()
while True:
    
    if GAME_STATE == 1:
        processInput()
        drawGame()
        pygame.display.update()
        GAMECLOCK.tick(FRAMERATE)