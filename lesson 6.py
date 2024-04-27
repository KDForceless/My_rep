# x = {'name':'Pasha','job':'TGbot creator'}
# print(x['name'],x['job'])

# data = {
# #     'name': ['Jordan', 'Pavel'],
# #     'age': (12, 21),
# #     'job': 'programmers'
# #         }
# #
# # print(data['name'][0], data['job'][-1])


# instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
# print(instructor.values())
# print(instructor.keys())
# print(instructor.items())

# instructor = {'name': "Jordan", 'age': 21, 'job': 'programmer'}
#
# if 21 in instructor:
#     print('Да есть')
# else:
#     print("Не понимаю о чем вы")

# users = {}
# users['name'] = 'Jordan'
#
# print(users)
# print(users['name'])

# my_dict = {'name': 'Jordan'}
# my_dict['name'] = 'Pasha'
# print(my_dict)
# my_dict.update({'name': 'Mickle'})
# print(my_dict)
# my_dict['name'] = 'Jordan', 'Peter'
# print(my_dict)

# user = ['post','likes','comments', 'followers','following','saves','stories']
# # user1 = {}.fromkeys("user", 0)
# user1 = {}
#
# user1 = {}.fromkeys(user, 0)
# print(user1)

# instructor = dict(name='Jordan', age = 21, job= 'programmer')
# for i in instructor.keys():
#     print(i)
# for j in instructor.values():
#     print(j)
# for k,m in instructor.items():
#     print(k,m)


all_product = {'Весь склад': {}}
while True:
    admin = input('Что вы хотите сделать?')
    if admin.lower() == "add":
        product_name = input('Enter product name:')
        product_count = input('Enter product count:')

        if product_count.isnumeric():
            all_product['Весь склад'][product_name] = int(product_count)
        else:
            print('not number')
    elif admin == "Stop":
        break
    elif admin.lower() == "product":
        print(all_product)
    else:
        print('no such a command')

