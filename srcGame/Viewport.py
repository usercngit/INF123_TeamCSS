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

class Viewport:
    
    def __init__(self, heightRatio, widthRatio):
        info = pygame.display.Info()
        self.nativeH = info.current_h
        self.nativeW = info.current_w
        
        ratioH = float(heightRatio)
        ratioW = float(widthRatio)
         
        self.height = self.nativeH * (ratioH/100)
        self.width = self.nativeW * (ratioW/100)
        
        resolution = int(self.width), int(self.height)
        
        self.window = pygame.display.set_mode(resolution)
        
    def render(self, models):
        
        pygame.display.update()
        