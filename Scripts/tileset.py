

# import modules

import json
import pygame
import Scripts.objects as objects


# check if tilesets are initialized
_initialized = False
def get_init():
    return _initialized

    
# initialize tilesets
def init():

    # get tilesets data from json file
    tilesets_data = None
    with open("Data/tilesets.json", "r") as file:
        tilesets_data = json.load(file)
        print(tilesets_data)

    # foreach tileset data make a tileset
    for tileset_data in tilesets_data:
        tileset = tileset_data.copy()
        tileset["image"] = pygame.image.load(f"Assets/Images/{tileset_data['name']}.png")
        objects.tilesets[tileset["name"]] = tileset

    # set tilesets as initialized
    _initialized = True
