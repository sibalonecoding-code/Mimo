

# chargement des modules
import pygame
from Scripts.Scenes.base import *


# initialisation de pygame si c'est pas fait
if not pygame.get_init():
    pygame.init()


# classe de la scène de test
class SceneTest2(SceneBase):

    def __init__(self, scene_manager):
        super().__init__(scene_manager)

    def update_logic(self, events, delta_time):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    self.scene_manager.next("test")

    def update_graphics(self):
        display = self.scene_manager.game.display
        display.fill([0, 255, 0])
