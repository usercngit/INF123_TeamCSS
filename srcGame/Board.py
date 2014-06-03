"""
@author: Chris
@author: Sofanah
@author: Shibani
"""
from GObject import GObject, Box, Button, Text
from Player import Player
import random

class Board:
    def __init__(self, viewwidth, viewheight, rows = 2, columns = 2, player_no=2):
        self._started = False
        self._ended = False
        
        self._rows = max(rows, 2)
        self._columns = max(columns, 2)
        self._viewwidth = viewwidth
        self._width = viewwidth - viewwidth/4
        self._height = viewheight
        
        self._playerControl = PlayerControl((self._width, 0), player_no)
        
        #TODO: other buttons
        startpos = 0,0#self._width/4, self._height/4
        startshape = self._width, self._height#(self._width/2, self._height/4)
        startcolor = (150, 150, 200)
        startButton = Button(startpos, startshape, startcolor, 0, "START", (0,0,0), 32)
        
        gameBackground = GObject((0,0), (self._width, self._height), (0,0,0))
        playerBackground = GObject((self._width, 0), (viewwidth-self._width, viewheight), (255, 255, 255))
        
        backgrounds = []
        dots = []
        lines = []
        boxes = []
        start = []
        
        start.append(startButton)
        backgrounds.append(gameBackground)
        backgrounds.append(playerBackground)
        
        self._objects = {'backgrounds':backgrounds, 'dots':dots, 'lines':lines, 'boxes':boxes, 'start':start}
        
        self._validLines = []
        self._filledBoxes = []
        
        self._dotSize = 10
        
        lineWidth = int(self._dotSize*0.8)
        lineLength = self._dotSize*10
        
        self._distBetweenDots = lineLength
        
        self._dotcolor = (200,50,50)
        self._dotshape = (self._dotSize, self._dotSize)
        
        self._linecolor = (100,100,100)
        self._linewideshape = (lineLength, lineWidth)
        self._linetallshape = (lineWidth, lineLength)
        
        self._boxcolor = (0, 255, 0)
        self._boxshape = (lineLength, lineLength)
    
    def getasdict(self, thing):
        gameobjects = []
        
        if thing == 'players':
            for player in self._playerControl._players:
                p = player.to_list()
                gameobjects.append(p)
                
        elif thing == 'backgrounds':
            for back in self._objects['backgrounds']:
                b = back.to_list()
                gameobjects.append(b)
                
        elif thing == 'dots':
            for dot in self._objects['dots']:
                d = dot.to_list()
                gameobjects.append(d)
            
        elif thing == 'lines':
            for line in self._objects['lines']:
                l = line.to_list()
                gameobjects.append(l)
                    
        elif thing == 'boxes':
            for box in self._objects['boxes']:
                if box.filled:
                    b = box.to_list()
                    gameobjects.append(b)
        
        elif thing == 'buttons':
            for button in self._objects['start']:
                s = button.to_list()
                gameobjects.append(s)
                                
        return gameobjects
        
    def to_list(self):
        players = self.getasdict('players')
        backgrounds = self.getasdict('backgrounds')
        dots = self.getasdict('dots')
        lines = self.getasdict('lines')
        boxes = self.getasdict('boxes')
        buttons = self.getasdict('buttons')
            
        return {'players':players, 'backgrounds':backgrounds, 'dots':dots, 'lines':lines, 'boxes':boxes, 'buttons':buttons}
        
####################### DRAWING #########################
    def draw(self, view):
        self.drawObj('backgrounds', view)
        self._playerControl.display(view)
        
        if not self._started:
            self.drawObj('start', view)
        else:
            self.drawObj('boxes', view)
            self.drawObj('lines', view)
            self.drawObj('dots', view)
    
    def drawObj(self, name, view):
        for obj in self._objects[name]:
            if name == 'boxes':
                if obj.filled:
                    obj.draw(view)
            else:
                obj.draw(view)

