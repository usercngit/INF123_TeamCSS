"""
@author: Chris
@author: Sofanah
@author: Shibani
"""

import pygame

from collections import namedtuple

pygame.init()

#TODO
    # Size
    # board objects
class GameBoard:
    def __init__(self, rows, columns, screen):
        self._rows = rows
        self._columns = columns
        self._screen = screen
        self._drawWindow = screen.screen;
        self._dots = []
        self._lines = []
        self._linecolors = []
        self._boxes = []
        
        dotSize = 10
        
        lineWidth = dotSize - 2
        lineLength = dotSize*10
        
        self._distBetweenDots = lineLength
        
        self._dotcolor = (255,0,0)
        self._dotshape = (dotSize, dotSize)
        
        self._linecolor = (255,255,255)
        self._linewideshape = (lineLength, lineWidth)
        self._linetallshape = (lineWidth, lineLength)
    
    def create_dots(self):
        for x in range(self._columns):
            for y in range(self._rows): 
                self._dots.append(pygame.Rect(((x)*self._distBetweenDots, (y)*self._distBetweenDots), (self._dotshape)))
        
    def draw_dots(self):
        for dot in self._dots:
            pygame.draw.rect(self._drawWindow, self._dotcolor, dot)
            
    def create_lines(self):
        """ The number of horizontal lines === Rows*Columns - [the smaller of the two]"""
        #make Horizontal
        for y in range(self._rows):
            for x in range(self._columns-1):
                self._lines.append(pygame.Rect( (x*self._distBetweenDots , y*self._distBetweenDots +1) , (self._linewideshape) ))
                self._linecolors.append(self._linecolor)
        #make Vertical
        for x in range(self._rows):
            for y in range(self._columns-1):
                self._lines.append(pygame.Rect( (x*self._distBetweenDots +1, y*self._distBetweenDots) , (self._linetallshape) ))
                self._linecolors.append(self._linecolor)

    def draw_lines(self):
        for i in range(len(self._lines)):
            pygame.draw.rect(self._drawWindow, self._linecolors[i], self._lines[i])
            
    def define_boxes(self):
        Edge = namedtuple("Edge", ["name", "index", "claimed"])
        
        for n in range(self._rows-1):
            for m in range(self._columns-1):
                top = Edge(name = "top", index = (len(self._boxes)), claimed = False)
                bottom = Edge(name = "bottom", index = ((len(self._boxes)) + (self._columns-1)), claimed = False)
                left = Edge(name = "left", index = ((len(self._boxes)) + ( (self._columns*self._rows) - (self._rows-n) )), claimed = False)
                right = Edge(name = "right", index = left.index+1, claimed = False)
            
                newBox = {top, bottom, left, right, None}
                self._boxes.append(newBox)

    def dot_collision(self, mousePos):
        for i in range(len(self._dots)):
            if self._dots[i].collidepoint(mousePos):
                return False
        return True

    def choose_line(self, mousePos):
        for i in range(len(self._lines)):
            if self._lines[i].collidepoint(mousePos) and self.dot_collision(mousePos): 
                self._linecolors[i] = (0,0,0)
                return i
        return None#instead of a boolean, lineIndex or None
    
    