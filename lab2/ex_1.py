import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов
COLORS = {
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'ORANGE': (255, 154, 13),
    'YELLOW': (255, 238, 84),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'GRAY': (128, 128, 128),
    'BROWN': (139, 69, 19)
}

# Создание окна с возможностью изменения размера
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
main_window.fill(COLORS['WHITE'])

# Установка заголовка окна
pygame.display.set_caption("Ефимов Станислав Александрович")

# Рисование геометрических фигур
def draw_circles():
    # Красный закрашенный круг
    pygame.draw.circle(main_window, COLORS['RED'], (200, 100), 30)
    
    # Оранжевый круг с контуром
    pygame.draw.circle(main_window, COLORS['ORANGE'], (100, 400), 50, 15)
    
    # Желтый круг в центре
    center_x = main_window.get_width() // 2
    center_y = main_window.get_height() // 2
    pygame.draw.circle(main_window, COLORS['YELLOW'], (center_x, center_y), 100, 5)

def draw_rectangles():
    # Основной прямоугольник
    pygame.draw.rect(main_window, COLORS['YELLOW'], (400, 20, 300, 200))
    
    # Случайные прямоугольники
    for _ in range(5):
        x = random.randint(50, 700)
        y = random.randint(50, 500)
        width = random.randint(10, 200)
        height = random.randint(10, 100)
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.rect(main_window, random_color, (x, y, width, height), 4)

def draw_house():
    # Параметры домика
    roof_points = [
        (400, 150),
        (250, 350),
        (550, 350)
    ]
    
    # Рисование элементов домика
    pygame.draw.polygon(main_window, COLORS['GRAY'], roof_points)
    pygame.draw.rect(main_window, COLORS['RED'], (250, 350, 300, 200))
    pygame.draw.rect(main_window, COLORS['YELLOW'], (325, 400, 50, 50))
    pygame.draw.rect(main_window, COLORS['BROWN'], (360, 450, 80, 100))

def draw_custom_shape():
    # Создание произвольной фигуры
    points = [
        (221, 432), (225, 331), (133, 342), (141, 310), (51, 230),
        (74, 217), (58, 153), (114, 164), (123, 135), (176, 190),
        (159, 77), (193, 93), (230, 28), (267, 93), (301, 77),
        (284, 190), (327, 135), (336, 164), (402, 153), (386, 217),
        (409, 230), (319, 310), (327, 342), (233, 331), (237, 432)
    ]
    pygame.draw.lines(main_window, COLORS['GREEN'], True, points, 2)

def handle_image():
    try:
        image = pygame.image.load("./assets/apple.png")
        initial_pos = (400, 450)
        final_pos = (600, 450)
        
        # Отображение изображения в начальной позиции
        main_window.blit(image, initial_pos)
        pygame.display.flip()
        
        # Задержка и перемещение
        pygame.time.delay(2000)
        pygame.draw.rect(main_window, COLORS['WHITE'], (*initial_pos, 100, 100))
        main_window.blit(image, final_pos)
        pygame.display.flip()
        
        return image
    except pygame.error:
        print("Ошибка при загрузке изображения apple.png")
        return None

def main():
    # Отрисовка всех элементов
    draw_circles()
    draw_rectangles()
    draw_house()
    draw_custom_shape()
    handle_image()
    
    # Основной цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                global main_window
                main_window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                main_window.fill(COLORS['WHITE'])
                # Перерисовка всех элементов при изменении размера окна
                draw_circles()
                draw_rectangles()
                draw_house()
                draw_custom_shape()
                handle_image()
                pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