######################## SETUP ##########################
    def setup_board(self):
        self._started = True
        self._objects['start'] = []
        
        self.create_dots()
        self.create_lines()
        self.create_boxes()
        self.define_boxes()
        
    def create_dots(self):
        for x in range(self._columns):
            for y in range(self._rows):
                pos = (x*self._distBetweenDots, y*self._distBetweenDots)
                newObj = GObject(pos, self._dotshape, self._dotcolor, 0)
                self._objects['dots'].append(newObj)
      
    def create_lines(self):
        """ The number of horizontal lines === Rows*Columns - [the smaller of the two]"""
        i = 0
        #make Horizontal
        for y in range(self._rows):
            for x in range(self._columns-1):
                pos = (x*self._distBetweenDots +1, y*self._distBetweenDots +1)
                newObj = GObject(pos, self._linewideshape, self._linecolor, 1)
                self._objects['lines'].append(newObj)
                self._validLines.append(i)
                i = i +1
        #make Vertical
        for y in range(self._rows-1):
            for x in range(self._columns):
                pos = (x*self._distBetweenDots +1, y*self._distBetweenDots +1)
                newObj = GObject(pos, self._linetallshape, self._linecolor, 1)
                self._objects['lines'].append(newObj)
                self._validLines.append(i)
                i = i +1
                
    def create_boxes(self):
        for y in range(self._rows-1):
            for x in range(self._columns-1):
                pos = (x*self._distBetweenDots + self._dotSize -1), (y*self._distBetweenDots + self._dotSize -1)
                newBox = Box(pos, self._boxshape, self._boxcolor, 0, 0, 0, 0, 0)
            
                self._objects['boxes'].append(newBox)
            
    def define_boxes(self): 
        i = 0
        for n in range(self._rows-1):
            for m in range(self._columns-1):
                index1 = i
                index2 = i + (self._columns-1)
                index3 = i + (self._columns*self._rows) - (self._rows-n)
                index4 = index3+1
                
                self._objects['boxes'][i].setIndexes(index1, index2, index3, index4)
                
                i = i+1


################# GAME LOGIC ###################
    def update(self, mousePos):
        #check if the game exit button is clicked first
        #TODO: implement
        
        #if game isn't started yet, wait for players
        if not self._started:
            if self._playerControl.is_full():
                self.setup_board()
                return True
                
            elif self._objects['start'][0].collide(mousePos) and (len(self._playerControl._players) >= 2):
                self.setup_board()
                return True
                
            return False
        #if game is started, run the logic
        else:
            index = self.choose_line(mousePos)
                #check if None --> failed choice of click
            if index == None:
                return False
                #if not valid move, line was already chosen
            elif not self.isValid_move(index):
                return False
            
            else:
                self._objects['lines'][index].linewidth = 0
                self._objects['lines'][index].color = self.current_player()._color
                self._validLines.remove(index)
                #if no boxes are scored, change player
                if not self.update_boxes(index):
                    self._playerControl.next()
            
                self.game_over()
                return True
        
    def choose_line(self, mousePos):
        for i, line in enumerate(self._objects['lines']):
            if line.collide(mousePos):
                for dot in self._objects['dots']:
                    if not dot.collide(mousePos):
                        return i
        return None #instead of a boolean, lineIndex or None

    def isValid_move(self, index):
        for i in self._validLines:
            if i == index:
                return True
        return False
    
    def update_boxes(self, index):
        reval = False
        for i, box in enumerate(self._objects['boxes']):
            box.update(index)
            
            if box.isClaimed():
                #if new box is filled.
                if i not in self._filledBoxes:
                    self._filledBoxes.append(i)
                    box.color = self.current_player()._color
                    self.current_player().score_inc()
                    reval = True
                    
        return reval
    
    def game_over(self):
        if len(self._validLines) == 0:
            self._ended = True
        return self._ended
    
    def remove_player(self, player):
        self._playerControl.remove_player(player)
        return self._playerControl.is_empty()
        
    def add_player(self, player): #tries to add player. returns false if fail: true if success
        #allow adding players
        if not self._started:
            return self._playerControl.add_player(player)
        return False
            
    def current_player(self): #returns the player
        return self._playerControl.current()
    
    def is_full(self):
        return self._playerControl.is_full()

class PlayerControl:
    def __init__(self, pos, player_no):
        
        self.pos = pos
        
        self._currentPlayer = 0
        self._player_no = max(player_no, 2) #number of players
        self._players = [] #player list
        
    def current(self):
        if not self.is_empty():
            return self._players[self._currentPlayer]
     
    def add_player(self, player):
        if len(self._players) < self._player_no:
            x,y = self.pos
            player._rep.pos = (x, (50*len(self._players)))
            if self.is_empty():
                player.set_color(player._color)
            self._players.append(player)
            return True
        return False
            
    def remove_player(self, player):
        #logic for altering the player list on a removal
        if player in self._players:
            self._players.remove(player)
            if not self.is_empty():
                self._currentPlayer = (self._currentPlayer) % len(self._players)
                self.current().set_color(self.current()._color)
                
                
        for player in self._players:
            gamepos = player._rep.pos[0], 50*((self._players.index(player)))
            player._rep.pos = gamepos
        
    def next(self):
        self.current().set_color((0,0,0))
        self._currentPlayer = (self._currentPlayer + 1) % len(self._players)
        self.current().set_color(self.current()._color)
        return self.current()
            
    def is_full(self):
        return len(self._players) == self._player_no
    
    def is_empty(self):
        return len(self._players) == 0
    
    def display(self, view):
        for player in self._players:
            player.draw(view)