import sys

import pygame

from settings import Settings

from ship import Ship
import game_functions as gf

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
        gf.check_events()
        # При каждом проходе цикла перерисовывается экран
        gf.update_screen(ai_settings, screen, ship)


run_game()