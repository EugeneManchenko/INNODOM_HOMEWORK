"""ЗАДАНИЕ 3
НЕОБХОДИМО ВЫПОЛНИТЬ ОПЕРАЦИЮ ОБНОВЛЕНИЯ ДАННЫХ В НЕСКОЛЬКИХ СВЯЗАННЫХ ТАБЛИЦАХ БАЗЫ ДАННЫХ.
ТАКЖЕ НУЖНО УБЕДИТЬСЯ, ЧТО ДАННЫЕ ОСТАЮТСЯ ЦЕЛОСТНЫМИ И В СЛУЧАЕ СБОЯ МОЖНО ВЫПОЛНИТЬ ОТКАТ ИЗМЕНЕНИЙ.
ИСПОЛЬЗУЙТЕ ТРАНЗАКЦИЮ ДЛЯ ГРУППИРОВКИ ОПЕРАЦИЙ ОБНОВЛЕНИЯ И СОЗДАЙТЕ НЕОБХОДИМЫЕ ИНДЕКСЫ
ДЛЯ УЛУЧШЕНИЯ ПРОИЗВОДИТЕЛЬНОСТИ ЗАПРОСОВ."""

"""
import sqlite3

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('task3base.db')
c = conn.cursor()

# Создаем таблицу "Клиенты"
c.execute('''CREATE TABLE Clients
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             email TEXT)''')

# Создаем таблицу "Заказы"
c.execute('''CREATE TABLE Orders
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             client_id INTEGER,
             product_name TEXT,
             quantity INTEGER,
             FOREIGN KEY (client_id) REFERENCES Clients(id))''')

# Создаем индекс для таблицы "Заказы" по полю "client_id"
c.execute('''CREATE INDEX idx_orders_client_id ON Orders (client_id)''')

# Сохраняем изменения и закрываем соединение с базой данных
conn.commit()
conn.close()"""

import sqlite3

# устанавливаю соединение с базой данных
conn = sqlite3.connect('task3base.db')
c = conn.cursor()

# начинаю транзакцию
conn.execute('BEGIN TRANSACTION')

try:
    # выполняю операции обновления данных
    c.execute("INSERT INTO Clients (name, email) VALUES (?, ?)", ('Алексей Коханский', 'alex.koh@gmail.com'))
    client_id = c.lastrowid

    c.execute("INSERT INTO Orders (client_id, product_name, quantity) VALUES (?, ?, ?)", (client_id, 'SSD Hard', 2))
    order_id = c.lastrowid

    # если необходимо выполнить откат изменений, я раскомментирую следующую строку
    # raise Exception("Rollback")

    # подтверждаем изменения
    conn.commit()
    print("Данные успешно обновлены.")
except Exception as e:
    # в случае исключения выполняем откат изменений
    conn.rollback()
    print("Произошла ошибка. Изменения отменены.", str(e))

# закрываю соединение с базой данных
conn.close()
