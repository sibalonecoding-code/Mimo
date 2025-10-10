

# chargement des modules
# - modules standards
# - modules téléchargés
# - modules crées
import time
import pygame
from Scripts.config import *
from Scripts.scene_manager import *


# initialisation de pygame si c'est pas fait
if not pygame.get_init():
    pygame.init()


# classe principale du jeu, contient les objets de base comme la
# fenêtre d'affichage, la surface de dessin etc
class Game:

    # initialisation
    def __init__(self):

        # charge la configuration
        Config.load()

        # initialise tout le camboui
        self.running = True
        self.window = pygame.display.set_mode(Config.resolutions[Config.Graphics.Window.size])
        self.display = pygame.Surface(Config.resolutions[Config.Graphics.Display.size])
        self.clock = pygame.time.Clock()
        self.scene_manager = SceneManager(self, "test")

        # modifie le nom de la fenêtre
        pygame.display.set_caption(f"{Config.Game.title} - v{Config.Game.version}")

        # démarre la boucle principale
        self.main_loop()

    # boucle principale
    def main_loop(self):
        previous_tick = time.time()
        current_tick = previous_tick
        while self.running:
            # calcul du temps écoulé entre deux itération de la boucle
            current_tick = time.time()
            elapsed_time = current_tick - previous_tick
            previous_tick = current_tick
            # calcul du delta time
            delta_time = elapsed_time * Config.General.fps
            # mises à jour des entrées et données
            self.display.fill([0, 0, 0])
            self.scene_manager.update(pygame.event.get(), delta_time)
            if self.scene_manager.should_quit:
                self.running = False
                break
            self.clock.tick(Config.General.fps)
            # mises à jour graphiques
            self.window.blit(pygame.transform.scale(self.display, Config.resolutions[Config.Graphics.Window.size]))
            pygame.display.update()


# point d'entrée 
if __name__ == "__main__":
    mimo = Game()
