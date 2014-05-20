"""
@author: Sofanah
"""

import pygame
import Viewport
import CreateGame

RGB = 0,0,0

class StartMenu:

	def __init__(self, window, height, width):
		self._screen = window
		self._height = height
		self._width = width
		self._start_locally = None
		self._go_to_lobby = None

	def drawTitle(self):
		font = pygame.font.Font(None, 40)
		label = font.render("Dots and Boxes", 1, (255,0,0))
		textpos = label.get_rect()
		textpos.centerx = self._screen.get_rect().centerx
		self._screen.blit(label, textpos)

	def drawLocalButton(self):
		the_rect = pygame.Rect(self._height - (self._height/1.1), self._width-(self._width/1.7), 200, 100)
		self._start_locally = pygame.draw.rect(self._screen, (0, 255, 0), the_rect, 0)
		font = pygame.font.Font(None, 40)
		label = font.render("Start Local", 1, (255,255,255))
		self._screen.blit(label, (self._height-(self._height/1.17), self._width -(self._width/1.85)))

	def drawGoToLobbyButton(self):
		the_rect = pygame.Rect(self._height - (self._height/30.17), self._width-(self._width/1.7), 200, 100)
		self._go_to_lobby = pygame.draw.rect(self._screen, (0, 255, 0), the_rect, 0)
		font = pygame.font.Font(None, 40)
		label = font.render("Go To Lobby", 1, (255,255,255))
		self._screen.blit(label, (self._height-(self._height/150.17), self._width -(self._width/1.85)))

	def update(self, mousePos):
		if self._start_locally.collidepoint(mousePos):
			return "offline"
			# self._screen.fill(0)
			# global create_local
			# create_local = CreateGame.CreateGame(False, self._screen, self._height, self._width)
			# create_local.draw()

		elif self._go_to_lobby.collidepoint(mousePos):
			return "online"

		return 



#####################################################

# def processInput():
#     for event in pygame.event.get():
#     	if event.type == pygame.QUIT:
#     	    exit()
#     	elif event.type == pygame.MOUSEBUTTONDOWN:
#     		answer = start.update(event.pos)
#     		return answer

####################################################	

# pygame.init()
# VIEWPORT = Viewport.Viewport(60,60)
# VIEWPORT.window.fill((200,200,150))

# global start
# start = StartMenu(VIEWPORT.window, VIEWPORT.height, VIEWPORT.width)
# start.drawTitle()
# start.drawLocalButton()
# start.drawGoToLobbyButton()
# pygame.display.update()
# done = False
# while not done:
# 	answer = processInput()
# 	if answer == "offline" or answer == "online":
# 		done = True
# 	pygame.display.update()

# VIEWPORT.window.fill(0)

# done = False


# if answer == "offline":
# 	global create
# 	create = CreateGame.CreateGame(False, VIEWPORT.window, VIEWPORT.height, VIEWPORT.width)
# 	# create.draw()


# while not done:
# 	# create.draw()
# 	# CreateGame.processInput()
# 	pygame.display.update()
# 	processInput()


	