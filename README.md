# Практикум по программированию. Лабы

## Настройка окружения

### Вариант 1: Использование venv

1. Создание виртуального окружения:
```bash
python -m venv venv
```

2. Активация виртуального окружения:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/MacOS:
```bash
source venv/bin/activate
```

3. Установка зависимостей:
```bash
pip install -r requirements.txt
```

### Вариант 2: Использование Poetry

1. Установка Poetry (если еще не установлен):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Установка зависимостей:
```bash
poetry install
```

3. Активация виртуального окружения:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/MacOS:
```bash
source venv/bin/activate
```

## Запуск лабораторных работ

### Лабораторная работа 2: Pygame
- [Описание лабораторной работы](lab2/README.md)
- Запуск:
```bash
cd lab2
python ex_{n}.py
```

### Лабораторная работа 3: Pygame спрайты и фон
- [Описание лабораторной работы](lab3/README.md)
- Запуск:
```bash
cd lab3
python ex_{n}.py
```

### Лабораторная работа 4: Модификация игры
- [Описание лабораторной работы](lab4/README.md)
- Запуск:
```bash
cd lab4/game
python arcada_main.py
```