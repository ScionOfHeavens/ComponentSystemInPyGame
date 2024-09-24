from Component import Component
from Componentable import Componentable
import pygame

class Game:
    __is_running: bool = False
    __components: list[Component] = []
    
    def __init__(self, scene: Componentable) -> None:
        pygame.init()
        self.__components.extend(scene.get_components())

    def enable(self):
        for component in self.__components:
            component.on_enable()

    def start_loop(self) -> None:
        self.__is_running = True
        for component in self.__components:
            component.start()

        while self.__is_running:
            self.__loop__()

    def __loop__(self):
        for component in self.__components:
            component.update()

    def get_component(self, component_type: type) -> Component:
        for component in self.__components:
            if isinstance(component, component_type):
                return component_type
            
    def add_game_object(self, game_object: Componentable) -> None:
        self.__components.extend(game_object.get_components())