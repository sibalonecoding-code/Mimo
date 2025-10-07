

# import modules

import json
import pygame
import Scripts.objects as objects


# check if maps are initialized
_initialized = False
def getInit():
    return _initialized


# initialize list of maps
def init():

    # get maps data from json file
    maps_data = None
    with open("Data/maps.json", "r") as file:
        maps_data = json.load(file)

    # foreach map data make a map
    for map_data in maps_data:
        map_ = map_data.copy()
        objects.maps[map_["name"]] = map_

    # set maps as initialized
    _initialized = True


# draw map function

def draw(map_name):

    display = objects.display
    tilesets = objects.tilesets
    maps = objects.maps

    map_data = maps[map_name]

    tiles = map_data["tiles"] # données des tuiles dans la map
    map_layers = map_data["layers"] # nombre de couches de la map
    map_width = map_data["width"] # largeur de la map en tuiles (pas pixels)
    map_height = map_data["height"] # hauteur de la map en tuiles (pas pixels)
    map_tilesets = map_data["tilesets"] # récupère la liste des tilesets utilisées par la map

    for layer in range(map_layers):
        tileset = tilesets[map_tilesets[layer]]
        tile_size = tileset["tile"]["size"] # taille d'une tuile dans le tileset
        for row in range(map_height):
            for col in range(map_width):
                
                tile_id = tiles[layer][row][col] # id de la tuile à afficher
                tile_x = col * tile_size - objects.camera["x"] # coordonnées x par rapport au display
                tile_y = row * tile_size - objects.camera["y"] # coordonnées y par rapport au display

                source_x = (tile_id % tileset["width"]) * tile_size # coordonnées x par rapport au tileset
                source_y = (tile_id // tileset["width"]) * tile_size # coordonnées y par rapport au tileset

                # colle la partie de l'image (1) ciblée en (3) aux coordonnées (2)
                display.blit(
                    tileset["image"], # (1)
                    [tile_x, tile_y], # (2)
                    [source_x, source_y, tile_size, tile_size] # (3)
                )
