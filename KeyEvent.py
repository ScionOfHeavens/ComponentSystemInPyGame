import pygame
from Event import Event
from Action import Action
from typing import Any, Callable

class TypeErrorException(Exception):
    pass

class keyEvent:
    __event: Event
    __key: int
    def __init__(self, key: str) -> None:
        if not isinstance(key, str):
            raise TypeErrorException
        self.__key = pygame.key.key_code(key)
        self.__event = Event()

    def subscribe_on_event(self, action: Action[[None],None]):
        if not isinstance(action, Callable):
            raise TypeErrorException("action has a", action.__class__.__name__, "type instead of action or function")
        self.__event.add_listener(action)
        
    def unsubscribe_on_event(self, action: Action[[None],None]):
        if not isinstance(action, Callable):
            raise TypeErrorException("action has a", action.__class__.__name__, "type instead of action or function")
        self.__event.remove_listener(action)

    @property
    def Key(self):
        return self.__key

    def act_on_event(self, py_key_events: list[pygame.event.Event]) -> None:
        self.__event()

    def __eq__(self, value: object) -> bool:
        if isinstance(value, str):
            return self.Key == value
        if isinstance(value, keyEvent):
            return self.Key == value.Key
        raise Exception
    
    def __hash__(self) -> int:
        return self.__key
        

class KeyPressed(keyEvent):
    def __init__(self, key: str) -> None:
        super().__init__(key)

    def act_on_event(self, py_key_events: list[pygame.event.Event]) -> None:
        pressed_keys: enumerate[bool] = pygame.key.get_pressed()
        if pressed_keys[self.Key] == True:
            super().act_on_event(py_key_events)
        

class KeyDown(keyEvent):
    def __init__(self, key: str) -> None:
        super().__init__(key)

    def act_on_event(self, py_key_events: list[pygame.event.Event]) -> None:
        for event in py_key_events:
            if event.key == self.Key and event.type == pygame.KEYDOWN:
                super().act_on_event(py_key_events)
                
                 
class KeyUp(keyEvent):
    def __init__(self, key: str) -> None:
        super().__init__(key)

    def act_on_event(self, py_key_events: list[pygame.event.Event]) -> None:
        for event in py_key_events:
            if event.key == self.Key and event.type == pygame.UP:
                super().act_on_event(py_key_events)