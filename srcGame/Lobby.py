from GObject import Button
from random import randint
global number
from Board import Board

class Lobby:

	def __init__(self, width, height):
		number = 0

		self._width = width
		self._height = height

		self._x = self._width/4
		self._y = self._height/4

		createpos = 0,0
		createshape = self._width, self._height
		createcolor = (150, 150, 200)
		createGameButton = Button(createpos, createshape, createcolor, 0, "Create Game", (0,0,0), 32)

		newGame = Board(900, 600, 6, 6, 5)

		self._buttons = {createGameButton: newGame}


	def add_game(self, game):
		if len(self._buttons) < 11:
			number += 1

			gamepos = self._x
			gameshape = self._y

			self._y += 50

			gamecolor = (150, 150, 200)
        	gameButton = Button(gamepos, gameshape, gamecolor, 0, "Game# " + str(number), (0,0,0), 32) 

        	self._buttons[gameButton] = game
        	return True
		return False

	def remove_game(self, game):
		for key, value in self._buttons.items():
			if value == game:
				del self._buttons[key]

	def is_full(self):
		return len(self._buttons) == 11 

	def is_empty(self):
		return len(self._buttons) == 1

	def draw(self, view):
		for key in self._buttons.keys():
			key.draw(view)

	def to_list(self):
		buttons = []

		for button in self._buttons.keys():
			s = button.to_list()
			buttons.append(s)

		return {'buttons': buttons}

	#create game button (send message and server will add that game to the list of games)
	#game just as temp server
	#send something that the client can draw(buttons) (just like player is set up with GObjects)
	#gets click from player and if collides (button) --> get name of button 

