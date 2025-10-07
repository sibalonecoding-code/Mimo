

# import modules

import pygame


# initialize pygame
if not pygame.get_init():
    pygame.init()


joysticks = dict()
clicked_key = dict()


def update(event):

    # set all clicked key to False
    for key in clicked_key:
        clicked_key[key] = False

    # keyboard part

    if event.type == pygame.KEYDOWN:
        pass

    elif event.type == pygame.KEYUP:
        clicked_key[event.key] = True
        # print(clicked_key)

    # joysticks part
    
    elif event.type == pygame.JOYDEVICEADDED:
        joy = pygame.joystick.Joystick(event.device_index)
        joysticks[joy.get_instance_id()] = joy
        # print(f"Manette ajoutée: {joy.get_instance_id()}")
    
    elif event.type == pygame.JOYDEVICEREMOVED:
        if event.instance_id in joysticks:
            joysticks.pop(event.instance_id)
            # print(f"Manette supprimée: {event.instance_id}")
