"""
@author: Sofanah
"""
import time
import pygame
from pygame.locals import KEYDOWN, K_BACKSPACE, K_RETURN
import string

class GetIP:

	def __init__(self, height, width):
		self._height = height
		self._width = width
		self.IPtext = ""
	
	def get_key(self):
		while True:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				return event.key
			elif event.type == pygame.QUIT:
				exit()
			else:
				pass

	def draw(self, view):
		tfont = pygame.font.Font(None, 20)
		pygame.draw.rect(view, (0,0,0), ((self._width/2)-100, (self._height/2)-10, 200,20), 0)
		pygame.draw.rect(view, (255,255,255), ((self._width/2)-102, (self._height/2)-12, 204,24), 1)
		view.blit(tfont.render("IP address: "+ self.IPtext, 1, (255,0,0)), ((self._width/ 2) - 100, (self._height/ 2) - 10))
		pygame.display.update()

	def get_ip(self,view):
		IP = []
		self.IPtext = ""
		self.draw(view)
		while True:
			time.sleep(0.2)
			inputkey = self.get_key()
			if inputkey == K_BACKSPACE:
				IP = IP[0:-1]
			elif inputkey == K_RETURN:
				break
			elif inputkey <=127:
				IP.append(chr(inputkey))

			self.IPtext = (string.join(IP,""))
			self.draw(view)
		return self.IPtext


# pygame.init()
# screen = pygame.display.set_mode((320,240))
# start = GetIP(screen, 320, 240)

# print (start.get_ip())
