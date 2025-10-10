

# chargement des modules
import json


# classe du gestionnaire de scènes qui permet de passer d'une scène à une autre
class Config:

    resolutions = [
        [320, 240],
        [640, 480],
        [960, 720],
        [1280, 960]
    ]

    class Game:

        title = ""
        version = 0.0

    class General:

        fps = 0

    class Graphics:

        class Window:

            size = 0

        class Display:

            size = 0

    class Audio:

        general = 0
        music = 0
        sfx = 0
        mute = False
        

    # Charge la configuration depuis le fichier Data/config.json
    @classmethod
    def load(cls):
        with open("Data/config.json", "r") as file:
            data = json.load(file)
            cls.Game.title = data["game"]["title"]
            cls.Game.version = data["game"]["version"]
            cls.General.fps = data["general"]["fps"]
            cls.Graphics.Window.size = data["graphics"]["window"]["size"]
            cls.Graphics.Display.size = data["graphics"]["display"]["size"]
            cls.Audio.general = data["audio"]["general"]
            cls.Audio.music = data["audio"]["music"]
            cls.Audio.sfx = data["audio"]["sfx"]
            cls.Audio.mute = data["audio"]["mute"]

    # Sauvegarde la configuration vers le fichier Data/config.json
    @classmethod
    def save(cls):
        pass
        
        

