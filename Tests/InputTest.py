from Component import Component
from BaseComponents.Input import KeyInputHanle, Keys

class InputTest(Component):
    __input: KeyInputHanle
    def __init__(self, input: KeyInputHanle) -> None:
        self.__input = input

    def start(self):
        self.__input.subscribe_on_pressed_key(Keys.q,lambda: print("q pressed"))
        self.__input.subscribe_on_pressed_key(Keys.w,lambda: print("w pressed"))
        self.__input.subscribe_on_pressed_key(Keys.e,lambda: print("e pressed"))
        self.__input.subscribe_on_pressed_key(Keys.s,lambda: print("s pressed"))
        self.__input.subscribe_on_down_key(Keys.space,lambda: print("space pressed"))
