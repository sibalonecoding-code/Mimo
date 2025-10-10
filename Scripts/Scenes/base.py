

# chargement des modules
# ...


# classe de base quand on crée une scène
class SceneBase:

    def __init__(self, scene_manager):
        self.scene_manager = scene_manager

    def update_logic(self, events, delta_time):
        pass

    def update_graphics(self):
        pass
