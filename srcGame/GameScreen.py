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
        self.draw(2, False)

        

    def drawScore(self, score):
        font = pygame.font.Font(None, 36)
        label = font.render("Score: " + str(score), 1, (255, 0, 0))
        textpos = label.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        self.screen.blit(label, textpos)

    def drawGameOver(self, gameover):
        if gameover:
            font = pygame.font.Font(None, 40)
            label = font.render("Game Over", 1, (255,0,0))
            textpos = label.get_rect()
            textpos.centery = self.screen.get_rect().centery
            self.screen.blit(label, textpos)

    def draw(self, score, gameover):
        self.screen.fill(self.RGB)
        self.drawScore(score)
        self.drawGameOver(gameover)

    def drawWindow(self):
        self.screen.fill(self.RGB)


