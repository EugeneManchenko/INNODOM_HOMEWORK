"""ЗАДАНИЕ 1
НЕОБХОДИМО ВЫПОЛНИТЬ ОПЕРАЦИЮ ВСТАВКИ ДАННЫХ В НЕСКОЛЬКО ТАБЛИЦ БАЗЫ ДАННЫХ И УБЕДИТЬСЯ, ЧТО ЭТИ ОПЕРАЦИИ ВЫПОЛНЯЮТСЯ
ВСЕ ИЛИ НИ ОДНА. ИСПОЛЬЗУЙТЕ ТРАНЗАКЦИЮ, ЧТОБЫ ОБЕСПЕЧИТЬ АТОМАРНОСТЬ ОПЕРАЦИЙ. ЕСЛИ ХОТЯ БЫ ОДНА ИЗ ОПЕРАЦИЙ
НЕ ВЫПОЛНИТСЯ УСПЕШНО,
ВСЕ ИЗМЕНЕНИЯ ДОЛЖНЫ БЫТЬ ОТМЕНЕНЫ."""

import sqlite3

# подключение к базе данных
conn = sqlite3.connect('task1.db')
cursor = conn.cursor()

try:
    # создание таблиц
    cursor.execute('''CREATE TABLE IF NOT EXISTS table1
                      (column1 TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS table2
                      (column1 TEXT)''')

    # начало транзакции - выполнение BEGIN
    cursor.execute('BEGIN')

    # выполнение операций вставки данных
    cursor.execute("INSERT INTO table1 (column1) VALUES ('value1')")
    cursor.execute("INSERT INTO table2 (column1) VALUES ('value2')")

    # завершение транзакции - фиксация изменений
    conn.commit()

    print("Все операции выполнены успешно.")
except:
    # откат изменений в случае ошибки
    conn.rollback()
    print("Произошла ошибка. Отмена всех изменений.")

# закрытие соединения с базой данных
conn.close()
