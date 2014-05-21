from network import Listener, Handler, poll
from random import randint
from time import sleep
from Viewport import FixedViewport
from Board import Board
from Player import Player

global VIEWPORT
VIEWPORT = FixedViewport(900, 600)

global board
board = Board(VIEWPORT.width, VIEWPORT.height, 6, 6, 5)


def broadcast(msg):
    for h in handlers.keys():
        h.do_send(msg)

class TempServer:

	def __init__(self):
		pass

	def on_open(self):
		handlers[self] = None
		print "connected to server"

	def on_close(self):
		name = handlers[self]
        del handlers[self]
        print "disconnected from server"

	def on_msg(self):
		if 'join' in msg:
			if board.add_player(handlers[self]):
				board.add_player(handlers[self])
				name = msg['join']
				handlers[self] = name
				broadcast({'join': name, 'users': handlers.values()})
			else:
				pass
		elif 'quit' in msg:
			del handlers[self]
			broadcast({'leave': name})
		elif event.type == pygame.MOUSEBUTTONDOWN:
			board.update(event.pos)



'''
on_open():
	print "connected to server"

on_close():
	delete all players from handler list
	print "disconnected from server"

on_msg():
	-if client joins:
		-if >5: 
			- fails -> ignore
		-else: (add_player == True)
			-add to game board & handler list 
	-elif quit:
		- delete player from handler list

	-elif mousePos:
		-check current_player == id:
			- board.update(mousePos)
			- send board to all clients (broadcast)
'''

##create a generate color and generate name for the players