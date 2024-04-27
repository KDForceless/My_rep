# korzina = {"Картошка": 20}
# print(korzina)
# a = input('Какой элемент изменить')

# a = int(input("1st number: "))
# mat_oper = input("Action: ")
# b = int(input("2nd number: "))
#
# def addition():
#     print(a + b)
#
# addition()

# def my1():
#     x = ['Jordan', 'Pasha', 'Pavel']
#     if 'Jordan' in x:
#         print(x)
#     else:
#         pass
# my1()



import requests
from bs4 import BeautifulSoup


#
# url = 'https://httpbin.org/post'
# data = {'custname': 'Elon Musk',
#         'custtel': '+998999999999',
#         'custemail': 'real-elon@mail.com',
#         'size': 'small',
#         'topping': 'cheese',
#         'delivery': '12.00',
#         'comments': 'hahahaha'
#         }
# print(requests.post(url, data = data))

link = 'http://browser-info.ru'
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')

check_js = block.find('div', id = 'javascript_check')

print(check_js)

