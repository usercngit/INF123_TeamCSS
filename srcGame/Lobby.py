from GObject import Text
import Board

class Lobby:

	def __init__(self, pos, games_no):
		self._pos = pos
		self._game_chosen = None
		self._game_no = min(len(games_no),10)
		self._games = []
		self._string = "Game# " + str(random.randint(1, 1000))
        self._rep = Text((0,0), string, (0,0,0), 40)

	def add_game(self, game):
		if len(self._games) < self._game_no:
			x, y = self._pos
			self._rep.pos = (x, (50*len(self._games)))
			if self.is_empty():
				self.set_color()
			self._games.append(game)
			return True
		return False

	def remove_game(self, game):
		if game in self._games:
			self._games.remove(game)

	def is_full(self):
		return len(self._games) == self._game_no 

	def is_empty(self):
		return len(self._games) == 0
	
	def set_color(self):
        r = lambda: random.randint(0,255)
        self._rep.color = '(%02X, %02X, %02X)' % (r(),r(),r()))

	def display(self, view):
		for game in self._games:
			game.draw(view)