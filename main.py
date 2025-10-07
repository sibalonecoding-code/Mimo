

# import modules

import time
import json
import pygame
import Scripts.inputs as inputs
import Scripts.tileset as tileset
import Scripts.game_map as game_map
import Scripts.scene as scene
import Scripts.objects as objects

# initialize pygame
if not pygame.get_init():
    pygame.init()

# initialize tilesets
if not tileset.getInit():
    tileset.init()

# initialize maps
if not game_map.getInit():
    game_map.init()

# initialize first scene
scene.sceneAppend("scene_map")


# main loop
running = True
current_tick = time.time()
previous_tick = time.time()

while running:

    # handle pygame events
    for event in pygame.event.get():

        # handle keyboard, joysticks etc first
        inputs.update(event)
        
        # handle quit event (when closing the window or alt+F4)
        if event.type == pygame.QUIT:
            running = False

    current_tick = time.time()
    elapsed_time = float(current_tick - previous_tick) * 30
    previous_tick = current_tick

    # handle player inputs
    scene.updateInputs(elapsed_time)

    # clear display in black
    objects.display.fill([0, 0, 0])

    # update scene graphics
    scene.updateGraphics()

    # draw display on window
    objects.window.blit(pygame.transform.scale(objects.display, objects.WINDOW_SIZE))

    # update pygame graphics
    pygame.display.update()

    # limit fps
    objects.clock.tick(objects.FPS)
    
