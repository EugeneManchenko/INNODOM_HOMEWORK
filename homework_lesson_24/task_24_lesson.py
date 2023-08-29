"""ЗАДАНИЕ
В ВАШЕЙ БАЗЕ ДАННЫХ ЕСТЬ ТАБЛИЦА "BOOKS" СО СЛЕДУЮЩИМИ СТОЛБЦАМИ: "ID" (ЦЕЛОЕ ЧИСЛО, ПЕРВИЧНЫЙ КЛЮЧ),
"TITLE" (ТЕКСТОВЫЙ ТИП), "AUTHOR" (ТЕКСТОВЫЙ ТИП), "YEAR" (ЦЕЛОЕ ЧИСЛО) И "PRICE" (ВЕЩЕСТВЕННЫЙ ТИП).
ВАМ НЕОБХОДИМО ВЫПОЛНИТЬ СЛЕДУЮЩИЕ ДЕЙСТВИЯ:

- ВСТАВЬТЕ НЕСКОЛЬКО ЗАПИСЕЙ В ТАБЛИЦУ "BOOKS" С ИНФОРМАЦИЕЙ О
РАЗЛИЧНЫХ КНИГАХ, ВКЛЮЧАЯ НАЗВАНИЕ, АВТОРА, ГОД ИЗДАНИЯ И ЦЕНУ.

- ВЫБЕРИТЕ ВСЕ ЗАПИСИ ИЗ ТАБЛИЦЫ "BOOKS", ОТСОРТИРОВАННЫЕ ПО ГОДУ ИЗДАНИЯ В ПОРЯДКЕ ВОЗРАСТАНИЯ.

- ВЫБЕРИТЕ КНИГИ, У КОТОРЫХ ЦЕНА ВЫШЕ ОПРЕДЕЛЕННОГО ЗНАЧЕНИЯ.

- ОБНОВИТЕ ЦЕНУ КНИГИ С ОПРЕДЕЛЕННЫМ ID.

- УДАЛИТЕ КНИГИ, У КОТОРЫХ ГОД ИЗДАНИЯ МЕНЬШЕ ОПРЕДЕЛЕННОГО ЗНАЧЕНИЯ."""

import sqlite3

# cоздание подключения к базе данных
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# cоздание таблицы "Books"
cursor.execute('''CREATE TABLE IF NOT EXISTS Books
                  (id INTEGER PRIMARY KEY,
                  title TEXT,
                  author TEXT,
                  year INTEGER,
                  price REAL)''')

# вставка записей в таблицу "Books"
books_data = [
    ("Мастер и Маргарита", "Михаил Булгаков", 1967, 18.99),
    ("Преступление и наказание", "Фёдор Достоевский", 1866, 9.99),
    ("Война и мир", "Лев Толстой", 1869, 13.99)
]

cursor.executemany("INSERT INTO Books (title, author, year, price) VALUES (?, ?, ?, ?)", books_data)

# выборка всех записей из таблицы "Books", отсортированных по году издания
cursor.execute("SELECT * FROM Books ORDER BY year ASC")
books = cursor.fetchall()
print("Все книги, отсортированные по году издания:")
for book in books:
    print(book)

# выборка книг с ценой выше определенного значения
price_limit = 15.00
cursor.execute("SELECT * FROM Books WHERE price > ?", (price_limit,))
books = cursor.fetchall()
print(f"\nКниги с ценой выше {price_limit}:")
for book in books:
    print(book)

# обновление цены книги с определенным ID
book_id = 1
new_price = 14.99
cursor.execute("UPDATE Books SET price = ? WHERE id = ?", (new_price, book_id))
conn.commit()
print(f"\nЦена книги с ID {book_id} обновлена.")

# удаление книг с годом издания меньше определенного значения
year_limit = 1870
cursor.execute("DELETE FROM Books WHERE year < ?", (year_limit,))
conn.commit()
print(f"\nУдалены книги с годом издания меньше {year_limit}.")

# закрываем соединение
conn.close()