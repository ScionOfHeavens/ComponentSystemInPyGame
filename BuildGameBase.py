from Game import Game
from BaseComponents.Input import KeyInputHanle
from BaseComponents.Group import Group
from BaseComponents.Screen import Screen
from BaseComponents.Time import Time
from Scene import Scene


KEY_INPUT = KeyInputHanle()
SCREEN = Screen()
RENDER_GROUP = Group()
TIME = Time()

SCENE = Scene()

SCENE.add_component(KEY_INPUT)
SCENE.add_component(SCREEN)
SCENE.add_component(RENDER_GROUP)
SCENE.add_component(TIME)

GAME = Game(SCENE)
GAME.enable()