'''
@author: Chris
'''

import pygame
import Viewport
from Player import Player
from Board import Board

pygame.init()
GAMECLOCK = pygame.time.Clock()
FRAMERATE = 40
VIEWPORT = Viewport.Viewport(90, 90)

sleft = VIEWPORT.window.subsurface((0,0,100,200))
sright = VIEWPORT.window.subsurface((100,0,100,200))
VIEWPORT.window.fill((200,200,150))

GAMEBOARD = Board(VIEWPORT.width, VIEWPORT.height,2,2,3)
#GAMEBOARD2 = Board(100,200,3,3,1)

player1 = Player("C", (200,200,200))
player2 = Player("J", (20,200,200))
GAMEBOARD.add_player(player1)
GAMEBOARD.add_player(player2)
#GAMEBOARD2.add_player(player1)
#GAMEBOARD2.add_player(player2)

######################################################################
def processInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            GAMEBOARD.update(event.pos)
            #GAMEBOARD2.update(event.pos)
    return

######################################################################
while True:
    processInput()
    VIEWPORT.renderFullScreen(GAMEBOARD)
#    VIEWPORT.renderPartScreen(GAMEBOARD, GAMEBOARD2, 50)
    GAMECLOCK.tick(50)
        