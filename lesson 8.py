# a = lambda x: x**3
# print(a(10))

# x, y ,u - параметры
# 10, 2, 3 -аргументы

# b = lambda  y, u: y + u
# print(b(2,3))
# a = int(input('a='))
# square = lambda i: i*4
# t = int(input('t='))
# f = int(input('f='))
# square = lambda t,f: (t+f)*2
# print(square(t, f))

# def spam(a,b,c=7):
#     return a+b+c
#
# print(spam(3,5))

# def sum(a,b):
#     return (a+b)**2
#
# a = int(input("a = "))
# b = int(input("b = "))
#
# print(sum(a,b))

# all_products = {'Склад':{'name':'Хлеб','Количество': 34}}
#
# def get_products(a = 'name'):
#     print(all_products["Склад"][a])
#
# get_products()

# def spam1(*args):
#     return args
#
# print(spam1(1,2,3,'Hello'))

# def spam1(*kolbasa):
#     for i in kolbasa:
#         print(i)
# spam1(1,2,3,'Hi',15.2)

# def spam1(**kwargs):
#     return kwargs
# print(spam1(name = 'my1', age = 23))

# def ddd(a):
#     while True:
#         if a % 2 == 1:
#             print("Нечетное")
#             break
#         elif a % 2 == 0:
#             print('Четное')
#             break
# a = int(input("enter number: "))
# ddd(a)

# def Add(a,b):
#
#     clients[a] = b
#     opened_rooms.remove(b)
#     closed_rooms.append(b)
#     return ("added")
#
# def check_out(name, room):
#     clients[name] = room
#     opened_rooms.remove(room)
#     closed_rooms.append(room)
#     return "client disposed"
#
# def show_rooms:
#     return closed_rooms
# opened_rooms = [i for i in range(1,21)]
# closed_rooms = [i for i in range(1,21)]
#
# while True:
#     choice = input("What to do")
#     if
#
#     a = str(input("enter name: "))
#     b = int(input("enter number: "))
#     Add(a, b)
#
# clients = {}


a = int(input("a = ")) # b = int(input("b = ")) # c = lambda x, y: x + y # print(c(a,b)) classes = {} previous_year = [i for i in range(1, 12)] this_year = [] def register(name, room): classes[name] = room previous_year.remove(room) this_year.append(room) return 'Ученик успешно вошел!' def check_out(name): this_year.remove(classes[name]) previous_year.insert(classes[name] - 1, classes[name]) classes.pop(name) return 'Ученик успешно вышел!' def change_rem(name, name2, num): this_year.remove(classes[name]) previous_year.insert(classes[name] - 1, classes[name]) classes.pop(name) previous_year.remove(num) classes[name2] = num this_year.append(classes[name2]) return 'Ученик успешно изменен!' def show_rooms(): return this_year while True: choice = input('Что хотите сделать? ') if choice.lower() == 'войти': cl_name = input('Имя ученика: ') print(previous_year) cl_room = input('Класс ученика: ') if cl_room.isnumeric(): register(cl_name, int(cl_room)) else: print('Ошибка!') elif choice.lower() == 'выйти': if classes: cl_name = input('Имя ученика: ') if cl_name in classes: check_out(cl_name) else: print('Такого ученика нет!') else: print('ученика пока нет!') elif choice.lower() == 'изменить': if classes: cl_name = input('Имя ученика: ') cl_name_new = input('Новое имя ученика: ') cl_number_new = input('Новый номер Класса: ') if cl_name in classes: change_rem(cl_name, cl_name_new, int(cl_number_new)) else: print('Такого ученика нет!') else: print('ученика пока нет!') elif choice.lower() == 'комнаты': print('Занятые Классы:\n', show_rooms()) elif choice.lower() == 'открытые_классы': print(previous_year) elif choice.lower() == 'словарь': print(classes) else: print('Ошибка')