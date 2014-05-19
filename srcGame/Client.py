'''
@author: Chris
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
        
client = Client('localhost', 8888)  # connect asynchronously

while 1:
    #if menu
    
    #if offline
    
    #if joining lobby
    
    #if in lobby
    
    #if in offline game
    
    #if in online game
    