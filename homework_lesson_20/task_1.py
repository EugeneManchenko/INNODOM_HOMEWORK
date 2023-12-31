"""ЗАДАЧА 1

СОЗДАЙТЕ ТАБЛИЦУ "КНИГИ" СО СЛЕДУЮЩИМИ ПОЛЯМИ:
    ID (ЦЕЛОЕ ЧИСЛО, ПЕРВИЧНЫЙ КЛЮЧ)
    НАЗВАНИЕ (СТРОКА)
    АВТОР (СТРОКА)
    ЖАНР (СТРОКА)
    ГОД ИЗДАНИЯ (ЦЕЛОЕ ЧИСЛО)"""

import sqlite3

# создаю подключение к базе данных
conn = sqlite3.connect('books.db')

# создаю курсор для выполнения SQL-запросов
cursor = conn.cursor()

# создаю таблицу "Книги"
cursor.execute('''CREATE TABLE Книги
                (id INTEGER PRIMARY KEY,
                название TEXT,
                автор TEXT,
                жанр TEXT,
                год_издания INTEGER)''')

# применяю все изменения в базе данных
conn.commit()

# закрываю подключение
conn.close()
