"""ЗАДАЧА 3

СОЗДАЙТЕ ТАБЛИЦУ "ФИЛЬМЫ" СО СЛЕДУЮЩИМИ ПОЛЯМИ:
    ID (ЦЕЛОЕ ЧИСЛО, ПЕРВИЧНЫЙ КЛЮЧ)
    НАЗВАНИЕ (СТРОКА)
    РЕЖИССЕР (СТРОКА)
    ГОД ВЫПУСКА (ЦЕЛОЕ ЧИСЛО)
    РЕЙТИНГ (ДЕСЯТИЧНОЕ ЧИСЛО)
    ДЛИТЕЛЬНОСТЬ (ЦЕЛОЕ ЧИСЛО)"""

import sqlite3

# cозда. подключение к базе данных
conn = sqlite3.connect('films.db')

# cоздаю курсор для выполнения SQL-запросов
cursor = conn.cursor()

# создаю таблицу "Фильмы"
cursor.execute('''CREATE TABLE Фильмы
                (id INTEGER PRIMARY KEY,
                название TEXT,
                режиссер TEXT,
                год_выпуска INTEGER,
                рейтинг REAL,
                длительность INTEGER)''')

# применяю все изменения в базе данных
conn.commit()

# закрываю подключение
conn.close()
