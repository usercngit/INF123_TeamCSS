### network imports ###
from network import Handler, poll

### pygame imports ###
import pygame
from pygame.event import get as get_pygame_events
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN
from pygame.locals import K_ESCAPE
from pygame.time import Clock

pygame.init()

### local imports ###
from GObject import Button, GObject, Text
from Viewport import FixedViewport
from GetIP import GetIP

viewx = 1000
viewy = 650

VIEWPORT = FixedViewport(viewx, viewy)
FRAMERATE = 40

IPwindow = GetIP(viewx, viewy)

view = VIEWPORT.window
clock = Clock()

global lobby
global board

global MODE
global GAMESTATE
global NAME
global CONNECTED
NAME = ""
MODE = ''
GAMESTATE = False
CONNECTED = False

#*************** LIGHT MODEL *******************
class boardRep:
	def __init__(self):
		self.objects = {'backgrounds':[], 'players':[], 'boxes':[], 'lines':[], 'dots':[], 'buttons':[]}
		
	def add(self, objtype, obj):
		self.objects[objtype].append(obj)
		
	def replace(self, objtype, objectlist):
		self.objects[objtype] = objectlist
		
	def draw(self, view):
		self.drawObj('backgrounds', view)
		
		self.drawObj('players', view)
		
		self.drawObj('boxes', view)
		self.drawObj('lines', view)
		self.drawObj('dots', view)
		
		if not GAMESTATE:
			self.drawObj('buttons', view)
	
	def drawObj(self, name, view):
		for obj in self.objects[name]:
			obj.draw(view)
			
class lobbyRep:
	def __init__(self):
		self.objects = {'buttons':[]}
		
	def add(self, obj):
		self.objects['buttons'].append(obj)
		
	def replace(self, objlist):
		self.objects['buttons'] = objlist
		
	def draw(self, view):
		view.fill((0,0,0))
		self.drawObj('buttons', view)
	
	def drawObj(self, name, view):
		for obj in self.objects[name]:
			obj.draw(view)

class Client(Handler):
	
	def __init__(self, host, port):
		Handler.__init__(self, host, port)

	def on_open(self):
		global CONNECTED
		CONNECTED = True

	def on_msg(self, data):
		global NAME
		global GAMESTATE
		global MODE
		global board
		global lobby
		#init and update are split, as to help in the reduction in the amount the server should ever have to send
		#init will be sent to the client whenever they initially join a lobby or game
		if data['type'] == 'init':
			if 'board' in data:
				MODE = 'game'
				board = boardRep()
				
				for dic in data['board']:
					for item in data['board'][dic]:
						if dic == 'buttons':
							obj = Button(item['pos'], item['shape'], item['color'], item['linewidth'], item['text'], item['textColor'], item['textSize'])
							board.add(dic, obj)
						elif dic == 'players':
							obj = Text(item['pos'], item['text'], item['color'], item['size'])
							board.add(dic, obj)
						else:
							obj = GObject(item['pos'], item['shape'], item['color'], item['linewidth'])
							board.add(dic, obj)
							
				#if state message is true, game has started.  Stop drawing button
				if data['state'] == True:
					GAMESTATE = True

			elif 'lobby' in data:
				MODE = 'lobby'
				GAMESTATE = False
				lobby = lobbyRep()
				for dic in data['lobby']:
					for item in data['lobby'][dic]:
						obj = Button(item['pos'], item['shape'], item['color'], item['linewidth'], item['text'], item['textColor'], item['textSize'])
						lobby.add(obj)
						
				if 'yourname' in data:
					NAME = data['yourname']
			
		elif data['type'] == 'update':
			if 'board' in data:
				for dic in data['board']:
					templist = []
					for item in data['board'][dic]:
						if dic == 'buttons':
							obj = Button(item['pos'], item['shape'], item['color'], item['linewidth'], item['text'], item['textColor'], item['textSize'])
							templist.append(obj)
						elif dic == 'players':
							obj = Text(item['pos'], item['text'], item['color'], item['size'])
							templist.append(obj)
						else:
							obj = GObject(item['pos'], item['shape'], item['color'], item['linewidth'])
							templist.append(obj)
						
					if len(templist) > 0:
						board.replace(dic, templist)
						
				if data['state'] == True:
					GAMESTATE = True
						
			elif 'lobby' in data:
				MODE = 'lobby'
				GAMESTATE = False
				for dic in data['lobby']:
					templist = []
					for item in data['lobby'][dic]:
						obj = Button(item['pos'], item['shape'], item['color'], item['linewidth'], item['text'], item['textColor'], item['textSize'])
						templist.append(obj)
						
					if len(templist) > 0:
						lobby.replace(templist)
						
thisip = IPwindow.get_ip(view)
view.fill((0,0,0))
client = Client(thisip, 8888)  # connect asynchronously
	
while 1:
	
	poll()
	
	for event in get_pygame_events():  
		if event.type == QUIT:
			exit()
		if event.type == MOUSEBUTTONDOWN:
			msg = {'input': event.pos}
			client.do_send(msg)
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				msg = {'input': "escapepress"}
				client.do_send(msg)
	
	if MODE == 'lobby':
		lobby.draw(view)
	elif MODE == 'game':
		board.draw(view)
			
	pygame.display.update()
	clock.tick(FRAMERATE)
	