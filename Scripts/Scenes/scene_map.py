

# import modules
import Scripts.objects as objects
import Scripts.game_map as game_map
import Scripts.player as player



def updateInputs(dt):
    player.update(dt)


def updateGraphics():
    # draw map on display
    game_map.draw("Forest 001")
    player.draw()


