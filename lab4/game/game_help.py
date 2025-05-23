import pygame
from constants import *

class Help:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 48)
        
    def line(self, points=0, lives=3):
        """Создает строку с информацией о текущем состоянии игры"""
        text = f"Очки: {points} | Жизни: {lives}"
        return self.font.render(text, True, (255, 255, 255))

    def show_help(self, window):
        """Показывает меню помощи"""
        # Заголовок
        title = self.title_font.render("Управление и правила игры", True, (255, 255, 255))
        title_rect = title.get_rect(center=(win_width/2, 50))
        window.blit(title, title_rect)

        # Основные элементы управления
        controls = [
            "Управление персонажем:",
            "A или ← - движение влево",
            "D или → - движение вправо",
            "W или ↑ - прыжок",
            "Пробел - стрельба",
            "",
            "Дополнительные клавиши:",
            "H - показать/скрыть это меню",
            "M - включить/выключить музыку",
            "U - увеличить громкость",
            "J - уменьшить громкость",
            "",
            "Цель игры:",
            "Достигните финиша, избегая врагов",
            "Стреляйте во врагов для получения очков",
            "У вас есть 3 жизни, берегите их!",
            "",
            "Нажмите H для возврата в игру"
        ]

        # Отображение текста
        y = 100
        for line in controls:
            if line:  # Если строка не пустая
                if line.endswith(":"):  # Если это заголовок
                    text = self.font.render(line, True, (255, 255, 0))
                else:
                    text = self.small_font.render(line, True, (255, 255, 255))
                text_rect = text.get_rect(left=50, top=y)
                window.blit(text, text_rect)
            y += 30  # Увеличиваем отступ для следующей строки


