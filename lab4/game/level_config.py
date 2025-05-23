from level import *
from gamesingle import game
from constants import *

level_1 = Level()
level_1.set_back('cave.png')
level_1.set_hero(200, 350)
level_1.min_x = 0 
level_1.max_x = win_width * 15

level_1.add_enemy(0, 650, 300, 600, 750, 3)
level_1.add_enemy(0, 880, 130, 280, 1000, 0)
level_1.add_enemy(0, 1820, 0, 1600, 1950, 1)

level_1.add_enemy(1, 1250, 400, 1120, 1400, 4)
level_1.add_enemy(1, 1700, 100, 1600, 1950, 6)

level_1.add_enemy(1, 3000, 100, 2950, 3300, 8)

level_1.add_enemy(0, 2650, 0, 1600, 2950, 0)
# level_1.add_platform(20, 550, 300, 100, 15, 0, 0)
# level_1.add_platform(100, 50, 300, 250, 5, 0, -5)

# level_1.add_platform(100, 50, 300, 150, 5, 0, -3)
level_1.add_platform(100, 450, 300, 250, 5, 0, 0)

# level_1.add_platform(150, 50, 200, 500, 5, 1.8, 0)
# level_1.add_platform(150, 250, 300, 500, 5, 5, 0)
level_1.add_platform(300, 170, 300, 250, 5, 0, -3)
level_1.add_platform(300, 565, 300, 250, 7, 0, 0)

level_1.add_platform(550, 550, 300, 100, 15, 0, 0)
level_1.add_platform(700, 100, 300, 250, 5, 2, 0)
level_1.add_platform(900, 250, 300, 250, 5, 0, -3)
level_1.add_platform(1100, 550, 300, 100, 15, 0, 0)

level_1.add_platform(1650, 400, 300, 100, 15, 0, 0)
level_1.add_platform(2200, 550, 300, 100, 15, 0, 0)

level_1.add_platform(2620, 180, 300, 340, 5, 0, 4)
level_1.add_platform(2900, 350, 300, 100, 15, 0, 0)

level_1.set_goal(3600, 180)

game.levels.append(level_1)

#  ______________________________________________________________________________________
#  
#                                 ДАЛЬШЕ УРОВЕНЬ 2
#  ______________________________________________________________________________________

level_2 = Level()
level_2.set_back('jungle.png')
level_2.set_hero(200, 350)
level_2.min_x = 0 
level_2.max_x = win_width * 15

# Платформы для первого этапа (более близко расположенные)
level_2.add_platform(100, 450, 300, 250, 5, 0, 0)
level_2.add_platform(450, 400, 300, 250, 5, 0, 0)
level_2.add_platform(800, 350, 300, 250, 5, 0, 0)
level_2.add_platform(1150, 400, 300, 250, 5, 0, 0)
level_2.add_platform(1500, 450, 300, 250, 5, 0, 0)

# Платформы для второго этапа (движущиеся, но более предсказуемые)
level_2.add_platform(1850, 400, 300, 100, 15, 1, 0)  # Уменьшена скорость
level_2.add_platform(2250, 350, 300, 100, 15, 0, -1)  # Уменьшена скорость
level_2.add_platform(2650, 300, 300, 100, 15, 1, 0)  # Уменьшена скорость
level_2.add_platform(3050, 350, 300, 100, 15, 0, -1)  # Уменьшена скорость

# Платформы для финального этапа (более безопасные)
level_2.add_platform(3450, 400, 300, 100, 15, 0, 0)
level_2.add_platform(3800, 350, 300, 100, 15, 0, 0)
level_2.add_platform(4150, 300, 300, 100, 15, 0, 0)
level_2.add_platform(4500, 250, 300, 100, 15, 0, 0)

# Враги первого этапа (не стреляющие, более редкие)
level_2.add_enemy(0, 600, 100, 500, 700, 3)
level_2.add_enemy(0, 1200, 100, 1100, 1300, 3)

# Враги второго этапа (стреляющие, но меньше)
level_2.add_enemy(1, 2000, 100, 1900, 2100, 4)
level_2.add_enemy(1, 2800, 100, 2700, 2900, 4)

# Враги финального этапа (смешанные, но более редкие)
level_2.add_enemy(0, 3600, 100, 3500, 3700, 3)
level_2.add_enemy(1, 4200, 100, 4100, 4300, 4)

# Цель в конце уровня
level_2.set_goal(4800, 200)

game.levels.append(level_2)
