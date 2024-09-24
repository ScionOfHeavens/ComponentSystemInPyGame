import pygame
from Component import Component

class Time(Component):
    __clock: pygame.time.Clock = None
    __delta_time: int = 0

    def on_enable(self) -> None:
        self.__clock = pygame.time.Clock()
    
    def update(self) -> None:
        self.__delta_time = self.__clock.tick(60) / 1000

    @property
    def delta_time(self):
        return self.__delta_time