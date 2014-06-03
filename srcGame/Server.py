from network import Listener, Handler, poll
from random import randint
from time import sleep
from Board import Board
from Player import Player
from Lobby import Lobby 

GAMESCREENSIZE = 1000, 650
GAMEBOARDSIZE = 7,8
GAMEPLAYERMAX = 5

event_queue = []
clients= {}

games = {} #all hosted games  "gamename":game

lobbyclients = [] #handler only
gameclients = {} #"handler":gamename

def broadcastAll(msg, ignore = ''):
	for client in clients.keys():
		if client != ignore:
			client.do_send(msg)
		
def broadcastGame(gamename, msg, ignore = ''):
	for client, value in gameclients.items():
		if value == gamename:
			if client != ignore:
				client.do_send(msg)
	
def broadcastLobby(msg, ignore = ''):
	for client in lobbyclients:
		if client != ignore:
			client.do_send(msg)
		
player_id = 0
def generate_name():
	global player_id
	player_id += 1
	return 'Anonymous' + str(player_id)

def generate_color():
	R = randint(5,250)
	G = randint(5,250)
	B = randint(5,250)
	return (R, G, B)

class TempServer(Handler):

	def on_open(self):
		print str(self) + "connected to server"
		event_queue.append(('join', self))

	def on_close(self):
		print str(self) + "disconnected from server"
		event_queue.append(('quit', self))

	def on_msg(self, msg):
		event_queue.append((msg['input'], self))

server = Listener(8888, TempServer)

#global board
#board = Board(900, 600, 6, 6, 5)

global lobby 
lobby = Lobby(GAMESCREENSIZE[0], GAMESCREENSIZE[1])

while 1:
	
	# enqueue the player events received by the client handlers
	poll()
	
	# apply events onto game state
	for event, handler in event_queue: 
		if event == 'quit':
			if handler in gameclients.keys():
				gamename = gameclients[handler]
				
				#if a player remove returns true, game is empty, end it
				if games[gamename].remove_player(clients[handler]):
					#remove button from game
					lobby.remove_game(gamename)
					del games[gamename]
				else:
					#update other's boards to reflect missing player
					msg = {'type':'update', 'board':{'players':games[gamename].getasdict('players')}, 'state':games[gamename]._started}
					broadcastGame(gamename, msg, handler)
					
				#delete game from game clients
				del gameclients[handler]
				
			if handler in lobbyclients:
				lobbyclients.remove(handler)
			
			del clients[handler]
			
		elif event == 'join':
			#generate Name and Color
			name = generate_name()
			color = generate_color()
			#generate new player and add to client list
			newPlayer = Player(name, color)
			clients[handler] = newPlayer
			#add to lobby and send initial lobby message
			lobbyclients.append(handler)
			lobbymsg = {'type':'init', 'lobby':lobby.to_list(), 'yourname':name}
			handler.do_send(lobbymsg)
			
		#INPUT EVENTS
		#an escape input will apply to anyone in a game, sending them back to the lobby	
		elif event == 'escapepress':
			if handler in gameclients.keys():
				#remove from game
				gamename = gameclients[handler]
				#if a player remove returns true, game is empty, end it
				if games[gamename].remove_player(clients[handler]):
					#remove button from game
					lobby.remove_game(gamename)
					del games[gamename]
				else:
					#update other's boards to reflect missing player
					msg = {'type':'update', 'board':{'players':games[gamename].getasdict('players')}, 'state':games[gamename]._started}
					broadcastGame(gamename, msg, handler)
					
					if not games[gamename]._started:
						if not lobby.has(gamename):
							lobby.add_button(gamename)
					
				del gameclients[handler]
				
				#add to lobby and send initial lobby message
				lobbyclients.append(handler)
				lobbymsg = {'type':'init', 'lobby':lobby.to_list()}
				broadcastLobby(lobbymsg)
			
		else:
			#FOR HANLDER IN LOBBY
			if handler in lobbyclients:
				#lobby.update returns either "Create Game" or "Game# X"
				update = lobby.update(event)
				
				#CREATE GAME GASE
				if update == "Create Game":
					#lobby.add_game returns either "" or "Game# X"
					value = lobby.add_game()
					if value != "":
						#remove client from lobby
						lobbyclients.remove(handler)
						#add to game list
						gameclients[handler] = value
						
						#create the new game
						newgame = Board(GAMESCREENSIZE[0], GAMESCREENSIZE[1], GAMEBOARDSIZE[0], GAMEBOARDSIZE[1], GAMEPLAYERMAX)
						newgame.add_player(clients[handler])
						#add game to server list of games
						games[value] = newgame
						
						#then send the person joining the current game as an initial board
						msg = {'type':'init', 'board':newgame.to_list(), 'state':games[value]._started}
						handler.do_send(msg)
						
						msg = {'type':'update', 'lobby':lobby.to_list()}
						broadcastLobby(msg)
				#CREATE GAME END
				
						
				#JOIN GAME CASE
				elif update != None and update[0:4] == "Game":
					#returns true if successful add, while also adding player to game
					if games[update].add_player(clients[handler]):
						lobbyclients.remove(handler)
						gameclients[handler] = update
						
						#then send the person joining the current game as an initial board
						msg = {'type':'init', 'board':games[update].to_list(), 'state':games[update]._started}
						handler.do_send(msg)
						
						msg['type'] = 'update'
						broadcastGame(update, msg, handler)
					
					if games[update]._started or games[update].is_full():
						lobby.remove_game(update)
						
						msg = {'type':'update', 'lobby':lobby.to_list()}
						broadcastLobby(msg)
				#JOIN GAME END
				
					
			#FOR HANLDER IN GAME
			elif handler in gameclients.keys():
				gamename = gameclients[handler]
				#handle start
				if not games[gamename]._started:
					#make sure only to take input from the first player to join (player1)
					if clients[handler] == games[gamename]._playerControl._players[0]:
						#handle input aka, let P1 start
						if games[gamename].update(event):
							msg = {'type':'update',\
									'board':{'players':games[gamename].getasdict('players'),\
												'dots':games[gamename].getasdict('dots'),\
												'lines':games[gamename].getasdict('lines'),\
												'boxes':games[gamename].getasdict('boxes'),\
												'buttons':games[gamename].getasdict('buttons')}, 'state':games[gamename]._started }
							broadcastGame(gamename, msg)
							
							lobby.remove_game(gamename)
							msg = {'type':'update', 'lobby':lobby.to_list()}
							broadcastLobby(msg)
			
				elif clients[handler] == games[gamename].current_player():
					#handle input if is the client's turn
						if games[gamename].update(event):
							msg = {'type':'update',\
									'board':{'players':games[gamename].getasdict('players'),\
												'lines':games[gamename].getasdict('lines'),\
												'boxes':games[gamename].getasdict('boxes')}, 'state':games[gamename]._started } 
							broadcastGame(gamename, msg)
						
		#end of event_queue events
			
	event_queue = []
	
	#msg = {'board': board.to_list(), 'started':board._started, 'ended':board.game_over()}
	#broadcast(msg)
		
		
	sleep(1. / 20)  # seconds
