import pygame
import random
import math 
import PIL
# -- Global Constants 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0)
RED = (255,0,0)
# -- Initialise PyGame
pygame.init() 
# -- Blank Screen 
size = (640,480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("Invaders") 

## -- Define the class snow which is a sprite 
class Invader(pygame.sprite.Sprite): 
    # Define the constructor for snow 
    def __init__(self, color, width, height, speed):
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour
        # Import image
        image = pygame.image.load('comp sci space invader.png')
        image = pygame.transform.scale(image, (50, 50))
        self.image = image
        #self.image = pygame.Surface([width,height]) 
        #self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = random.randrange(0, 600) 
        self.rect.y = random.randrange(-100, 0)
        # Set speed of the sprite 
        self.speed = speed  
    # Class update function - runs for each pass through the game loop 
    def update(self): 
        if self.rect.y <= 480:
            self.rect.y = self.rect.y + self.speed
        else:
            self.rect.y = 0
        #endif
 #End Procedure
#End Class

## -- Define the class player which is a sprite 
class Player(pygame.sprite.Sprite): 
    # Define the constructor for player 
    def __init__(self, color, width, height):
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = 300 
        self.rect.y = size[1] - height
        # Set speed of the sprite 
        self.speed = 0
        #add new attribute to Player class - lives
        self.lives = 5
        #add new attribute to Player class - bullet_count
        self.bullet_count = 50
        #add new attribute to Player class - score
        self.score = 0
    # Class update function - runs for each pass through the game loop 
    def update(self): 
        self.rect.x = self.rect.x + self.speed
    #End Procedure


#End Class

## -- Define the class snow which is a sprite 
class Bullet(pygame.sprite.Sprite): 
    # Define the constructor for snow 
    def __init__(self, color, x_co, y_co):
        # Call the sprite constructor 
        super().__init__() 
        #Set size of sprite
        self.width = 2
        self.height = 2
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([self.width,self.height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = x_co 
        self.rect.y = y_co
        # Set speed of the sprite 
        self.speed = -2
    # Class update function - runs for each pass through the game loop 
    def update(self): 
        self.rect.y = self.rect.y + self.speed
    #End Procedure


#End Class

def player_set_speed(val):
    if val > 0:
        if player.rect.x < 630:
            player.speed = val
    elif val < 0:
        if player.rect.x > 0:
            player.speed = val
    else: 
        player.speed = val
#end procedure

# -- Exit game flag set to false 
done = False

#create font 
font = pygame.font.SysFont(None, 25)

# Create a list of the invaders
invader_group = pygame.sprite.Group()
# Create a list of bullets
bullet_group = pygame.sprite.Group()  
# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group()

# Create the invaders 
number_of_invaders = 20 # we are creating 50 snowflakes
for x in range (number_of_invaders): 
    my_invader = Invader(BLUE, 10, 10, 1) # snowflakes are white with size 5 by 5 px
    invader_group.add (my_invader) # adds the new snowflake to the group of snowflakes
    all_sprites_group.add (my_invader) # adds it to the group of all Sprites
#Next x

#create object: player
player = Player(YELLOW, 10, 10)
all_sprites_group.add(player)


# -- Manages how fast screen refreshes 
clock = pygame.time.Clock() 

### -- Game Loop 
while not done: 
     # -- User input and controls
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        elif event.type == pygame.KEYDOWN: # - a key is down 
            if event.key == pygame.K_LEFT: # - if the left key pressed
                player_set_speed(-3) # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                player_set_speed(3) # speed set to 3
            elif event.key == pygame.K_UP:
                player.bullet_count = player.bullet_count - 1
                my_bullet = Bullet(RED, player.rect.x + 4, 470) # snowflakes are white with size 5 by 5 px
                bullet_group.add (my_bullet) # adds the new snowflake to the group of snowflakes
                all_sprites_group.add (my_bullet) # adds it to the group of all Sprites
        elif event.type == pygame.KEYUP: # - a key released 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                player_set_speed (0) # speed set to 0
    #Next event
    # -- Game logic goes after this comment
    # -- when invader hits the player, player loses one life. 
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    for foo in player_hit_group: 
        player.lives = player.lives - 1
    # -- when bullet hits the invader, invader is deleted. 
    bullet_hit_group = pygame.sprite.groupcollide(invader_group, bullet_group, True, True)
    for count in bullet_hit_group:
        player.score += 5

    all_sprites_group.update()  
    if player.rect.x <= 0:
        player.speed = 0
    elif player.rect.x >= 630:
        player.speed = 0
    # - Screen background is BLACK 
    screen.fill (BLACK) 
    # -- Draw here 
    all_sprites_group.draw (screen)
        #show lives
    text = font.render(("Lives = " + str(player.lives)), True, WHITE)
    screen.blit(text, ( 100, 20 ) )
        #show score
    text = font.render(("Score = " + str(player.score)), True, WHITE)
    screen.blit(text, ( 100, 60 ) )
        #show bullet count
    text = font.render(("Bullets = " + str(player.bullet_count)), True, WHITE)
    screen.blit(text, ( 100, 100 ) )
    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()