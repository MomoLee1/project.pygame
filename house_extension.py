import pygame 
# -- Global Constants 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0)
GREEN = (0,255,0) 
LIGHTBLUE = (152,193,229)
DARKBLUE = (5,66,120)
# -- Initialise PyGame
pygame.init() 
# -- Blank Screen 
size = (640,480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("House") 
# -- Exit game flag set to false 
done = False
# -- Initialise sun coordinates
sun_x = 0
sun_y = 100
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock() 

### -- Game Loop 
while not done: 
     # -- User input and controls
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        #End If
    #Next event
    # -- Game logic goes after this comment
    sun_x = sun_x + 5
    #quadratic
    sun_y = (100/320**2)*(sun_x-320)**2
    if sun_x > size[0] + 40:
        # -- time lag
        pygame.time.delay(1000)
        sun_x = -40
    #endif
    # -- Screen background is BLACK 
    screen.fill (LIGHTBLUE) 
    if sun_x == size[0] + 40:
        screen.fill(DARKBLUE)
    #endif
    # -- Draw here 
    # -- Draw house
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    # -- Draw windows
    pygame.draw.rect(screen, YELLOW, (255,185,40,40))
    pygame.draw.rect(screen, YELLOW, (345,185,40,40))
    pygame.draw.rect(screen, YELLOW, (255,250,40,40))
    pygame.draw.rect(screen, YELLOW, (345,250,40,40))
    # -- Draw door
    pygame.draw.rect(screen, YELLOW, (310,255,20,60))
    # -- Draw roof
    pygame.draw.polygon(screen, BLUE, ((220,165), (420,165), (320,145)))
    # -- Draw sun
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y),40,0)
    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()