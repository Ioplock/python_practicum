import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ефимов Станислав Александрович - Анимация")
clock = pygame.time.Clock()

# Базовый класс для фигур
class Shape:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.width = 0  # Будет установлено в подклассах
        self.height = 0  # Будет установлено в подклассах

    def move(self):
        # Предварительное вычисление новой позиции
        new_x = self.x + self.speed
        
        # Проверка границ окна с учетом размеров фигуры
        if new_x < 0 or new_x + self.width > WINDOW_WIDTH:
            self.speed = -self.speed  # Смена направления
            self.color = [random.randint(0, 255) for _ in range(3)]  # Случайный цвет
            # Корректировка позиции, чтобы фигура не выходила за границы
            self.x = max(0, min(WINDOW_WIDTH - self.width, new_x))
        else:
            self.x = new_x

    def draw(self):
        pass

    def check_click(self, pos):
        pass

# Класс для квадрата
class Square(Shape):
    def __init__(self, x, y, size, color, speed):
        super().__init__(x, y, color, speed)
        self.size = size
        self.width = size
        self.height = size

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])

    def check_click(self, pos):
        if self.x <= pos[0] <= self.x + self.size and self.y <= pos[1] <= self.y + self.size:
            self.color = [random.randint(0, 255) for _ in range(3)]

# Класс для прямоугольника
class Rectangle(Shape):
    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y, color, speed)
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def check_click(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            self.color = [random.randint(0, 255) for _ in range(3)]

# Класс для круга
class Circle(Shape):
    def __init__(self, x, y, radius, color, speed):
        super().__init__(x, y, color, speed)
        self.radius = radius
        self.width = radius * 2
        self.height = radius * 2

    def move(self):
        # Предварительное вычисление новой позиции
        new_x = self.x + self.speed
        
        # Проверка границ окна с учетом радиуса круга
        if new_x - self.radius < 0 or new_x + self.radius > WINDOW_WIDTH:
            self.speed = -self.speed  # Смена направления
            self.color = [random.randint(0, 255) for _ in range(3)]  # Случайный цвет
            # Корректировка позиции, чтобы круг не выходил за границы
            self.x = max(self.radius, min(WINDOW_WIDTH - self.radius, new_x))
        else:
            self.x = new_x

    def draw(self):
        pygame.draw.circle(screen, self.color, [int(self.x), int(self.y)], self.radius)

    def check_click(self, pos):
        distance = ((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2) ** 0.5
        if distance <= self.radius:
            self.color = [random.randint(0, 255) for _ in range(3)]

# Класс для треугольника
class Triangle(Shape):
    def __init__(self, x, y, size, color, speed):
        super().__init__(x, y, color, speed)
        self.size = size
        self.width = size
        self.height = size

    def draw(self):
        points = [(self.x, self.y), (self.x + self.size, self.y), 
                 (self.x + self.size // 2, self.y - self.size)]
        pygame.draw.polygon(screen, self.color, points)

    def check_click(self, pos):
        # Улучшенная проверка клика для треугольника
        if self.x <= pos[0] <= self.x + self.size and self.y - self.size <= pos[1] <= self.y:
            # Проверка, находится ли точка внутри треугольника
            x1, y1 = self.x, self.y
            x2, y2 = self.x + self.size, self.y
            x3, y3 = self.x + self.size // 2, self.y - self.size
            
            def sign(p1, p2, p3):
                return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
            
            d1 = sign(pos, (x1, y1), (x2, y2))
            d2 = sign(pos, (x2, y2), (x3, y3))
            d3 = sign(pos, (x3, y3), (x1, y1))
            
            has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
            has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
            
            if not (has_neg and has_pos):
                self.color = [random.randint(0, 255) for _ in range(3)]

# Создание фигур
shapes = [
    Square(100, 100, 50, [255, 0, 0], 2),              # Квадрат
    Rectangle(200, 200, 100, 50, [0, 255, 0], 5),      # Прямоугольник
    Circle(300, 300, 30, [0, 0, 255], 3),             # Круг
    Triangle(400, 400, 60, [255, 255, 0], 6)          # Треугольник
]

# Главный цикл анимации
running = True
while running:
    screen.fill([255, 255, 255])  # Очистка экрана

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for shape in shapes:
                shape.check_click(pos)

    # Движение и отрисовка фигур
    for shape in shapes:
        shape.move()
        shape.draw()

    pygame.display.flip()  # Обновление экрана
    clock.tick(FPS)  # Ограничение FPS

pygame.quit()
