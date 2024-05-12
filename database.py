import sqlite3

# создание БД
conn = sqlite3.connect('delivery.db', check_same_thread=False)
# Python + SQl
sql = conn.cursor()

# создание таблицы пользователи
sql.execute('CREATE TABLE IF NOT EXISTs users '
            '(id INTEGER, name TEXT, number TEXT, location TEXT);')

# создание таблицы продукты
sql.execute('CREATE TABLE IF NOT EXISTS products '
            '(pr_id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'pr_name TEXT, pr_desc TEXT, pr_price REAL, '
            'pr_photo TEXT, pr_count INTEGER);')

# создание таблицы корзины
sql.execute('CREATE TABLE IF NOT EXISTS cart '
            '(user_id INTEGER, user_product TEXT, '
            'user_quantity INTEGER);')


# методы для пользователя
# Регистрация
def register(id, name, number, location):
    sql.execute('INSERT INTO users VALUES (?, ?, ?, ?);',
                (id, name, number, location))
    # Фиксируем изменения
    conn.commit()


# Проверка на наличие пользователя в БД
def check_user(id):
    if sql.execute('SELECT * FROM users WHERE id=?;', (id,)).fetchone():
        return True
    else:
        return False


# Методы для продукта
# метод для выведения всех товаров
def get_all_pr():
    return sql.execute('SELECT pr_id, pr_name, pr_count FROM products;').fetchall()


# метод для вывода определенного товара
def get_exact_pr(id):
    return sql.execute('SELECT * FROM products WHERE pr_id=?;', (id,)).fetchone()


# Метод для добавления продукта в ДБ
def add_pr(pr_name, pr_desc, pr_price, pr_photo, pr_count):
    sql.execute('INSERT INTO products '
                '(pr_name, pr_desc, pr_price, pr_photo, pr_count) VALUES '
                '(?, ?, ?, ?, ?);',
                (pr_name, pr_desc, pr_price, pr_photo, pr_count))
    # фиксируем изменения
    conn.commit()


# Метод для удаления товара
def del_pr(id):
    sql.execute('DELETE FROM products WHERE pr_id=?;', (id,))

    # фиксируем изменения
    conn.commit()


# Метод для изменения количества товара
def change_pr_count(id, new_count):
    # ТЕкущее количество
    now_count = sql.execute('SELECT pr_count FROM products WHERE pr_id=?;', (id,)).fetchone()
    # НОвое колчество
    plus_count = now_count[0] + new_count
    sql.execute('UPDATE products SET pr_count=? WHERE pr_id;', (plus_count, id)).fetchone()
    # фиксируем изменения
    conn.commit()


# Метод на проверку на наличие товара в БД
def check_pr():
    if sql.execute('SELECT * FROM product;').fetchall():
        return True
    else:
        return False


# Методы для корзины
# Метод для добавления товара в корзину
def add_pr_to_cart(user_id, user_product, user_quantity):
    sql.execute('INSERT INTO cart VALUES (?, ?, ?);', (user_id, user_product, user_quantity))
    # фиксируем изменения
    conn.commit()


# Метод для очистки корзины
def clear_cart(user_id):
    sql.execute('DELETE FROM cart WHERE user_id=?;', (user_id,))
    # фиксируем изменения
    conn.commit()


# Вывод корзины
def show_cart(user_id):
    return sql.execute('SELECT * FROM cart WHERE user_id=?;', (user_id,)).fetchall()


# Оформление коризны
# Оформление заказа
def make_order(user_id):
    # Вещи, которые выбрал пользователь
    product_name = sql.execute('SELECT user_product FROM cart WHERE user_id=?;', (user_id,)).fetchall()
    product_quantity = sql.execute('SELECT user_quantity FROM cart WHERE user_id=?;', (user_id,)).fetchall()
    # Склад
    product_counts = []
    for i in product_name:
        product_counts.append(sql.execute('SELECT pr_count FROM products WHERE pr_name=?;', (i[0],)).fetchone()[0])
    totals = []
    for e, c in product_quantity, product_counts:
        totals.append(c - e[0])
    for t, n in totals, product_name:
        sql.execute('UPDATE products SET pr_count=? WHERE pr_name=?;', (t, n[0]))
    address = sql.execute('SELECT location FROM users WHERE id=?;', (user_id,)).fetchone()
    # Фиксируем изменения
    conn.commit()
    return product_counts, totals, address
