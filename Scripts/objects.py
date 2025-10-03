

# import modules
import json
import pygame


# initialize pygame
if not pygame.get_init():
    pygame.init()


# load configuration
config = None
with open("Data/config.json", "r") as file:
    config = json.load(file)

    
# global constants
SIZES = config["game"]["sizes"]
WINDOW_SIZE_ID = config["window"]["size"]
WINDOW_SIZE = SIZES[WINDOW_SIZE_ID]
DISPLAY_SIZE = config["display"]["size"]
GAME_TITLE = config["game"]["title"]
GAME_VERSION = config["game"]["version"]


# create global objects
window = pygame.display.set_mode(WINDOW_SIZE)
display = pygame.Surface(DISPLAY_SIZE)
tilesets = dict()
maps = dict()

# change window's title
pygame.display.set_caption(f"{GAME_TITLE} v{GAME_VERSION}")
