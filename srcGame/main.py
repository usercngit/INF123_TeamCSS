'''
@author: Chris
@author: Sofanah
@author: Shibani
'''

import pygame

from Viewport import FixedViewport
from Board import Board
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
    global TURN 
    TURN = 0
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
    
    global VIEWPORT
    VIEWPORT = FixedViewport(900, 600)
    
    global GAMEBOARD
    GAMEBOARD = Board(VIEWPORT.width, VIEWPORT.height, 6, 2, 5)

    player_one = Player("Chris", (255,0,0))
    GAMEBOARD.add_player(player_one)

    player_two = Player("Alex", (0,255,0))
    GAMEBOARD.add_player(player_two)
    
    player_three = Player("Joe", (0,0,255))
    GAMEBOARD.add_player(player_three)
    
    player_four = Player("Sufana", (100,100,100))
    GAMEBOARD.add_player(player_four)
    
    player_five = Player("Shibani", (200,200,200))
    GAMEBOARD.add_player(player_five)
    
    global GAME_STATE
    GAME_STATE = 1;
        
######################################################################
def drawGame():
    """
    Draw screen, then dots, then lines, then boxes
    """
    #VIEWPORT.renderPartScreen(GAMEBOARD, SIDEBAR, 60)
    VIEWPORT.renderFullScreen(GAMEBOARD)
#    GAMESCREEN.draw(GAMEBOARD.game_over(), GAMEBOARD._players, GAMEBOARD._players[GAMEBOARD._currentPlayer])
    
######################################################################
def processInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if PROG_STATE == 1:
                return
            else:
                GAMEBOARD.update(event.pos)
    return

######################################################################

gameInit()

while True:
    
    if GAME_STATE == 1:
        processInput()
        drawGame()
        pygame.display.update()
        GAMECLOCK.tick(FRAMERATE)
        