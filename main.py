

# import modules

import json
import pygame
import Scripts.inputs as inputs
import Scripts.tileset as tileset
import Scripts.map_ as map_
import Scripts.objects as objects


# initialize pygame
if not pygame.get_init():
    pygame.init()

# initialize tilesets
if not tileset.get_init():
    tileset.init()

# initialize maps
if not map_.get_init():
    map_.init()


camera = {
    "x": 0,
    "y": 0
}

# main loop
running = True
while running:

    # handle pygame events
    for event in pygame.event.get():

        # handle keyboard, joysticks etc first
        inputs.update(event)
        
        # handle quit event (when closing the window or alt+F4)
        if event.type == pygame.QUIT:
            running = False

    # clear display in black
    objects.display.fill([0, 0, 0])

    # draw map on display
    map_.draw_map(camera, "Forest 001")

    # draw display on window
    objects.window.blit(pygame.transform.scale(objects.display, objects.WINDOW_SIZE))

    # update pygame graphics
    pygame.display.update()
