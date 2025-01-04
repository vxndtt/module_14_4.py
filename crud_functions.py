import sqlite3

def initiate_db():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY, 
            title TEXT NOT NULL,
            description TEXT, 
            price INTEGER NOT NULL
        )
    ''')

    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",("Product1", "Описание продукта 1", 100))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", ("Product2", "Описание продукта 2", 200))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", ("Product3", "Описание продукта 3", 300))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",("Product4", "Описание продукта 4", 400))

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products