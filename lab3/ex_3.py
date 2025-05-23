import pygame
import time

pygame.init()

# Глобальные переменные (настройки)
window_width = 800
window_height = 600
fon = './assets/background.png'  # изображение должно быть в том же каталоге, что и код на питоне
hero_image = './assets/player.png'  # путь к изображению героя
box_image = './assets/box.png'
arrow_image = './assets/arrow.png'

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

class Box(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, x_speed=2):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = x_speed

    def update(self):
        self.rect.x += self.x_speed
        if self.rect.right > window_width or self.rect.left < 0:
            self.x_speed = -self.x_speed

class Arrow(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > window_width:
            self.kill()

# Запуск
window = pygame.display.set_mode([window_width, window_height])  # создание окна указанных размеров
pygame.display.set_caption("Игра v1.2")  # установка надписи окна программы

# Создание спрайтов
player = Player(hero_image)
box1 = Box(box_image, 300, 200)
box2 = Box(box_image, 500, 300)

# Группы спрайтов
all_sprites = pygame.sprite.Group()
arrows = pygame.sprite.Group()
boxes = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(box1)
all_sprites.add(box2)
boxes.add(box1)
boxes.add(box2)

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
            elif event.key == pygame.K_SPACE:
                # Создаем новую стрелу при нажатии пробела
                arrow = Arrow(arrow_image, player.rect.right - 10, player.rect.centery - 30)  # Adjust y by half of arrow height
                all_sprites.add(arrow)
                arrows.add(arrow)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player.x_speed = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                player.y_speed = 0

    # Обновление позиций
    all_sprites.update()

    # Проверка коллизий
    hits = pygame.sprite.groupcollide(arrows, boxes, True, True)
    for hit in hits:
        all_sprites.remove(hit)

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
