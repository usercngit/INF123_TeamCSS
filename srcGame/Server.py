'''
@author: Chris
'''
from __future__ import division # So to make division be float instead of int
from network import Listener, Handler, poll
from random import randint
from time import sleep


##################### network logic #############

     
################### network ##############

event_queue = []  # list of ('event', handler) 
# 'event' can be 'quit', 'join', 'up', 'down', 'left', 'right'

class MyHandler(Handler):
        
    def on_open(self):
        event_queue.append(('join', self))
        
    def on_close(self):
        event_queue.append(('quit', self))
        
    def on_msg(self, data):
        event_queue.append((data['input'], self))
    
server = Listener(8888, MyHandler)

######################### loop #######################

while 1:
    # enqueue the player events received by the client handlers
    poll()
    
    # apply events onto game state
    for event, handler in event_queue: 
        if event == 'quit':
            del players[handler]
        elif event == 'join':
            players[handler] = Player()
        else:  # movement input
            players[handler].change_dir(event)
    event_queue = []
    
    # move everyone and detect collisions
    for player in players.values():  
        player.move()
        for border in borders:  # collision with borders
            if collide_boxes(player.box, border):
                player.revive()
        for p in players.values():  # collision with other players
        # only the player with lowest id of the pair detects the collision
            if player.name < p.name and collide_boxes(player.box, p.box):
                playerw, pw = player.box[2], p.box[2]  # widths
                if playerw > pw:
                    player.grow_and_slow(pw)
                    p.revive()
                elif playerw < pw:
                    p.grow_and_slow(playerw)
                    player.revive()
                else:  # they have same width: kill both 
                    p.revive()
                    player.revive()
        for index, pellet in enumerate(pellets):  # collision with pellets
            if collide_boxes(player.box, pellet):
                player.grow_and_slow()
                pellets[index] = [randint(10, 390), randint(10, 290), 5, 5]
        
    # Send to all players 1) the whole game state, and 2) their own name, 
    # so each player can draw herself differently from the other players.
    serialized_players = {p.name: p.box for p in players.values()}
    for handler, player in players.items():
        msg = {'borders': borders,
               'pellets': pellets,
               'myname': player.name,
               'players': serialized_players}
        handler.do_send(msg)
        
    sleep(1. / 20)  # seconds