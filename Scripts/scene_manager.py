

# chargement des modules
import sys
import pygame
from Scripts.utils import *
from Scripts.Scenes.base import *
from Scripts.Scenes.test import *
from Scripts.Scenes.test2 import *


# initialisation de pygame si c'est pas fait
if not pygame.get_init():
    pygame.init()


# classe du gestionnaire de scènes qui permet de passer d'une scène à une autre
class SceneManager:

    # liste des scènes proposées par le gestionnaire de scènes
    SCENES = {
        "test": SceneTest,
        "test2": SceneTest2
    }

    def __init__(self, game, first_scene, *args, **kwargs):
        self.game = game
        self.scenes = overlist()
        self.scenes.append(SceneManager.SCENES[first_scene])
        self.scene = self.scenes.last(self, *args, **kwargs)
        self.should_quit = False

    # ajoute une scène à la liste de scène, si next_scene se trouve déjà dans
    # la liste des scènes retire la dernière scène jusqu'à ce que next_scene
    # vaut la dernière scène dans la liste des scènes
    def next(self, next_scene, *args, **kwargs):
        if next_scene not in SceneManager.SCENES:
            print("[ERROR]: This scene doesn't exists")
            sys.exit()
        if SceneManager.SCENES[next_scene] is self.scenes[-1]:
            self.change_scene(*args, **kwargs)
        elif SceneManager.SCENES[next_scene] in self.scenes:
            self.scenes.pop()
            self.next(next_scene, *args, **kwargs)
        else:
            self.scenes.append(SceneManager.SCENES[next_scene])
        self.change_scene(*args, **kwargs)

    # retire la dernière scène de la liste des scènes
    def previous(self):
        self.scenes.pop()
        self.change_scene()

    # instancie la dernière scène de la liste des scènes
    def change_scene(self, *args, **kwargs):
        self.scene = self.scenes[-1](self, *args, **kwargs)

    # met à jour la logique et les graphismes de la dernière scène de la
    # liste des scènes
    def update(self, events, delta_time):
        for event in events:
            if event.type == pygame.QUIT:
                self.should_quit = True
                return
        self.scene.update_logic(events, delta_time)
        self.scene.update_graphics()

