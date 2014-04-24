"""
@author: Chris
@author: Sofanah
@author: Shibani
"""

import pygame

from collections import namedtuple
Edge = namedtuple("Edge", ["name", "index", "claimed"])

pygame.init()



#TODO
    # Size
    # board objects
class GameBoard:
    def __init__(self, rows, columns, screen):
        self._rows = max(rows, 2)
        self._columns = max(columns, 2)
        self._screen = screen
        self._drawWindow = screen.screen;
        self._dots = []
        self._lines = []
        self._validLines = []
        self._linecolors = []
        self._boxes = []
        
        dotSize = 10
        
        lineWidth = int(dotSize*0.8)
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
        i = 0
        #make Horizontal
        for y in range(self._rows):
            for x in range(self._columns-1):
                self._lines.append(pygame.Rect( (x*self._distBetweenDots +1, y*self._distBetweenDots +1) , (self._linewideshape) ))
                self._linecolors.append(self._linecolor)
                self._validLines.append(i)
                i = i +1
        #make Vertical
        for y in range(self._rows-1):
            for x in range(self._columns):
                self._lines.append(pygame.Rect( (x*self._distBetweenDots +1, y*self._distBetweenDots +1) , (self._linetallshape) ))
                self._linecolors.append(self._linecolor)
                self._validLines.append(i)
                i = i +1
    
    def draw_lines(self):
        for i in range(len(self._lines)):
            pygame.draw.rect(self._drawWindow, self._linecolors[i], self._lines[i], 1)
            
    def define_boxes(self):
        for n in range(self._rows-1):
            for m in range(self._columns-1):
                top = Edge(name = "top", index = (len(self._boxes)), claimed = False)
                bottom = Edge(name = "bottom", index = ((len(self._boxes)) + (self._columns-1)), claimed = False)
                left = Edge(name = "left", index = ((len(self._boxes)) + ( (self._columns*self._rows) - (self._rows-n) )), claimed = False)
                right = Edge(name = "right", index = left.index+1, claimed = False)
            
                newBox = [top, bottom, left, right, None]
                self._boxes.append(newBox)
            
    def choose_line(self, mousePos):
        for i in range(len(self._lines)):
            if self._lines[i].collidepoint(mousePos) and self.dot_collision(mousePos):
                self._linecolors[i] = (0,0,0)
                return i
        return None#instead of a boolean, lineIndex or None
    
    def setup_board(self):
        self.create_dots()
        self.create_lines()
        self.define_boxes()
    
    def draw(self):
        self.draw_lines()
        self.draw_dots()
        
    def isValid_move(self, index):
        for line in self._validLines:
            if line == index:
                return True
        return False
    
    def update_boxes(self, index):
        #for every box that has the index of this line in it's named tuple, update that Edge to True
        print index
        for i in range(len(self._boxes)):
            top, bottom, left, right, owner = self._boxes[i]
            if index == top.index:
                top = Edge(name = "top", index = index, claimed = True)
                print "TT"
            if index == bottom.index:
                bottom = Edge(name = "bottom", index = index, claimed = True)
                print "BT"
            if index == left.index:
                left = Edge(name = "left", index = index, claimed = True)
                print "LT"
            if index == right.index:
                right = Edge(name = "right", index = index, claimed = True)
                print "RT"
                
            self._boxes[i] = [top, bottom, left, right, owner]
            
            if(top.claimed == True) and (bottom.claimed == True) and (left.claimed == True) and (right.claimed == True):
                print "BOXMAKE! " + str(i)

    #return False for failed move, return True for success 
    def make_move(self, mousePos):
        index = self.choose_line(mousePos)
        
        #check if None --> failed choice of click
        if index == None:
            return False
        #if not valid move, line was already chosen
        elif not self.isValid_move(index):
            return False
        else:
            self._validLines.remove(index)
            self.update_boxes(index)
            
            self.game_over()
            return True
    
    def game_over(self):
        print len(self._validLines)
        if len(self._validLines) == 0:
            print "GAMEOVERS"
            return True
        else:
            return False
        
    def dot_collision(self, mousePos):
        for i in range(len(self._dots)):
            if self._dots[i].collidepoint(mousePos):
                return False
        return True
    
    
