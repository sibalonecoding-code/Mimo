

# import modules

import pygame


# draw map function

def draw_map(display, camera, tileset, map_data):

    tiles = map_data["tiles"] # données des tuiles dans la map
    tile_size = tileset["tile"]["size"] # taille d'une tuile dans le tileset
    map_width = map_data["width"] # largeur de la map en tuiles (pas pixels)
    map_height = map_data["height"] # hauteur de la map en tuiles (pas pixels)

    for row in range(len(map_height)):
        for in col in range(len(map_width)):
            
            tile_id = tiles[row][col] # id de la tuile à afficher
            tile_x = col * tile_size - camera["x"] # coordonnées x par rapport au display
            tile_y = row * tile_size - camera["y"] # coordonnées y par rapport au display

            source_x = (tile_id % tileset["width"]) * tile_size # coordonnées x par rapport au tileset
            source_y = (tile_id // tileset["width"]) * tile_size # coordonnées y par rapport au tileset

            # colle la partie de l'image (1) ciblée en (3) aux coordonnées (2)
            display.blit(
                tileset["image"], # (1)
                [tile_x, tile_y], # (2)
                [source_x, source_y, tile_size, tile_size] # (3)
            )
