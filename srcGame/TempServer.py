from network import Listener, Handler, poll
from random import randint
from time import sleep
from Board import Board
from Player import Player


event_queue = []
clients= {}

def broadcast(msg):
	for client in clients.keys():
		client.do_send(msg)
		
player_id = 0
def generate_name():
	global player_id
	player_id += 1
	return str(player_id)

def generate_color():
	R = randint(5,250)
	G = randint(5,250)
	B = randint(5,250)
	return (R, G, B) 

class TempServer(Handler):

	def on_open(self):
		event_queue.append(('join', self))

	def on_close(self):
		event_queue.append(('quit', self))

	def on_msg(self, msg):
		event_queue.append((msg['input'], self))

server = Listener(8888, TempServer)

global board
board = Board(900, 600, 6, 6, 5)

while 1:
	
	# enqueue the player events received by the client handlers
	poll()
	
	# apply events onto game state
	for event, handler in event_queue: 
		if event == 'quit':
			#name = clients[handler]._name 
			board.remove_player(clients[handler])
			del clients[handler]
			#broadcast(str(name) + " quit the game")
		elif event == 'join':
			#generate Name and Color
			name = "Player #".__add__(generate_name())
			color = generate_color()
			newPlayer = Player(name, color)
			clients[handler] = newPlayer
			board.add_player(newPlayer)
		else:  # input event
			#handle start
			if not board._started:
				#make sure only to take input from the first player to join (player1)
				if clients[handler] == board._playerControl._players[0]:
					#handle input aka, let P1 start
					board.update(event)
			
			elif clients[handler] == board.current_player():
				#handle input if is the client's turn
					board.update(event)
			
	event_queue = []
	
	msg = {'board': board.to_list(), 'started':board._started, 'ended':board.game_over()}
	broadcast(msg)
		
		
	sleep(1. / 20)  # seconds

##create a generate color and generate name for the players