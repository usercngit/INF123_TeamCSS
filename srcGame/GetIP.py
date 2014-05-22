"""
@author: Sofanah
"""

import pygame
from pygame.locals import *
import string

class GetIP:

	def __init__(self, window, height, width):
		self._screen = window
		self._height = height
		self._width = width
	
	def get_key(self):
		while True:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				return event.key
			# elif event.type == pygame.QUIT:
			# 	exit()
			else:
				pass

	def draw(self, IP):
		tfont = pygame.font.Font(None, 20)
		pygame.draw.rect(self._screen, (0,0,0), ((self._width/2)-100, (self._height/2)-10, 200,20), 0)
		pygame.draw.rect(self._screen, (255,255,255), ((self._width/2)-102, (self._height/2)-12, 204,24), 1)
		if len(IP) != 0:
			self._screen.blit(tfont.render(IP, 1, (255,0,0)), ((self._width/ 2) - 100, (self._height/ 2) - 10))

		pygame.display.update()

	def get_ip(self):
		IP = []
		self.draw("IP: " + string.join(IP,""))
		while True:
			inputkey = self.get_key()
			if inputkey == K_BACKSPACE:
				IP = IP[0:-1]
			elif inputkey == K_RETURN:
				break
			elif inputkey <=127:
				IP.append(chr(inputkey))

			self.draw("IP address: "+ string.join(IP,""))
		return string.join(IP,"")


# pygame.init()
# screen = pygame.display.set_mode((320,240))
# start = GetIP(screen, 320, 240)

# print (start.get_ip())
