"""
@author: Chris
@author: Sofanah
@author: Shibani
"""

import pygame 
from Player import Player

from collections import namedtuple
Edge = namedtuple("Edge", ["name", "index", "claimed"])
player_one = Player("Shibani", (255,0,0))
pygame.init()



#TODO
    # Size
    # board objects
class GameBoard:
    def __init__(self, rows, columns, screen, player_no=1):
        self._rows = max(rows, 2)
        self._columns = max(columns, 2)
        self._screen = screen
        self._drawWindow = screen.screen;
        self._dots = []
        self._lines = []
        self._validLines = []
        self._linecolors = []
        self._boxes = []
        self._player_no = player_no #number of players
        self._players = [] #player list
        self._currentPlayer = player_one
        self._boxmake = []
        
        self._dotSize = 10
        
        lineWidth = int(self._dotSize*0.8)
        lineLength = self._dotSize*10
        
        self._distBetweenDots = lineLength
        
        self._dotcolor = (255,0,0)
        self._dotshape = (self._dotSize, self._dotSize)
        
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
                player_color = self._players[0].get_color() #TODO: need to find a way to find which player
                self._linecolors[i] = player_color
                return i
        return None#instead of a boolean, lineIndex or None
    
    def setup_board(self):
        self.create_dots()
        self.create_lines()
        self.define_boxes()
    
    def draw(self):
        self.draw_lines()
        self.draw_dots()
        self.draw_boxes()

    def draw_boxes(self):
        for i in range(len(self._boxes)):
            top, bottom, left, right, owner = self._boxes[i]
            if(top.claimed == True) and (bottom.claimed == True) and (left.claimed == True) and (right.claimed == True):
                pygame.draw.rect(self._drawWindow, (0,255,0), (self._lines[i].left+(self._dotSize-1), self._lines[i].top+(self._dotSize-1), 100-(self._dotSize-1), 100-(self._dotSize-1)), 0)

    def isValid_move(self, index):
        for line in self._validLines:
            if line == index:
                return True
        return False
    
    def update_boxes(self, index, turn):
        #for every box that has the index of this line in it's named tuple, update that Edge to True
        #print index
        for i in range(len(self._boxes)):
            top, bottom, left, right, owner = self._boxes[i]
            if index == top.index:
                top = Edge(name = "top", index = index, claimed = True)
                #print "TT"
            if index == bottom.index:
                bottom = Edge(name = "bottom", index = index, claimed = True)
                #print "BT"
            if index == left.index:
                left = Edge(name = "left", index = index, claimed = True)
                #print "LT"
            if index == right.index:
                right = Edge(name = "right", index = index, claimed = True)
                #print "RT"
                
            self._boxes[i] = [top, bottom, left, right, owner]
            
            if(top.claimed == True) and (bottom.claimed == True) and (left.claimed == True) and (right.claimed == True):
                #print "BOXMAKE! " + str(i)
                if self._boxes[i] not in self._boxmake:
                    self._boxmake.append(self._boxes[i])
                    self._players[turn].score_inc()
                    print(self._players[turn]._name + "'s Score:" + str(self._players[turn].get_score()))
                    # print self._lines[i]
                    #print(self._boxmake)




    #return False for failed move, return True for success 
    def make_move(self, mousePos, turn):
        index = self.choose_line(mousePos)  
        if turn >= len(self._players):
            turn = 0
        self._currentPlayer = self._players[turn] 
        print ("--------TURN-------- " + str(turn))
        print ("Current Player: " + self._currentPlayer._name + "'s Turn " + str(turn))
        #check if None --> failed choice of click
        if index == None:
            return False
        #if not valid move, line was already chosen
        elif not self.isValid_move(index):
            return False
        else:
            self._validLines.remove(index)
            if (turn  + 1) >= len(self._players):
                turn = 0
                self._currentPlayer = self._players[turn] 
            else:
                turn += 1
                self._currentPlayer = self._players[turn] 
            print ("Next Player: " + self._currentPlayer._name + "'s Turn" + str(turn))
            if turn == 0:
                self.update_boxes(index, 2)  
            else:
                self.update_boxes(index, turn - 1)  
            self.game_over()
            return self._currentPlayer
            return True
    
    def game_over(self):
        #print len(self._validLines)
        if len(self._validLines) == 0:
            return True
        else:
            return False
        
    def dot_collision(self, mousePos):
        for i in range(len(self._dots)):
            if self._dots[i].collidepoint(mousePos):
                return False
        return True

    def add_player(self, player):
        # if len(self._players) < self._player_no:
        self._players.append(player)









