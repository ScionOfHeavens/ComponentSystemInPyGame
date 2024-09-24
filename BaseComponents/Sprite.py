from Component import Component
import pygame


class Sprite(Component):
    class __PyGameSprite(pygame.sprite.DirtySprite):
        image: pygame.Surface = None
        rect: pygame.rect.Rect = None
        def __init__(self, image: pygame.Surface) -> None:
            super().__init__()
            self.image = image
            self.rect = image.get_rect()
        
            
    __sprite: __PyGameSprite = None
    def __init__(self, image_path: str) -> None:
        self.__sprite = self.__PyGameSprite(pygame.image.load(image_path))
        self.__rect = self.__sprite.rect

    def start(self) -> None:
        pass

    def update(self) -> None:
        self.__sprite.dirty = 1
        self.__sprite.rect = self.__rect

    def get_sprite(self) -> pygame.Surface:
        return self.__sprite
    
    def set_position(self, position: tuple[int:int]):
        self.__rect.topleft = position
