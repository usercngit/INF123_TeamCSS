'''
@author: Chris
@author: Sofanah
@author: Shibani
'''

"""
Defines window size, color
and will contain displays of game objects
"""

# TDOD
    # Build it
    # Display it
    # put the game board in it

import pygame
import GameBoard
from Player import Player

class GameScreen:
    def __init__ (self, dims, RGB):
        self.width, self.height = dims
        self.RGB = RGB
        self.screen = pygame.display.set_mode(dims)
        # self.drawScore(2)
        self.draw(2)

        

    def drawScore(self, score):
        font = pygame.font.Font(None, 36)
        label = font.render("Score: " + str(score), 1, (255, 0, 0))
        textpos = label.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        self.screen.blit(label, textpos)

    def draw(self, score):
        self.screen.fill(self.RGB)
        self.drawScore(score)

