

# import modules

import json
import pygame
import inputs


# initialize pygame
if not pygame.get_init():
    pygame.init()


# load configuration
config = None
with open("config.json", "r") as file:
    config = json.load(file)

    
# create window and display
SIZES = config["game"]["sizes"]
WINDOW_SIZE_ID = config["window"]["size"]
WINDOW_SIZE = SIZES[WINDOW_SIZE_ID]
DISPLAY_SIZE = config["display"]["size"]
GAME_TITLE = config["game"]["title"]
GAME_VERSION = config["game"]["version"]

WINDOW = pygame.display.set_mode(WINDOW_SIZE)
DISPLAY = pygame.Surface(DISPLAY_SIZE)
pygame.display.set_caption(f"{GAME_TITLE} v{GAME_VERSION}")



# main loop

running = True
while running:

    # handle pygame events
    for event in pygame.event.get():

        # handle quit event (when closing the window or alt+F4)
        if event.type == pygame.QUIT:
            running = False
            
        inputs.update(event)
    
    
