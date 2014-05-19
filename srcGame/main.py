'''
@author: Chris
@author: Sofanah
@author: Shibani
'''

import pygame

from Viewport import Viewport
from GameScreen import GameScreen
import GameBoard
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
    
    global SCREEN
    SCREEN = GameScreen((600, 600), (0,0,0))
    
    global VIEWPORT
    VIEWPORT = Viewport(60,60)
    
    global g
    g = GameBoard.GameBoard(3, 3, SCREEN, 3)
    #g = Board(3,3,1)

    global player_one
    player_one = Player("Shibani", (255,0,0))
    g.add_player(player_one)

    global player_two
    player_two = Player("Sufana", (0,255,0))
    g.add_player(player_two)

    global player_three
    player_three = Player("Chris", (0,0,255))
    g.add_player(player_three)
    
    g.setup_board()
    
    global GAME_STATE
    GAME_STATE = 1;
        
######################################################################
def drawGame():
    """
    Draw screen, then dots, then lines, then boxes
    """
    SCREEN.draw(g.game_over(), g._players, g._currentPlayer) ##HERE
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
                global TURN
                if (g.make_move(event.pos, TURN)):
                    if (TURN  + 1) >= len(g._players):
                        TURN = 0
                    else:
                        TURN += 1
    return

######################################################################

gameInit()

while True:
    
    if GAME_STATE == 1:
        processInput()
        drawGame()
        pygame.display.update()
        GAMECLOCK.tick(FRAMERATE)
        