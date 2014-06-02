from GObject import Button
number = 0

class Lobby:

	def __init__(self, width, height):
		self._buttons = []

		self._width = width
		self._height = height

		self._x = self._width/6
		self._y = self._height/6

		createpos = 0,0
		createshape = self._width/6, self._height/6
		createcolor = (150, 150, 200)
		createGameButton = Button(createpos, createshape, createcolor, 0, "Create Game", (0,0,0), 32)

		self._buttons.append(createGameButton)

	def add_game(self):
		print(len(self._buttons))
		if len(self._buttons) < 11:
			global number
			number += 1

			# gamepos = self._x, 50*len(self._buttons)#self._y
			gamepos = self._x, 50*len(self._buttons)
			gameshape = self._width/6, self._height/9

			# self._y += 50

			gamecolor = (150, 150, 200)
			gameButton = Button(gamepos, gameshape, gamecolor, 0, "Game# " + str(number), (0,0,0), 32) 

			self._buttons.append(gameButton)
			return gameButton.text
		return ""

	def remove_game(self, button_text):
		for button in self._buttons:
			if button.text == button_text:
				self._buttons.remove(button)

		for button in self._buttons[1:]:
			gamepos = self._x, 50*((self._buttons.index(button)))
			button.new_pos(gamepos)


	def is_full(self):
		return len(self._buttons) == 11 

	def is_empty(self):
		return len(self._buttons) == 1

	def to_list(self):
		buttons = []

		for button in self._buttons:
			s = button.to_list()
			buttons.append(s)

		return {'buttons': buttons}

	def update(self, mousePos):
		for button in self._buttons:
			if button.collide(mousePos):
				print button.text
				return button.text		#'Create Game' or 'Game# n'

	def draw(self, view):
		for button in self._buttons:
			button.draw(view)
			# print button.pos

	#create game button (send message and server will add that game to the list of games)
	#game just as temp server
	#send something that the client can draw(buttons) (just like player is set up with GObjects)
	#gets click from player and if collides (button) --> get name of button 

