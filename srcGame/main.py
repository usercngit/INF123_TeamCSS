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
    
    #create display
    dims = 800, 720
    RGB = 100, 150, 150
    global SCREEN
    SCREEN = GameScreen.GameScreen(dims, RGB)
    
    global g
    g = GameBoard.GameBoard(4,4,SCREEN.screen)
    
    global GAME_STATE
    GAME_STATE = 1;
        
######################################################################
def drawGame():
    """
    Draw screen, then dots, then lines, then boxes
    """
    SCREEN.draw()
    g.draw_dots()
    pygame.display.update()
    g.run()
    
######################################################################
def processInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    return

######################################################################

gameInit()
while True:
    
    if GAME_STATE == 1:
        processInput()
        drawGame()
        pygame.display.update()
        GAMECLOCK.tick(FRAMERATE)