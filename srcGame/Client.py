'''
@author: Chris
@author: Sufana
@author: Shibani
'''
"""
The Client is slave: 
- it sends only the player inputs to the server.
- every frame, it displays the server's last received data
Pros: the server is the only component with game logic, 
so all clients see the same game at the same time (consistency, no rollbacks).
Cons: lag between player input and screen display (one round-trip).
But the client can smooth the lag by interpolating the position of the boxes. 
"""
from network import Handler, poll
    
class Client(Handler):
            
    def on_msg(self, data):
        pass

"""
0 = mainmenu
1 = lobby
2 = offline game
3 = online game
"""
GAMESTATE = 0
client = None
#client = Client('localhost', 8888)  # connect asynchronously

while 1:
    #if menu
        
    
    #if joining lobby
    
    #if in lobby
    
    #if in offline game
    
    #if in online game
    