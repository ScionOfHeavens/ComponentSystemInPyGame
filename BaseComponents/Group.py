from typing import Any
from Component import Component
from BaseComponents.Sprite import Sprite
from BaseComponents.Screen import Screen
import pygame

class Group(Component):
    __py_group: pygame.sprite.LayeredDirty = None
    __screen: pygame.Surface = None
    def on_enable(self) -> None:
        self.__py_group = pygame.sprite.LayeredDirty()
    
    def start(self) -> None:
        screen: Screen = self.get_component(Screen)
        self.__screen = screen.get_surface()

    def add_sprite(self, sprite: Sprite):
        self.__py_group.add(sprite.get_sprite())

    def draw_sprites_on(self, surface: pygame.Surface):
        self.__py_group.draw(surface)

    def update(self) -> None:
        self.__py_group.draw(self.__screen)