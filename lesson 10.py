# def select(a,b):
#     for i in a:
#         i+=b
#
# g = [1,2,4,5]
# b = int(input())
# a = select(g,b)
# print(a)

# def x(b[4]):
#     b[0]=5
# v=[1,2,3,[3,4,5,3]]
# x(v)
# print(v)
#
# class Animal:
#     def make_sound(self, s):
#         print(s)
# class Horse(Animal):
#     pass
# pony = Horse()
# pony.make_sound("Igogo")

# class Parent:
#     def buy(self,s,b):
#         s+=b
#         print(s)
#
# class Child(Parent):
#     def sell(self,s,a):
#         s-=a
#         print(s)
#
# family = Child()
# family.buy(10,5)
# family.sell(10,4)


# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# class SuperCar(Car):
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(model, color, year)
#         self.sponsor = sponsor
# matiz = SuperCar('Matiz','white','2000','GMavto')
# mashina = SuperCar('ANG','Green','2016','Mercedes')
# b = vars(mashina)
# a = vars(matiz)
# print(b,a)

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
# rectangle = Rectangle(4, 5)
# print(rectangle.area)
#
# rectangle.width = 6
# print(rectangle.area)

# class Worker:
#     def __init__(self, name, status):
#         self.name = name
#         self.status = status
#
# class HR(Worker):
#     def __init(self, name, status):
#         super().__init__(self, name, status)
#
#     def Check(self):
#         return self.name, self.status
#
# worker = Worker('Kolya', 'Rabochiy')
# worker1 = HR('Kolya', 'Rabochiy')
# worker2 = HR('Kolya', 'Rabochiy')
#
# worker.check()


class Player:
    def __init__(self, stamina, speed, accuracy, power):
        self.stamina = stamina
        self.speed = speed
        self.accuracy = accuracy
        self.power = power

class Attaker(Player):
    def __init__(self, stamina, speed, accuracy, power):
        super().__init__(stamina, speed, accuracy, power)
    def goal(self):
        print("Attack")

class Defender(Player):
    def __init__(self, stamina, speed, accuracy, power):
        super().__init__(stamina, speed, accuracy, power)
    def defend(self):
        print("Take ball")

class Half_Defender(Player):
    def __init__(self, stamina, speed, accuracy, power):
        super().__init__(stamina, speed, accuracy, power)
    def attack(self):
        print('Fast Run')

class GoalKeeper(Player):
    def __init__(self, stamina, speed, accuracy, power):
        super().__init__(stamina, speed, accuracy, power)
    def handball(self):
        print('fast reaction')




