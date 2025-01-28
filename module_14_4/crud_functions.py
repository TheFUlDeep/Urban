import sqlite3


def initiate_db():
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()

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
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products
