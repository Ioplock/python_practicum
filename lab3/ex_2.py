import pygame
import time

pygame.init()

# Глобальные переменные (настройки)
window_width = 800
window_height = 600
fon = './assets/background.png'  # изображение должно быть в том же каталоге, что и код на питоне
hero_image = './assets/player.png'  # путь к изображению героя

class Player(pygame.sprite.Sprite):
    def __init__(self, filename, hero_x=100, hero_y=None, x_speed=0, y_speed=0):
        super().__init__()  # Инициализация родительского класса Sprite
        self.image = pygame.image.load(filename)  # загрузка героя из файла
        self.rect = self.image.get_rect()

        self.hero_x = hero_x
        # Позиционируем героя на 5 пикселей выше нижней границы окна
        self.hero_y = window_height - self.rect.height - 5 if hero_y is None else hero_y

        # ставим персонажа в переданную точку (x, y):
        self.rect.x = self.hero_x
        self.rect.y = self.hero_y

        # создаем скорость движения спрайта:
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        '''перемещает персонажа,
        применяя текущую горизонтальную и вертикальную скорость'''
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        
        # Проверка вертикальных границ
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > window_height:
            self.rect.bottom = window_height

# Запуск
window = pygame.display.set_mode([window_width, window_height])  # создание окна указанных размеров
pygame.display.set_caption("Игра v1.1")  # установка надписи окна программы

# Создание спрайта игрока
player = Player(hero_image)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Загрузка фона
img1 = pygame.image.load(fon)
back_fon = pygame.transform.scale(img1, (window_width, window_height))
sdvig_fona = 0  # сдвиг фона

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_speed = -5
            elif event.key == pygame.K_RIGHT:
                player.x_speed = 5
            elif event.key == pygame.K_UP:
                player.y_speed = -5
            elif event.key == pygame.K_DOWN:
                player.y_speed = 5
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player.x_speed = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                player.y_speed = 0

    # Обновление позиции игрока
    player.update()

    # Проверка границ экрана и перемещение фона только при движении
    if player.x_speed != 0:  # Проверяем, движется ли игрок
        if player.rect.left <= 0:
            player.rect.left = 0
            sdvig_fona = (sdvig_fona + 5) % window_width
        elif player.rect.right >= window_width:
            player.rect.right = window_width
            sdvig_fona = (sdvig_fona - 5) % window_width

    # Отрисовка фона
    window.blit(back_fon, (sdvig_fona, 0))
    if sdvig_fona != 0:
        window.blit(back_fon, (sdvig_fona - window_width, 0))

    # Отрисовка всех спрайтов
    all_sprites.draw(window)

    pygame.display.update()
    time.sleep(0.02)

pygame.quit()
