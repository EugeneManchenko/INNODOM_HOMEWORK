"""ЗАДАНИЕ 2
ВАМ ПРЕДОСТАВЛЕНА БАЗА ДАННЫХ СО МНОЖЕСТВОМ ЗАПИСЕЙ. НЕОБХОДИМО ОПТИМИЗИРОВАТЬ ПРОИЗВОДИТЕЛЬНОСТЬ ЗАПРОСА,
КОТОРЫЙ ВЫПОЛНЯЕТ ПОИСК ЗАПИСЕЙ ПО ОПРЕДЕЛЕННОМУ СТОЛБЦУ. СОЗДАЙТЕ ПОДХОДЯЩИЙ ИНДЕКС ДЛЯ ЭТОГО СТОЛБЦА,
ЧТОБЫ УСКОРИТЬ ВЫПОЛНЕНИЕ ЗАПРОСА И СНИЗИТЬ НАГРУЗКУ НА БАЗУ ДАННЫХ."""

import sqlite3

# создаем подключение к базе данных
conn = sqlite3.connect('fruits_base.db')
cursor = conn.cursor()

# создаем таблицу
cursor.execute('''CREATE TABLE IF NOT EXISTS records
                  (id INTEGER PRIMARY KEY,
                  name TEXT,
                  value INTEGER)''')

# предположим, у нас есть набор данных, которые мы хотим добавить в базу данных
data = [
    (1, 'Яблоко', 10),
    (2, 'Арбуз', 20),
    (3, 'Дыня', 30),
]

# добавляем записи в базу данных
cursor.executemany("INSERT INTO records (id, name, value) VALUES (?, ?, ?)", data)

# создаем индекс для столбца "name"
cursor.execute("CREATE INDEX idx_name ON records (name)")

# коммитим изменения
conn.commit()

# выполняем поиск записей по имени
name_to_search = "Дыня"
cursor.execute("SELECT * FROM records WHERE name=?", (name_to_search,))
result = cursor.fetchall()
print(result)

# закрываем соединение
conn.close()