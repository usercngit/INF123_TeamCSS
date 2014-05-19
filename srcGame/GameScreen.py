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
        # self.draw(2, False)

        

    def drawScore(self, currentPlayer):
        font = pygame.font.Font(None, 36)
        label = font.render("Score: " + str(currentPlayer._score), 1, (255, 0, 0))
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

    def drawPlayerTurn(self, currentPlayer):
        font = pygame.font.Font(None, 40)
        label = font.render("It is " + currentPlayer._name + "'s turn", 1, (255,0,0))
        textpos = label.get_rect()
        textpos.centery = self.screen.get_rect().centery + 50
        self.screen.blit(label, textpos)

    def drawScore(self, Players):
        vertical_space = 0
        font = pygame.font.Font(None, 40)
        for player in Players:
            vertical_space += 50
            label = font.render(player._name + ": " + str(player._score), 1, (255,0,0))
            textpos = label.get_rect()
            textpos.centery = self.screen.get_rect().centerx + vertical_space
            self.screen.blit(label, textpos)

    def draw(self, gameover, Players, currentPlayer):
        self.screen.fill(self.RGB)
        self.drawScore(Players)
        self.drawGameOver(gameover)
        self.drawPlayerTurn(currentPlayer)



