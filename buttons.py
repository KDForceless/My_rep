from telebot import types

#Кнопка для отправки номера
def num_button():
    #Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #Создаем кнопки
    but1 = types.KeyboardButton('Отправить номер телефона', request_contact=True)
    #Добавляем кнопки в пространство
    kb.add(but1)
    return kb

#Кнопка для отправки локации
def loc_button():
    #Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #Создаем кнопки
    but2 = types.KeyboardButton('Отправить геопозицию', request_location=True)
    #Добавляем кнопки в пространство
    kb.add(but2)
    return kb

# Кнопка админ меню
def admin_menu():
    #Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #Создаем сами кнопки
    add = types.KeyboardButton('Добавить продукт')
    delete = types.KeyboardButton('Удалить продукт')
    change = types.KeyboardButton('Изменить продукт')
    back = types.KeyboardButton('Обратно в меню')
    #Дбавляем кнопки в пространство
    kb.add(add, delete, change)
    kb.row(back)
    return kb

#Кнопки для подтверждения
def confirm_buttons():
    #Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #Создаем сами кнопки
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    #Добавляем кнопки в просоранство
    kb.add(yes, no)

#кнопки выбора продукта
def pr_buttons(products):
    #Создаем пространство
    kb = types.InlineKeyboardMarkup(row_width=2)
    #Создаем кнопки
    cart = types.InlineKeyboardButton(text='Корзина', callback_data='cart')
    all_products = [types.InlineKeyboardButton(text=i[1], callback_data=i[0]) for i in products
                    if i[2]>0]
    #добавляет кнопки в пространство
    kb.add(*all_products)
    kb.row(cart)
    return kb

def choose_lang(arg=''):
    kb = types.InlineKeyboardMarkup(row_width=2)
    rus = types.InlineKeyboardButton(text='Русский',callback_data='Russian')
    uzb = types.InlineKeyboardButton(text='Узбекский',callback_data='Uzbek')
    if arg == 'Russian':
        lang = types.InlineKeyboardButton(text=str('Теперь язык русский'))
    if arg == 'Uzbek':
        lang = types.InlineKeyboardButton(text=str('Endi til o‘zbek tilidir'))
    kb.add(rus, uzb)
    return kb

def choose_pr_count_buttons(plus_or_minus='',amount=1):
    #пространство
    kb = types.InlineKeyboardMarkup(row_width=3)

    minus = types.InlineKeyboardButton(text='-',callback_data='decrement')
    count = types.InlineKeyboardButton(text=amount,callback_data=amount)
    plus = types.InlineKeyboardButton(text='+',callback_data='increment')
    to_cart = types.InlineKeyboardButton(text='Добавить в корзину',callback_data='to_cart')
    back = types.InlineKeyboardButton(text='назад',callback_data='back')


    if plus_or_minus == 'decrement':
        if amount > 1:
            count = types.InlineKeyboardButton(text=str(amount-1), callback_data=amount)
        elif plus_or_minus == 'increment':
            count = types.InlineKeyboardButton(text=str(amount + 1), callback_data=amount)

    kb.add(minus, count, plus)
    kb.row(to_cart, back)
    return kb