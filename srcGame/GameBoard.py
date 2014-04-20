"""
@author: Chris
@author: Sofanah
@author: Shibani
"""

import pygame

pygame.init()

#TODO
    # Size
    # board objects
class GameBoard:
    def __init__(self, rows, columns, screen):
        self._rows = rows
        self._columns = columns
        self._screen = screen
        self._dots = []
        self._lines = []
        self._boxes = []
        self.create_dots()
        #self.create_lines()
        
        self._dotcolor = (255,0,0)
        self._dotshape = (10, 10)
        
        self._linecolor = (100,100,255)
        self._linewideshape = (100, 10)
        self._linetallshape = (10, 100)
    
    def draw_dots(self):
        for x in range(self._columns):
            for y in range(self._rows):
                if (x== self._columns-1 and y== self._rows-1):
                    pygame.draw.rect(self._screen, (255,0,0), ((x+1)*100, (y+1)*100-4, 10, 10), 0)

                    break
                    
                elif(x == self._columns-1):
                    pygame.draw.line(self._screen, (255, 255, 255), ((x+1)*100+4, (y+1)*100), ((x+1)*100+4, (y+2)*100), 10)#vertical
                
                elif(y== self._rows-1):
                    pygame.draw.line(self._screen, (255, 255, 255), ((x+1)*100, (y+1)*100), ((x+2)*100, (y+1)*100), 10)#horizontal
                
                
                else:
                    pygame.draw.line(self._screen, (255, 255, 255), ((x+1)*100+4, (y+1)*100), ((x+1)*100+4, (y+2)*100), 10)#vertical
                    pygame.draw.line(self._screen, (255, 255, 255), ((x+1)*100, (y+1)*100), ((x+2)*100, (y+1)*100), 10)#horizontal
                pygame.draw.rect(self._screen, (255,0,0), ((x+1)*100, (y+1)*100-4, 10, 10), 0)


    def run(self): #only with a 3x3 (in  terms of boxes) --> 4x4 (in terms of dots)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = event.pos        
                            
                    #first row
                    if((x <= 200) and (x >= 100) and (y <= 106) and (y >=96)):
                        pygame.draw.line(self._screen, (0,0,255), (100,100), (200,100), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 300) and (x >= 200) and (y <= 106) and (y >=96)):
                        pygame.draw.line(self._screen, (0,0,255), (200,100), (300,100), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 400) and (x >= 300) and (y <= 106) and (y >=96)):
                        pygame.draw.line(self._screen, (0,0,255), (300,100), (400,100), 10) #horizontal
                        pygame.display.flip()
                
                    #second row
                    elif((x <= 200) and (x >= 100) and (y <= 206) and (y >=196)):
                        pygame.draw.line(self._screen, (0,0,255), (100,200), (200,200), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 300) and (x >= 200) and (y <= 206) and (y >=196)):
                        pygame.draw.line(self._screen, (0,0,255), (200,200), (300,200), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 400) and (x >= 300) and (y <= 206) and (y >=196)):
                        pygame.draw.line(self._screen, (0,0,255), (300,200), (400,200), 10) #horizontal
                        pygame.display.flip()
                    
                    #third row
                    elif((x <= 200) and (x >= 100) and (y <= 306) and (y >=296)):
                        pygame.draw.line(self._screen, (0,0,255), (100,300), (200,300), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 300) and (x >= 200) and (y <= 306) and (y >=296)):
                        pygame.draw.line(self._screen, (0,0,255), (200,300), (300,300), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 400) and (x >= 300) and (y <= 306) and (y >=296)):
                        pygame.draw.line(self._screen, (0,0,255), (300,300), (400,300), 10) #horizontal
                        pygame.display.flip()
                    
                    #fourth row
                    elif((x <= 200) and (x >= 100) and (y <= 406) and (y >=396)):
                        pygame.draw.line(self._screen, (0,0,255), (100,400), (200,400), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 300) and (x >= 200) and (y <= 406) and (y >=396)):
                        pygame.draw.line(self._screen, (0,0,255), (200,400), (300,400), 10) #horizontal
                        pygame.display.flip()
                    elif((x <= 400) and (x >= 300) and (y <= 406) and (y >=396)):
                        pygame.draw.line(self._screen, (0,0,255), (300,400), (410,400), 10) #horizontal #extra 10
                        pygame.display.flip()
                        
                    #first column
                    elif((x <= 110) and (x >= 100) and (y >= 106) and (y <= 196)):
                        pygame.draw.line(self._screen, (0,0,255), (104,96), (104,196), 10) #veritcal 
                        pygame.display.flip()
                    elif((x <= 110) and (x >= 100) and (y >= 206) and (y <= 296)):
                        pygame.draw.line(self._screen, (0,0,255), (104,196), (104,296), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 110) and (x >= 100) and (y >= 306) and (y <= 396)):
                        pygame.draw.line(self._screen, (0,0,255), (104,296), (104,396), 10) #vertical
                        pygame.display.flip()
                    
                    #second column
                    elif((x <= 210) and (x >= 200) and (y >= 106) and (y <= 196)):
                        pygame.draw.line(self._screen, (0,0,255), (204,96), (204,196), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 210) and (x >= 200) and (y >= 206) and (y <= 296)):
                        pygame.draw.line(self._screen, (0,0,255), (204,196), (204,296), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 210) and (x >= 200) and (y >= 306) and (y <= 396)):
                        pygame.draw.line(self._screen, (0,0,255), (204,296), (204,396), 10) #vertical
                        pygame.display.flip()
                        
                    #third column
                    elif((x <= 310) and (x >= 300) and (y >= 106) and (y <= 196)):
                        pygame.draw.line(self._screen, (0,0,255), (304,96), (304,196), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 310) and (x >= 300) and (y >= 206) and (y <= 296)):
                        pygame.draw.line(self._screen, (0,0,255), (304,196), (304,296), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 310) and (x >= 300) and (y >= 306) and (y <= 396)):
                        pygame.draw.line(self._screen, (0,0,255), (304,296), (304,396), 10) #vertical
                        pygame.display.flip()

                    #fourth column
                    elif((x <= 410) and (x >= 400) and (y >= 106) and (y <= 196)):
                        pygame.draw.line(self._screen, (0,0,255), (404,96), (404,196), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 410) and (x >= 400) and (y >= 206) and (y <= 296)):
                        pygame.draw.line(self._screen, (0,0,255), (404,196), (404,296), 10) #vertical
                        pygame.display.flip()
                    elif((x <= 410) and (x >= 400) and (y >= 306) and (y <= 396)):
                        pygame.draw.line(self._screen, (0,0,255), (404,296), (404,396), 10) #vertical
                        pygame.display.flip()
