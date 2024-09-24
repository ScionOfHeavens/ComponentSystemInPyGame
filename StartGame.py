from BuildGameBase import GAME, KEY_INPUT, TIME
from GameObject import GameObject
from Component import Component
from BaseComponents.Sprite import Sprite


class TryToMove(Component):
    __position: list[int, int] = None
    __sprite: Sprite = None
    __speed: float = None
    def __init__(self, position: list[int, int], speed: float) -> None:
        super().__init__()
        self.__position = position
        self.__speed = speed

    def start(self) -> None:
        self.__sprite: Sprite = self.get_component(Sprite)
        def up() -> None:
            self.__position[1]-=self.__speed*TIME.delta_time
            self.__sprite.set_position(self.__position)
        def down() -> None:
            self.__position[1]+=self.__speed*TIME.delta_time
            self.__sprite.set_position(self.__position)
        def left() -> None:
            self.__position[0]-=self.__speed*TIME.delta_time
            self.__sprite.set_position(self.__position)
        def right() -> None:
            self.__position[0]+=self.__speed*TIME.delta_time
            self.__sprite.set_position(self.__position)

        KEY_INPUT.subscribe_on_pressed_key("w", up)
        KEY_INPUT.subscribe_on_pressed_key("s", down)
        KEY_INPUT.subscribe_on_pressed_key("a", left)
        KEY_INPUT.subscribe_on_pressed_key("d", right)

slime = GameObject()
slime.with_sprite(r"C:\Users\webda\OneDrive\Desktop\pyGame\resources\sprites\slime.png")
component = TryToMove([0,0], 300)
slime.add_component(component)

reversed_slime = GameObject()
reversed_slime.with_sprite(r"C:\Users\webda\OneDrive\Desktop\pyGame\resources\sprites\slime.png")
component = TryToMove([300,0], -300)
reversed_slime.add_component(component)

GAME.add_game_object(slime)
GAME.add_game_object(reversed_slime)
GAME.start_loop()