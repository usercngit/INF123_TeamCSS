'''
@author: Chris
'''

import pygame
import Viewport
from Board import Board

pygame.init()
GAMECLOCK = pygame.time.Clock()
FRAMERATE = 40
VIEWPORT = Viewport.Viewport(60, 60)

GAMEBOARD = Board(2,2,1)
GAMEBOARD2 = Board(3,3,1)
GAMEBOARD.setup_board()
GAMEBOARD2.setup_board()

sleft = VIEWPORT.window.subsurface((0,0,100,200))
sright = VIEWPORT.window.subsurface((100,0,100,200))
VIEWPORT.window.fill((200,200,150))

######################################################################
def processInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            GAMEBOARD.make_move(event.pos)
            GAMEBOARD2.make_move(event.pos)
    return

######################################################################
pygame.init()
while True:
    processInput()
#    VIEWPORT.renderFullScreen(GAMEBOARD)
    VIEWPORT.renderPartScreen(GAMEBOARD, 50, GAMEBOARD2)
    GAMECLOCK.tick(50)
        