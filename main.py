# Basic Pygame Structure

import pygame                               # Imports pygame and other libraries# Define Classes (sprites) here
import random
pygame.init()                               # Pygame is initialised (starts running)
#Define Classes (sprites) here
class FallingObject(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite__init__(self)
        self.timecreated = pygame.time.get_tickets()
        self.image = pygame.Surface([30,30])
        self.image.set_colorkey(black)

        self.react = self.image.get_rect()
        self.react.x = random.randint(0,670)
        self.react.y = 0

    def setImage(self,graphicSelect):
        fallingObjectsImage = pygame.image.load(graphicSelect)
        self.image.blit(fallingObjectsImage,(0,0))


screen = pygame.display.set_mode([700,500]) # Set the width and height of the screen [width,height]
pygame.display.set_caption("Dodge")
background_image = pygame.image.load("OrchardBackground.jpg").convert()# Name your window
done = False                                # Loop until the user clicks the close button.
clock = pygame.time.Clock()                 # Used to manage how fast the screen updates
black    = (   0,   0,   0)                 # Define some colors using rgb values.  These can be
white    = ( 255, 255, 255)                 # used throughout the game instead of using rgb values.

# Define additional Functions and Procedures here
allFallingObjects = pygame.sprite.Group()

# -------- Main Program Loop -----------
while done == False:

    for event in pygame.event.get():        # Check for an event (mouse click, key press)
        if event.type == pygame.QUIT:       # If user clicked close window
            done = True                     # Flag that we are done so we exit this loop

    # Update sprites here
    nextObject = FallingObject()
    nextObject.setImage("Apple.png")

    allFallingObjects.add(nextObject)

    screen.blit(background_image, [0,0])
    allFallingObjects.draw(screen)
    pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
    clock.tick(20)                          # Limit to 20 frames per second

pygame.quit()                               # Close the window and quit.

