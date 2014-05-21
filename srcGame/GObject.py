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
        
    def to_list(self):
        return {'pos':self.pos, 'shape':self.shape, 'color':self.color, 'linewidth':self.linewidth}
    
    def collide(self, point):
        return self.rect.collidepoint(point)
    
    def draw(self, view):
        pygame.draw.rect(view,self.color, self.rect, self.linewidth)
        
########## TEXT #############
class Text():
    def __init__(self, pos, text, color, size):
        self.pos = pos
        self.text = text
        self.color = color
        self.size = size
        
    def to_list(self):
        return {'pos':self.pos, 'text':self.text, 'color':self.color, 'size':self.size}
        
    def draw(self, view):
        font = pygame.font.Font(None, self.size)
        label = font.render(self.text, 1, self.color)
        view.blit(label, self.pos)

######### BUTTON ############
class Button(GObject):
    def __init__ (self, pos, shape, color, linewidth, text, textColor, textSize):
        GObject.__init__(self, pos, shape, color, linewidth)
        self.text = text
        self.textSize = textSize
        self.textColor = textColor
        
    def to_list(self):
        return {'pos':self.pos, 'shape':self.shape, 'color':self.color, 'linewidth':self.linewidth, 'text':self.text, 'textColor':self.textColor, 'textSize':self.textSize}
        
    def draw(self, view):
        font = pygame.font.Font(None, self.textSize)
        label = font.render(self.text, 1, self.textColor)
        textpos = label.get_rect()
        textpos.center = self.rect.center
        
        pygame.draw.rect(view, self.color, self.rect, self.linewidth)
        view.blit(label, textpos)        
        
########### BOX #############
class Box(GObject):
    def __init__ (self, pos, shape, color, linewidth, topIndex, bottomIndex, leftIndex, rightIndex, top = False, bottom = False, left = False, right = False, filled = False):
        GObject.__init__(self, pos, shape, color, linewidth)
        
        self.topindex = topIndex
        self.top = top
        self.bottomindex = bottomIndex
        self.bottom = bottom
        self.leftindex = leftIndex
        self.left = left
        self.rightindex = rightIndex
        self.right = right
        
        self.filled = filled
        
    def to_list(self):
        return {'pos':self.pos, 'shape':self.shape, 'color':self.color, 'linewidth':self.linewidth}
        
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