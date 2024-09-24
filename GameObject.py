from Component import Component
from BaseComponents.Sprite import Sprite
from BuildGameBase import RENDER_GROUP, GAME
from Componentable import Componentable

class GameObject(Componentable):
    def __init__(self) -> None:
        super().__init__()

    def with_sprite(self, image_path: str) -> None:
        sprite: Sprite = Sprite(image_path)
        RENDER_GROUP.add_sprite(sprite)
        self.add_component(sprite)

    def ready(self) -> None:
        GAME.add_game_object(self)