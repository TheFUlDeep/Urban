import sqlite3


def initiate_db():
    connection = sqlite3.connect('db2.db')
    cursor = connection.cursor()

    # cursor.execute("DROP TABLE IF EXISTS Users")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT noT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)

    # cursor.execute("DROP TABLE IF EXISTS Products")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)
    # for i in range(1, 5):
    #     cursor.execute("INSERT INTO Products (title, description, price) VALUES(?, ?, ?)",
    #                    (f'Product{i}', f"Описание {i}", f'{i}00'))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('db2.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


def is_included(username):
    connection = sqlite3.connect('db2.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM Users WHERE username = ?", (username,))
    res = cursor.fetchone()
    connection.close()
    if res:
        return True
    else:
        return False


def add_user(username, email, age):
    connection = sqlite3.connect('db2.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, 1000))
    connection.commit()
    connection.close()
