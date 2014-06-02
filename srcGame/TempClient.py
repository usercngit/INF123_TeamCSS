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

VIEWPORT = FixedViewport(900, 600)
FRAMERATE = 40

IPwindow = GetIP(900, 600)

view = VIEWPORT.window
clock = Clock()

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
		
		self.drawObj('buttons', view)
	
	def drawObj(self, name, view):
		for obj in self._objects[name]:
			obj.draw(view)
			
class lobbyRep:
	def __init__(self):
		self.objects = {'buttons':[]}
		
	def add(self, obj):
		self.objects['buttons'].append(obj)
		
	def replace(self, objlist):
		self.objects['buttons'] = objlist
		
	def draw(self, view):
		self.drawObj('buttons', view)
	
	def drawObj(self, name, view):
		for obj in self._objects[name]:
			obj.draw(view)

class Client(Handler):
	
	def __init__(self, host, port):
		Handler.__init__(self, host, port)
		print 'client built'

	def on_open(self):
		global board
		global lobby
		
		print 'opened'

	def on_msg(self, data):
		#init and update are split, as to help in the reduction in the amount the server should ever have to send
		#init will be sent to the client whenever they initially join a lobby or game
		if data['type'] == 'init':
			if 'board' in data:
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

			elif 'lobby' in data:
				lobby = lobbyRep()
				
				for dic in data['lobby']:
					for item in data['lobby'][dic]:
						obj = Button(item['pos'], item['shape'], item['color'], item['linewidth'], item['text'], item['textColor'], item['textSize'])
						lobby.add(obj)
			
		elif data['type'] == 'update':
			if 'board' in data:
				for dic in data['board']:
					for item in data['board'][dic]:
						if dic == 'buttons':
							obj = Button(item['pos'], item['shape'], item['color'], item['linewidth'], item['text'], item['textColor'], item['textSize'])
						elif dic == 'players':
							obj = Text(item['pos'], item['text'], item['color'], item['size'])
						else:
							obj = GObject(item['pos'], item['shape'], item['color'], item['linewidth'])
			elif 'lobby' in data:
				for dic in data['lobby']:
					for item in data['lobby'][dic]:
						obj = Button(item['pos'], item['shape'], item['color'], item['linewidth'], item['text'], item['textColor'], item['textSize'])

thisip = IPwindow.get_ip(view)
client = Client(thisip, 8888)  # connect asynchronously
	
while 1:
	
	poll()
	
	for event in get_pygame_events():  
		if event.type == QUIT:
			msg = {'input': "quit"}
			client.do_send(msg)
			exit()
		if event.type == MOUSEBUTTONDOWN:
			msg = {'input': event.pos}
			client.do_send(msg)
		elif event.type == KEYDOWN:
			msg = {'input': "escape"}
			client.do_send(msg)
			
	pygame.display.update()
	clock.tick(FRAMERATE)
	