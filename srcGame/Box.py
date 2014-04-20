'''
@author: Chris
@author: Sofanah
@author: Shibani
'''

class Box:
    def __init__ (self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.filled = False
        self.owner = None
        
    