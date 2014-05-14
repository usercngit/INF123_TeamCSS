'''
@author: Chris
'''

'''
@author: Chris
@author: Sofanah
@author: Shibani
'''

import pygame
import Viewport

pygame.init()
GAMECLOCK = pygame.time.Clock()
FRAMERATE = 40
VIEWPORT = Viewport.Viewport(60, 60)

sleft = VIEWPORT.window.subsurface((0,0,100,200))
sright = VIEWPORT.window.subsurface((100,0,100,200))
VIEWPORT.window.fill((200,200,150))

######################################################################
def processInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

######################################################################
pygame.init()
while True:
    processInput()
    VIEWPORT.render("model")
    GAMECLOCK.tick(50)
        