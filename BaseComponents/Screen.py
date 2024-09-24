from Component import Component
import pygame


class Screen(Component):
    __screen_surface: pygame.Surface = None
    
    def on_enable(self) -> None:
        self.__screen_surface = pygame.display.set_mode((640, 480))

    def get_surface(self) -> pygame.Surface:
        return self.__screen_surface

    def update(self) -> None:
        pygame.display.flip()
        self.__screen_surface.fill("purple")


if __name__ == "__main__":
    pygame.init()
    screen: Screen = Screen()
    while True:
        screen.update()