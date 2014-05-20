


"""
Server master:
The server is almighty. 
Every frame, it receives player inputs from clients,
executes these inputs to update the game state,
and sends the whole game state to all the clients for display. 
"""
from __future__ import division # So to make division be float instead of int
from network import Listener, Handler, poll
from random import randint
from time import sleep


     
################### network ##############

handlers = {}

def broadcast(msg):
    for h in handlers.keys():
        h.do_send(msg)

class MyHandler(Handler):
        
    def on_open(self):
        handlers[self] = None
        
    def on_close(self):
        name = handlers[self]
        del handlers[self]
        broadcast({'leave': name, 'users': handlers.values()})
        
    def on_msg(self, msg):
        if 'join' in msg:
            name = msg['join']
            handlers[self] = name
            broadcast({'join':name, 'users': handlers.values()})

    

server = Listener(8888, MyHandler)

######################### loop #######################

while 1:
    poll(0.05)
