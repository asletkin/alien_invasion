class Settings():
    '''Класс для хранения всех настроек игры Flien Invasion'''

    def __init__(self):
        '''Инициализация настройки игры'''
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Настройки коробля
        self.ship_speed_factor = 1.5
