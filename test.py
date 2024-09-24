import pygame
import sys
from pygame.sprite import DirtySprite, LayeredDirty
from BaseComponents.Sprite import Sprite
from BaseComponents.Group import Group

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Цвета
WHITE = (255, 255, 255)

# Скорость движения
speed = 5
position = [0,0]

# Метод для обновления спрайта
def update(keys):
    if keys[pygame.K_LEFT]:
        position[0] -= speed
    if keys[pygame.K_RIGHT]:
        position[0] += speed
    if keys[pygame.K_UP]:
        position[1] -= speed
    if keys[pygame.K_DOWN]:
        position[1] += speed

# Создание группы LayeredDirty
all_sprites = Group(screen)

# Создание экземпляра спрайта и добавление его в группу
sprite = Sprite(r"C:\Users\webda\OneDrive\Desktop\pyGame\resources\sprites\slime.png")
all_sprites.add_sprite(sprite)

# Главный игровой цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Получение списка нажатых клавиш
    keys = pygame.key.get_pressed()

    update(keys)
    sprite.set_position(position)
    sprite.update()


    # Очистка экрана
    screen.fill(WHITE)

    # Отрисовка всех спрайтов (только грязных)
    all_sprites.draw_sprites_on(screen)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)
