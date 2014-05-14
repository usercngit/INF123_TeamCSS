'''
@author: Chris
@author: Sofanah
@author: Shibani
'''

class Player:
	
	def __init__(self, name, color):
		self._name = name 
		self._color = color
		self._score = 0
		
	def score_inc(self):
		self._score +=1
	
	def get_color(self):
		return self._color

	def get_score(self):
		return self._score
		