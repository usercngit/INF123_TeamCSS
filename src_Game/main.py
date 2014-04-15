import GameScreen
import GameBoard

import pygame

pygame.init()

g = GameBoard.GameBoard(4,4)
while True:
	g.create_dots()
	pygame.display.update()

	g.run()
	pygame.display.update()