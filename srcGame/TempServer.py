

class TempServer:

	def __init__(self):
		pass

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