from network import Handler, poll
from pygame.event import get as get_pygame_events
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, MOUSEBUTTONDOWN

from Board import Board
from Viewport import FixedViewport

VIEWPORT = FixedViewport(900, 600)
GAMEBOARD = None


class Client(Handler):
	
	def on_msg(self, data):
		global GAMEBOARD
		GAMEBOARD = data['board']

client = Client('localhost', 8888)  # connect asynchronously

while 1:
	
	poll()
	
	#if we've received the gameboard
	if not GAMEBOARD == None:
		for event in get_pygame_events():  
			if event.type == QUIT:
				exit()
			if event.type == KEYDOWN:
				key = event.key
				if key == K_ESCAPE:
					exit()
			if event.type == MOUSEBUTTONDOWN:
				msg = {'input': event.pos}
				client.do_send(msg)
					
					