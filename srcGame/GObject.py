'''
@author: Chris
@author: Sofanah
@author: Shibani
'''

"""
Class for creating representations of the different game objects,
as well as updating them or drawing them
"""
import pygame

class GObject:
    def __init__(self, pos, shape, color, linewidth=0):
        self.pos = pos
        self.shape = shape
        self.color = color
        self.linewidth = linewidth
        self.rect = pygame.Rect(self.pos, self.shape)
    
    def collide(self, point):
        return self.rect.collidepoint(point)
    
    def draw(self, view):
        pygame.draw.rect(view,self.color, self.rect, self.linewidth)
        
########## TEXT #############
class Text():
    def __init__(self, text, color, size):
        font = pygame.font.Font(None, size)
        self.label = font.render(text, 1, color)
        
    def draw(self, view, x, y):
        textpos = (x,y)
        view.blit(self.label, textpos)   

######### BUTTON ############
class Button(GObject):
    def __init__ (self, pos, shape, color, linewidth, text, textColor, textSize):
        GObject.__init__(self, pos, shape, color, linewidth)
        
        font = pygame.font.Font(None, textSize)
        self.label = font.render(text, 1, textColor)
        self.textpos = self.label.get_rect()
        self.textpos.center = self.rect.center
        
    def draw(self, view):
        pygame.draw.rect(view, self.color, self.rect, self.linewidth)
        view.blit(self.label, self.textpos)        
        
########### BOX #############
class Box(GObject):
    def __init__ (self, pos, shape, color, linewidth, topIndex, bottomIndex, leftIndex, rightIndex):
        GObject.__init__(self, pos, shape, color, linewidth)
        
        self.topindex = topIndex
        self.top = False
        self.bottomindex = bottomIndex
        self.bottom = False
        self.leftindex = leftIndex
        self.left = False
        self.rightindex = rightIndex
        self.right = False
        
        self.filled = False
        self.owner = None
        
    def setIndexes(self, top, bottom, left, right):
        self.topindex = top
        self.bottomindex = bottom
        self.leftindex = left
        self.rightindex = right
        
    def isClaimed(self):
        return self.filled

    def update(self, index):
        if not self.filled:
            if self.topindex == index:
                self.top = True
            elif self.bottomindex == index:
                self.bottom = True
            elif self.leftindex == index:
                self.left = True
            elif self.rightindex == index:
                self.right = True
        
            if(self.left) and (self.right) and (self.bottom) and (self.top):
                self.filled = True
                
    def draw(self, view):
        if self.filled:
            pygame.draw.rect(view, self.color, self.rect, self.linewidth)