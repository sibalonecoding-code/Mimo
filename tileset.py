

# import modules

import json
import pygame


# liste des tilesets

tilesets = list()


# initialize tilesets

def init():

    # get tilesets data from json file
    tilesets_data = None
    with open("tilesets.json", "r") as file:
        tilesets_data.load(file)

    # foreach tileset data make a tileset
    for tileset_data in tilesets_data:
        tileset = tileset_data.copy()
        tileset["image"] = pygame.image.load(f"Assets/Images/{tileset_data['name']}.png")
        tilesets.append(tileset)
