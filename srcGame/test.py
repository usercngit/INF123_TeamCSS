import pygame

screen = pygame.display.set_mode((200,200))
line1 = pygame.Rect(1,1,40,5)
line2 = pygame.Rect(1,1,5,40)
line3 = pygame.Rect(41,1,5,40)
line4 = pygame.Rect(1,41,40,5)
    
line5 = pygame.Rect(41,1,40,5)
line6 = pygame.Rect(81,1,5,40)
line7 = pygame.Rect(41,41,40,5)
    
box1 = (line1, line2, line3, line4)
box2 = (line5, line3, line6, line7)
    
while True:

    screen.fill((255,255,255))
    pygame.draw.rect(screen, (200,200,200), line1)
    pygame.draw.rect(screen, (200,200,200), line2)
    pygame.draw.rect(screen, (200,200,200), line3)
    pygame.draw.rect(screen, (200,200,200), line4)
    pygame.draw.rect(screen, (200,200,200), line5)
    pygame.draw.rect(screen, (200,200,200), line6)
    pygame.draw.rect(screen, (200,200,200), line7)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = event.pos
                    
                    if(x < 45 and x > 35 and y > 0 and y < 42):
                        
                        line3 = pygame.Rect(0,0,0,0)
    
    
    print box1                         
