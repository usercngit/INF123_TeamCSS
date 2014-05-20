'''
@author: Chris
@author: Sofanah
@author: Shibani
'''

"""
Viewport
    class will take in the native resolution to produce a view that is
    near (heightRatio, widthRatio) of native.
    
    It will be used to display any screens the program must display.
"""

import pygame.display
from math import floor

class FixedViewport:
    
    def __init__(self, width, height):        
        self.height = height
        self.width = width
        
        resolution = int(self.width), int(self.height)
        
        self.window = pygame.display.set_mode(resolution)
        
    def renderFullScreen(self, model):
        model.draw(self.window)
        pygame.display.flip()
        
    def renderPartScreen(self, model1, model2, percent1=50):
        percent1 = float(min( max(percent1, 30.0)/100.0, 1.0))
        percent2 = float(1.0 - percent1)
        
        surface1 = 0, 0, floor(self.width * percent1), self.height
        surface2 = surface1[2], 0, floor(self.width * percent2), self.height

        model1.draw(self.window.subsurface(surface1))
        model2.draw(self.window.subsurface(surface2))
        
        pygame.display.update()
    
class Viewport:
    
    def __init__(self, heightRatio=50, widthRatio=50):
        info = pygame.display.Info()
        self.nativeH = info.current_h
        self.nativeW = info.current_w
        
        ratioH = float(min( max(heightRatio, 30) , 100.0))
        ratioW = float(min( max(widthRatio , 30) , 100.0))
        
        self.height = floor(self.nativeH * (ratioH/100.0))
        self.width = floor(self.nativeW * (ratioW/100.0))
        
        resolution = int(self.width), int(self.height)
        
        self.window = pygame.display.set_mode(resolution)
        
    def renderFullScreen(self, model):
        model.draw(self.window)
        pygame.display.flip()
        
    def renderPartScreen(self, model1, model2, percent1=50):
        percent1 = float(min( max(percent1, 30.0)/100.0, 1.0))
        percent2 = float(1.0 - percent1)
        
        surface1 = 0, 0, floor(self.width * percent1), self.height
        surface2 = surface1[2], 0, floor(self.width * percent2), self.height

        model1.draw(self.window.subsurface(surface1))
        model2.draw(self.window.subsurface(surface2))
        
        pygame.display.update()
        