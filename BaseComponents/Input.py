from KeyEvent import keyEvent, KeyPressed, KeyDown, KeyUp
from Action import Action
from Component import Component
import pygame

class KeyInputHanle(Component):
    __keys_pressed: dict[str, KeyPressed] = {}
    __keys_down: dict[str, KeyDown] = {}
    __keys_up: dict[str, KeyUp] = {}
    
    def subscribe_on_pressed_key(self, key: str, action: Action[[None], None]) -> None:
        event = self.__keys_pressed.setdefault(key, KeyPressed(key))
        event.subscribe_on_event(action)

    def unsubscribe_on_pressed_key(self, key: str, action: Action[[None], None]) -> None:
        event = self.__keys_pressed[key]
        event.unsubscribe_on_event(action)

    def subscribe_on_down_key(self, key: str, action: Action[[None], None]) -> None:
        event = self.__keys_down.setdefault(key, KeyDown(key))
        event.subscribe_on_event(action)

    def unsubscribe_on_down_key(self, key: str, action: Action[[None], None]) -> None:
        event = self.__keys_down[key]
        event.unsubscribe_on_event(action)

    def subscribe_on_up_key(self, key: str, action: Action[[None], None]) -> None:
        event = self.__keys_up.setdefault(key, KeyUp(key))
        event.subscribe_on_event(action)

    def unsubscribe_on_up_key(self, key: str, action: Action[[None], None]) -> None:
        event = self.__keys_up[key]
        event.unsubscribe_on_event(action)

    def update(self):
        events: list[keyEvent] = list(self.__keys_pressed.values()) + list(self.__keys_down.values()) + list(self.__keys_up.values())
        py_key_events = pygame.event.get([pygame.KEYUP, pygame.KEYDOWN])
        pygame.event.get()
        for event in events:
            event.act_on_event(py_key_events)


class Keys:
    q: str = "q"
    w: str = "w"
    e: str = "e"
    s: str = "s"
    space: str = "space"
