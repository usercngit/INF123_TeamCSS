from network import Handler, poll
import pygame
from pygame.event import get as get_pygame_events
from pygame.locals import KEYDOWN, QUIT, MOUSEBUTTONDOWN
from pygame.time import Clock

pygame.init()

from GObject import Button, GObject, Text
from Viewport import FixedViewport

VIEWPORT = FixedViewport(900, 600)
FRAMERATE = 40

view = VIEWPORT.window
clock = Clock()

class Client(Handler):
	
	def on_msg(self, data):
		global STARTED, ENDED
		STARTED = data['started']
		ENDED = data['ended']
		
		for back in data['board']['backgrounds']:
			#print back
			ba = GObject(back['pos'], back['shape'], back['color'], back['linewidth'])
			ba.draw(view)
			
		for player in data['board']['players']:
			#print player
			pl = Text(player['pos'], player['text'], player['color'], player['size'])
			pl.draw(view)
		
		for box in data['board']['boxes']:
			#print box
			bo = GObject(box['pos'], box['shape'], box['color'], box['linewidth'])
			bo.draw(view)
			
		for line in data['board']['lines']:
			#print line
			li = GObject(line['pos'], line['shape'], line['color'], line['linewidth'])
			li.draw(view)
			
		for dot in data['board']['dots']:
			#print dot
			do = GObject(dot['pos'], dot['shape'], dot['color'], dot['linewidth'])
			do.draw(view)
			
		for button in data['board']['buttons']:
			#print button
			bu = Button(button['pos'], button['shape'], button['color'], button['linewidth'], button['text'], button['textColor'], button['textSize'])
			bu.draw(view)
			

client = Client('localhost', 8888)  # connect asynchronously

while 1:
	
	poll()
	
	if 1:
		for event in get_pygame_events():  
			if event.type == QUIT:
				exit()
			if event.type == MOUSEBUTTONDOWN:
				msg = {'input': event.pos}
				client.do_send(msg)
				
	pygame.display.update()
	clock.tick(FRAMERATE)	
	