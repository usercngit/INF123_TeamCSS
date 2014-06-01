from GObject import Text
import Board

class Lobby:
	def __init__(self, pos, games_no):
		self._pos = pos
		self._game_chosen = None
		self._game_no = min(len(games_no),10)
		self._games = []

	def add_game(self, game):
		if len(self._games) < self._game_no:
			x, y = self._pos
			Board._rep.pos = (x, (50*len(self._games)))
			if self.is_empty():
				Board.set_color()
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

	def display(self, view):
		for game in self._games:
			game.draw(view)