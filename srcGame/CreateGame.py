"""
@author: Chris
@author: Sofanah
@author: Shibani
"""
import pygame
import GameScreen
from network import Handler, poll
from threading import Thread
import os
import sys
from time import sleep


MAX_PLAYERS = 5
MAX_BOARD_DIMS = 15

dims = 800, 640
RGB = 0,0,0 

myname = raw_input("What is your name? ")

class CreateGame(Handler):

	def __init__(self, online):
		self._online = online #bool
		if self._online:
			Handler.__init__(self, 'localhost', 8888)
			print "Server is connected."
			self._game_type = " Online"
		else:
			self._game_type = " Offline" 
		self._screen = GameScreen.GameScreen(dims, RGB)
		self._number_of_players = 0
		self._rows = 0
		self._columns = 0
		self._theplayers = {}
		self._therows = {}
		self._thecolumns = {}
		self._create_button = None

	def on_close(self):
		print "Server has been closed."
		os._exit(0)

	def on_msg(self, msg):
		if 'join' in msg:
			print '%s joined' % (msg['join'])

	def drawTitle(self):
		font = pygame.font.Font(None, 40)
		label = font.render("Create Game" + self._game_type, 1, (255,0,0))
		textpos = label.get_rect()
		textpos.centerx = self._screen.screen.get_rect().centerx
		self._screen.screen.blit(label, textpos)

	def drawPlayers(self):
		font = pygame.font.Font(None, 40)
		label = font.render("Number of Players: " + str(self._number_of_players), 1, (255,0,0))
		textpos = label.get_rect()
		textpos.centery = (self._screen.screen.get_rect().centery) - 200
		self._screen.screen.blit(label, textpos)

	def drawRows(self):
		font = pygame.font.Font(None, 40)
		label = font.render("Number of Board Rows: " + str(self._rows), 1, (255,0,0))
		textpos = label.get_rect()
		textpos.centery = (self._screen.screen.get_rect().centery) - 100
		self._screen.screen.blit(label, textpos)

	def drawColumns(self):
		font = pygame.font.Font(None, 40)
		label = font.render("Number of Board Columns: " + str(self._columns), 1, (255,0,0))
		textpos = label.get_rect()
		textpos.centery = self._screen.screen.get_rect().centery
		self._screen.screen.blit(label, textpos)

	def drawPlayerNumbers(self):
		font = pygame.font.Font(None, 30)
		for i in range(MAX_PLAYERS):
			label = font.render(str(i+1), 1, (255,255,255))
			self._screen.screen.blit(label, (25+(i*50), 140))
			the_circle = pygame.draw.circle(self._screen.screen, (0,0,255), (30+(i*50),170), 10)
			self._theplayers[i+1] = the_circle

	def drawRowNumbers(self):
		font = pygame.font.Font(None, 30)
		for i in range(MAX_BOARD_DIMS-1):
			label = font.render(str(i+2), 1, (255,255,255))
			if((i+1) < 10):
				self._screen.screen.blit(label, (25+(i*50), 240))
			else:
				self._screen.screen.blit(label, (20+(i*50), 240))
			the_circle = pygame.draw.circle(self._screen.screen, (0,0,255), (30+(i*50),270), 10)
			self._therows[i+2] = the_circle

	def drawColumnNumbers(self):
		font = pygame.font.Font(None, 30)
		for i in range(MAX_BOARD_DIMS-1):
			label = font.render(str(i+2), 1, (255,255,255))
			if((i+1) < 10):
				self._screen.screen.blit(label, (25+(i*50), 340))
			else:
				self._screen.screen.blit(label, (20+(i*50), 340))
			the_circle = pygame.draw.circle(self._screen.screen, (0,0,255), (30+(i*50),370), 10)
			self._thecolumns[i+2] = the_circle

	def drawCreateButton(self):
		the_rect = pygame.Rect(dims[0] - 300, dims[1]-150, 200, 100)
		self._create_button = pygame.draw.rect(self._screen.screen, (0, 255, 0), the_rect, 0)
		font = pygame.font.Font(None, 40)
		label = font.render("Create Game", 1, (255,255,255))
		self._screen.screen.blit(label, (dims[0]-290, dims[1] -115))
	
	def draw(self):
		self._screen.drawWindow()
		self.drawTitle()
		self.drawPlayers()
		self.drawPlayers()
		self.drawRows()
		self.drawColumns()
		self.drawPlayerNumbers()
		self.drawRowNumbers()
		self.drawColumnNumbers()
		self.drawCreateButton()
		pygame.display.update()

	def update(self, mousePos):
		#optimize this
		for k,v in self._theplayers.items():
			if self._theplayers[k].collidepoint(mousePos):
				self._number_of_players = k

		for k,v in self._therows.items():
			if self._therows[k].collidepoint(mousePos):
				self._rows = k

		for k,v in self._thecolumns.items():
			if self._thecolumns[k].collidepoint(mousePos):
				self._columns = k

		if self._create_button.collidepoint(mousePos):
			if (self._number_of_players != 0 and self._rows !=0 and self._columns !=0):
				print "Ready to go to GameMode!"
			else:
				print "Please choose from ALL the options"


#####################################################

def processInput():
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    	    exit()
    	elif event.type == pygame.MOUSEBUTTONDOWN:
    		window.update(event.pos)

####################################################	


def periodic_poll():
	while 1:
		poll()
		sleep(0.05) #seconds

thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()

pygame.init()
global window
window = CreateGame(True)
window.do_send({'join': myname})

while True:
	window.draw()
	processInput()

