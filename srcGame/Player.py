'''
@author: Chris
@author: Sofanah
@author: Shibani
'''
from GObject import Text

class Player:
	
	def __init__(self, name, color, score = 0):
		self._name = name 
		self._color = color
		self._score = score
		string = name + ": " + str(score)
		self._rep = Text((0,0), string, (0,0,0), 40)
		
	def to_list(self):
		return self._rep.to_list()
		
	def score_inc(self):
		self._score +=1
		self._rep.text = self._name + ": " + str(self._score)
		
	def set_color(self, color):
		self._rep.color = color
	
	def draw(self, view):
		self._rep.draw(view)
		