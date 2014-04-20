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

class GameScreen:
    def __init__ (self, dims, RGB):
        self.width, self.height = dims
        self.RGB = RGB
        self.screen = pygame.display.set_mode(dims)
        
    def draw(self):
        self.screen.fill(self.RGB)