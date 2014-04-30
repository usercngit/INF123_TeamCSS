'''
@author: Chris
@author: Sofanah
@author: Shibani
'''

import pygame

import GameScreen
import GameBoard
from Player import Player


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
    dims = 800, 640
    #RGB = 100, 150, 150
    RGB = 0,0,0 
    global SCREEN
    SCREEN = GameScreen.GameScreen(dims, RGB)
    
    global g
    g = GameBoard.GameBoard(3,3,SCREEN)

    global player_one
    player_one = Player("CSS", (255,0,0))
    g.add_player(player_one)
    
    g.setup_board()
    
    global GAME_STATE
    GAME_STATE = 1;
        
######################################################################
def drawGame():
    """
    Draw screen, then dots, then lines, then boxes
    """
    SCREEN.draw()
    g.draw()
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
                g.make_move(event.pos)
    return

######################################################################

gameInit()
while True:
    
    if GAME_STATE == 1:
        processInput()
        drawGame()
        SCREEN.drawScore(player_one.get_score())
        pygame.display.update()
        GAMECLOCK.tick(FRAMERATE)
        