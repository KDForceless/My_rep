from telebot import types


# Кнопка для отправки номера
def num_button():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем кнопки
    but1 = types.KeyboardButton('Отправить номер телефона', request_contact=True)
    # Добавляем кнопки в пространство
    kb.add(but1)
    return kb


# Кнопка для отправки локации
def loc_button():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем кнопки
    but2 = types.KeyboardButton('Отправить геопозицию', request_location=True)
    # Добавляем кнопки в пространство
    kb.add(but2)
    return kb


# Кнопка админ меню
def admin_menu():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    add = types.KeyboardButton('Добавить продукт')
    delete = types.KeyboardButton('Удалить продукт')
    change = types.KeyboardButton('Изменить продукт')
    back = types.KeyboardButton('Обратно в меню')
    # Дбавляем кнопки в пространство
    kb.add(add, delete, change)
    kb.row(back)


# Кнопки для подтверждения
def confirm_buttons():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    # Добавляем кнопки в просоранство
    kb.add(yes, no)
