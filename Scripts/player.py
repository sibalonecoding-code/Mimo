

# import modules

import time
import pygame
import Scripts.objects as objects


if not pygame.get_init():
    pygame.init()


position = {
    "x": 0,
    "y": 0
}
player_speed = 2.0
player_position_locked = False

player_directions = {
    "bas": 0,
    "bas-gauche": 1,
    "gauche": 2,
    "haut-gauche": 3,
    "haut": 4,
    "haut-droite": 5,
    "droite": 6,
    "bas-droite": 7
}
player_direction = player_directions["bas"]
player_direction_locked = False

player_frame_locked = False
player_frame = 0
player_image = pygame.image.load("Assets/Images/player_temp.png")
frame_duration = 0.25
previous_tick = time.time()


def update(dt):
    global player_frame
    global previous_tick
    global position
    global player_direction

    pressed_keys = pygame.key.get_pressed()

    # update player position
    if not player_position_locked:
        if pressed_keys[pygame.K_LEFT]:
            position["x"] -= player_speed * dt
        if pressed_keys[pygame.K_RIGHT]:
            position["x"] += player_speed * dt
        if pressed_keys[pygame.K_UP]:
            position["y"] -= player_speed * dt
        if pressed_keys[pygame.K_DOWN]:
            position["y"] += player_speed * dt
    
    # update frame id
    if not player_frame_locked:
        current_tick = time.time()
        next_frame = current_tick - previous_tick >= frame_duration
        if next_frame:
            previous_tick = current_tick
            player_frame += 1
            if player_frame >= 4:
                player_frame = 0

    # update player direction
    if not player_direction_locked:
        if pressed_keys[pygame.K_DOWN]:
            if pressed_keys[pygame.K_LEFT]:
                player_direction = 1
            elif pressed_keys[pygame.K_RIGHT]:
                player_direction = 7
            else:
                player_direction = 0
        elif pressed_keys[pygame.K_UP]:
            if pressed_keys[pygame.K_LEFT]:
                player_direction = 3
            elif pressed_keys[pygame.K_RIGHT]:
                player_direction = 5
            else:
                player_direction = 4
        else:
            if pressed_keys[pygame.K_LEFT]:
                player_direction = 2
            elif pressed_keys[pygame.K_RIGHT]:
                player_direction = 6

    
def draw():
    sy = 16 * player_direction
    sx = 16 * player_frame
    objects.display.blit(
        player_image,
        [position["x"], position["y"]],
        [sx, sy, 16, 16]
    )

