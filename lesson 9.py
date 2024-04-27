# class Phone:
#     name = 'Samsung'
#     model = 'SM096'
#     sound = 'Volumebit'
#     material = 'Aluminium'
#     glass = 'retina'
#     chip = 'Snapdradon890'

# class Notebook:
#     def __init__(self, model, processor, videocard, RAM, storage):
#         self.model = model         #AsusRogStrix
#         self.processor = processor #i9-13700
#         self.videocard = videocard #nvidiaRTX4090
#         self.RAM = RAM             #96GB
#         self.storage = storage     #2TB
#
# asus = Notebook('AsusRogStrix','i9-13700','nvidiaRTX4090','96GB','2TB')
# macbook = Notebook(RAM='8GB', storage='1TB', processor='A1', videocard='Nothing', model='AppleMacbook2024')
# user1 = Phone()
# print(vars(asus))
# print(vars(macbook))

# class Comment:
#     def __init__(self, username, text,likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
#     def change_text(self, new_text):
#         self.text = new_text
#
#     def stop(self):
#         print('Notebook turned off')
#
# com = Comment('Abdulazis','Datastructure information is important')
# print(com.text)
# a = str(input('text: '))
# com.change_text(a)
# print(com.text)

class BankAccaunt:
    def __init__(self, name, balance=0.0 ):
        self.name = name
        self.balance = balance


    def deposit(self, how_much):
        self.balance += how_much

    def cash(self, how_much):
        self.balance -= how_much


    def balance(self):
        print(self.balance)

sasha = BankAccaunt("Sasha")
print(sasha.deposit(90))
print(sasha.cash(70))
print(sasha.balance)


