

# import modules
import Scripts.objects as objects
import Scripts.game_map as game_map



def updateInputs(dt):
    objects.camera["x"] += 0.1 * dt


def updateGraphics():
    # draw map on display
    game_map.draw_map("Forest 001")


