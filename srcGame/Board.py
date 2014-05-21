"""
@author: Chris
@author: Sofanah
@author: Shibani
"""
from GObject import GObject, Box
from Player import Player

class Board:
    def __init__(self, rows = 2, columns = 2, player_no=2, viewheight, viewwidth):
        self._started = False
        self._ended = False
        
        self._rows = max(rows, 2)
        self._columns = max(columns, 2)
        
<<<<<<< HEAD
        startpos = (viewwidth - viewwidth/2, viewheight - viewheight/2)
        startshape = (viewwidth/2, viewheight/2)
=======
        self._playerControl = PlayerControl((self._width, 0), player_no)
        
        #TODO: other buttons
        startpos = self._width/4, self._height/4
        startshape = (self._width/2, self._height/4)
>>>>>>> FETCH_HEAD
        startcolor = (150, 150, 200)
        startButton = GObject(startpos, startshape, startcolor)
        
        dots = []
        lines = []
        boxes = []
        self._objects = {'dots':dots, 'lines':lines, 'boxes':boxes, 'start':startButton}
        
        self._validLines = []
        self._filledBoxes = []
        
        self._currentPlayer = None
        self._player_no = player_no #number of players
        self._players = [] #player list
        
        self._dotSize = 10
        
        lineWidth = int(self._dotSize*0.8)
        lineLength = self._dotSize*10
        
        self._distBetweenDots = lineLength
        
        self._dotcolor = (255,0,0)
        self._dotshape = (self._dotSize, self._dotSize)
        
        self._linecolor = (255,255,255)
        self._linewideshape = (lineLength, lineWidth)
        self._linetallshape = (lineWidth, lineLength)
        
        self._boxcolor = (0, 255, 0)
        self._boxshape = (100-(self._dotSize-1), 100-(self._dotSize-1))

######################## SETUP ##########################
    def setup_board(self):
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
        for y in range(self._columns-1):
            for x in range(self._rows-1):
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
                
    def add_players(self):
        return
                
####################### DRAWING #########################
    def draw(self, view):
        for name in self._objects.keys():
            for obj in self._objects[name]:
                obj.draw(view)

################# GAME LOGIC ###################
    def update(self, mousePos):
        if not self._started:
            if len(self._players == self._player_no):
                self._started = True
                self.setup_board()
            elif self._objects['start'].collide(mousePos) and (len(self._players) >= 2):
                self._started = True
                self.setup_board()
<<<<<<< HEAD
                self._objects.pop('start')
=======
                
            return
        #if game is started, run the logic
>>>>>>> FETCH_HEAD
        else:
            index = self.choose_line(mousePos)
        
                #check if None --> failed choice of click
            if index == None:
<<<<<<< HEAD
                return False
        #if not valid move, line was already chosen
            elif not self.isValid_move(index):
                return False
=======
                return
                #if not valid move, line was already chosen
            elif not self.isValid_move(index):
                return
            
>>>>>>> FETCH_HEAD
            else:
                self._objects['lines'][index].linewidth = 0
                self._validLines.remove(index)
                self.update_boxes(index)
            
                self.game_over()
                return
        
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
        for i, box in enumerate(self._objects['boxes']):
            box.update(index)
            
            if box.isClaimed():
                if i not in self._filledBoxes:
                    self._filledBoxes.append(i)
                    self._players[0].score_inc()
                    print("Score:" + str(self._players[0].get_score()))
    
    def game_over(self):
        if len(self._validLines) == 0:
            self._ended = True
        return self._ended

<<<<<<< HEAD
    def remove_player(self, player):
        if player in self._players:
            self._players.remove(player)
            if len(self._players) == 0:
                self._ended = True
=======
class PlayerControl:
    def __init__(self, pos, player_no):
        
        self.pos = pos
        
        self._currentPlayer = 0
        self._player_no = max(player_no, 2) #number of players
        self._players = [] #player list
        
    def current(self):
        return self._players[self._currentPlayer]
     
    def add_player(self, player):
        if len(self._players) < self._player_no:
            self._players.append(player)
            
    def remove_player(self, player):
        if player in self._players:
            self._players.remove(player)
            
    def next(self):
        self._currentPlayer = (self._currentPlayer + 1) % (self._player_no-1)
        return self.current()
            
    def is_full(self):
        return len(self._players) == self._player_no
    
    def is_empty(self):
        return len(self._players) == 0
    
    def display(self, view):
        vertical_space = 0
        for player in self._players:
            text = player._name + ": " + str(player._score)
            x,y = self.pos
            y = vertical_space
            obj = Text(text, (0,0,0), 40)
            if player == self.current():
                obj.draw(view, x, y)
            else:
                obj.draw(view, x, y)
            vertical_space += 50
>>>>>>> FETCH_HEAD
        
    def add_player(self, player):
        #allow adding players
        if not self._started:
            if len(self._players) < self._player_no:
                self._players.append(player)
            
