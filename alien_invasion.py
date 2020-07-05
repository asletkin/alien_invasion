import sys

import pygame

from settings import Settings

from ship import Ship

def run_game():
    # Инициализируем игру и создаем объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # Назначение цвета фона
    # bg_color = (230, 230, 230)
    # Создание карабля
    ship = Ship(screen)
    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # При каждом проходе цикла перерисовывается экран
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # Отображение последнего прорисованного экрана
        pygame.display.flip()

run_game()