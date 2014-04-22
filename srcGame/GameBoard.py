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
                self._lines.append(pygame.Rect( (x*self._distBetweenDots, y*self._distBetweenDots +1) , (self._linewideshape) ))
        #make Vertical
        for x in range(self._rows):
            for y in range(self._columns-1):
                self._lines.append(pygame.Rect( (x*self._distBetweenDots +1, y*self._distBetweenDots) , (self._linetallshape) ))
    
    def draw_lines(self):
        for line in self._lines:
            pygame.draw.rect(self._drawWindow, self._linecolor, line)
            
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
                print top, bottom, left, right
            
    def choose_line(self, mousePos):
        x,y = mousePos
        return #instead of a boolean, (x,y) or None

    def run(self): #only with a 3x3 (in  terms of boxes) --> 4x4 (in terms of dots)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = event.pos        
                            
                    #first row
                    if((x <= 200) and (x >= 100) and (y <= 106) and (y >=96)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (100,100), (200,100), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 300) and (x >= 200) and (y <= 106) and (y >=96)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (200,100), (300,100), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 400) and (x >= 300) and (y <= 106) and (y >=96)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (300,100), (400,100), 10) #horizontal
                        pygame.display.flip()
                
                    #second row
                    elif((x <= 200) and (x >= 100) and (y <= 206) and (y >=196)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (100,200), (200,200), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 300) and (x >= 200) and (y <= 206) and (y >=196)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (200,200), (300,200), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 400) and (x >= 300) and (y <= 206) and (y >=196)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (300,200), (400,200), 10) #horizontal
                        pygame.display.flip()
                    
                    #third row
                    elif((x <= 200) and (x >= 100) and (y <= 306) and (y >=296)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (100,300), (200,300), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 300) and (x >= 200) and (y <= 306) and (y >=296)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (200,300), (300,300), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 400) and (x >= 300) and (y <= 306) and (y >=296)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (300,300), (400,300), 10) #horizontal
                        pygame.display.flip()
                    
                    #fourth row
                    elif((x <= 200) and (x >= 100) and (y <= 406) and (y >=396)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (100,400), (200,400), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 300) and (x >= 200) and (y <= 406) and (y >=396)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (200,400), (300,400), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 400) and (x >= 300) and (y <= 406) and (y >=396)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (300,400), (410,400), 10) #horizontal #extra 10
                        pygame.display.flip()
                        
                    #first column
                    elif((x <= 110) and (x >= 100) and (y >= 106) and (y <= 196)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (104,96), (104,196), 10) #veritcal 
                        pygame.display.flip()
                    elif((x <= 110) and (x >= 100) and (y >= 206) and (y <= 296)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (104,196), (104,296), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 110) and (x >= 100) and (y >= 306) and (y <= 396)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (104,296), (104,396), 10) #vertical
                        pygame.display.flip()
                    
                    #second column
                    elif((x <= 210) and (x >= 200) and (y >= 106) and (y <= 196)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (204,96), (204,196), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 210) and (x >= 200) and (y >= 206) and (y <= 296)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (204,196), (204,296), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 210) and (x >= 200) and (y >= 306) and (y <= 396)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (204,296), (204,396), 10) #vertical
                        pygame.display.flip()
                        
                    #third column
                    elif((x <= 310) and (x >= 300) and (y >= 106) and (y <= 196)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (304,96), (304,196), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 310) and (x >= 300) and (y >= 206) and (y <= 296)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (304,196), (304,296), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 310) and (x >= 300) and (y >= 306) and (y <= 396)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (304,296), (304,396), 10) #vertical
                        pygame.display.flip()

                    #fourth column
                    elif((x <= 410) and (x >= 400) and (y >= 106) and (y <= 196)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (404,96), (404,196), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 410) and (x >= 400) and (y >= 206) and (y <= 296)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (404,196), (404,296), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 410) and (x >= 400) and (y >= 306) and (y <= 396)):
                        pygame.draw.line(self._drawWindow, (0,0,255), (404,296), (404,396), 10) #vertical
                        pygame.display.flip()
