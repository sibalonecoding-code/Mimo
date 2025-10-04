

# import modules
import sys
import Scripts.objects as objects
import Scripts.Scenes.scene_title as scene_title
import Scripts.Scenes.scene_map as scene_map


# add a new scene
def sceneAppend(scene_name):
    objects.scenes.append(scene_name)

# remove last scene
def scenePop():
    objects.scenes.pop()

# update player inputs
def updateInputs(dt):
    if not objects.scenes:
        print("/!\\ La liste des scènes est vide")
        sys.exit()
    current_scene = objects.scenes[-1]
    if current_scene == "scene_title":
        scene_title.updateInputs(dt)
    elif current_scene == "scene_map":
        scene_map.updateInputs(dt)

# update graphics
def updateGraphics():
    if not objects.scenes:
        print("/!\\ La liste des scènes est vide")
        sys.exit()
    current_scene = objects.scenes[-1]
    if current_scene == "scene_title":
        scene_title.updateGraphics()
    elif current_scene == "scene_map":
        scene_map.updateGraphics()
