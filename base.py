#---------------------------------------------------------------------------
                                     # Number
# integer = 42  # integer
# float = 42.42 # float
# pow = 10e3    # 10 000
# print(pow)

# 5 / 2
# # 2
#
# 5.0 / 2
# # 2.5
#
# float(5) / 2
# # 2.5
#---------------------------------------------------------------------------
                                   # type()
# def distance_from_zero(num):
#   if type(num) == int or type(num) == float:
#     return abs(num)
#   else:
#     return "Nope"

# print(type(108))
# print(type(3.14))
# print(type('hello'))
#---------------------------------------------------------------------------
                                    # mim max abs
# def biggest_number(*args):
#     print(max(args))
#     return max(args)
#
# def smallest_number(*args):
#     print(min(args))
#     return min(args)
#
# def distance_from_zero(arg):
#     print(abs(arg))
#     return abs(arg)
#
# distance_from_zero(-40)

#----------------------------------------------------------------------------
                                     # %
# i - integer
# s - string
# d - Десятичное число
# c - Соответствующий символ Unicode
# b - Двоичный формат
# o - Восьмеричный формат
# x - Шестнадцатеричный формат (в нижнем регистре)
# X - Шестнадцатеричный формат (в верхнем регистре)
# n - То же, что и d, но использует местную настройку для разделения числа
# e - Экспоненциальная запись (e в нижнем регистре)
# E - Экспоненциальная запись (E в верхнем регистре)
# f - Отображать фиксированное количество знаков (по умолчанию 6)
# F - То же, что и f, только отображает inf как INF, а nan как NAN
# g - Общий формат. Округляет число до p значащих цифр (Точность по умолчанию: 6)
# G - То же, что и g. Но переключается к E, если число очень большое
# % - Проценты. Делит на 100 и добавляет % в конце

# name = "Mike"
# print("Hello %s" % name)
#----------------------------------------------------------------------------
                                     # Multiplication of string
# a = "Text "
# b = a * 5
# print(b)
#----------------------------------------------------------------------------
                                      # len(), set()
# c = len('world')
# print(c)

# f = "Some words"
# e = len(f)
# print(e)
#---------------------------------------------------------------------------=
                                       # String indexing
# a = 'Hellow'
#
# print(a[0])
# print(a[1])
# b = a[2]
# print(b)
#----------------------------------------------------------------------------
                                       # .lower(), .upper() .capitalize(),
                                       # .title(), .swapcase(), .strip(),
                                       # .rstrip(), .lstrip()
# parrot = "Norwegian Blue"
# print("Norwegian Blue".lower())

# parrot = "norwegian blue"
# print("Norwegian Blue".upper())
#----------------------------------------------------------------------------
                                       # .find(), .rfind(), .index(),
                                       # .rindex(), .replace('x', 'X'),
                                       # .split(), .join(), .isalpha()
                                       # .isalnum(), .isdigit(), .islower()
                                       # .isupper(), .istitle(), .isspace()
                                       # .isnumeric()
# a = 'Hit the ball before it hits you!'
# b = a.find('i')
# print(b)

# a = 'Hit the ball before it hits you!'
# b = a.split(' ', 2)
# print(b)

# list = ['list', 'there', 'be', 'light!']
# variable = " ".join(list)
# print(variable)

# list = ['list', 'there', 'be', 'light!']
# variable = " "
# print(variable.join(list))
#----------------------------------------------------------------------------
                                       # str(), float(), type(), int(), tuple(),
                                       # list(), dict(), ord('a') == 97, chr(97) == 'a'
# pi = 3.14
# a = str(pi)
# b = 'это pi - ' + a
# print(b)
# # print(int(pi))


# radius = float(input("Enter radius: "))

# radius = int(input("Enter radius: "))
#----------------------------------------------------------------------------
                                       # input()
#----------------------------------------------------------------------------
                                       # from ___ import ___
# from math import sqrt
# print(sqrt(25))

# import math
# print(math.sqrt(25))

# from math import *
# print(sqrt(25))

# import math
# everything = dir(math)
# print(everything)
#----------------------------------------------------------------------------
                                     # datetime
# from datetime import datetime
# now = datetime.now()
# print(now)

# from datetime import datetime
# now = datetime.now()
# current_year = now.year
# current_month = now.month
# current_day = now.day
# print(now.year)
# print('%02d-%02d-%04d' % (now.day, now.month, now.year))
#----------------------------------------------------------------------------
                                    # conditionals
# bool_one = 6 > 8 or not 6 < 8 and 7 < 8
# bool_two = 10 != 10 and not 9 != 9 or 9 == 9
# bool_three = 5 > 3 and not (5 != 5 or 4 == 10)
# bool_four = 5 == 5 or 10 != 10 and not 5 != 5
# bool_five = 5 > 20 or not (5 == 5 and 20 < 30)
# # Make me false!
# bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!
# # Make me true!
# bool_two = 2 == 2 or 3 == 2
# # Make me false!
# bool_three = 2 != 2 and 3 != 2
# # Make me true!
# bool_four = 2 == 3 or not 2 == 3
# # Make me true!
# bool_five = 2 == 2 and 10 != 20
#---------------------------------------------------------------------------
                                   # if elif else
# money = 100
# if money <= 50:
#     print('It is bad')
# elif money > 50 and money <=100:
#     print('It is good')
# else:
#     print('You are rich')
#---------------------------------------------------------------------------
                                   # while
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print('I\'d love to go to ' + city.title() + '!')


# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print('Verifying user: ' + current_user.title())
#     confirmed_users.append(current_user)
# print('\nThe following users have been confirmed:')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# responses = {}
#
# polling_active = True
#
# while polling_active:
#     name = input('\nWhat is your name? ')
#     response = input('Which mountain would you like to climb someday? ')
#     responses[name] = response
#     repeat = input('Would you like to let another peerson respond? (yes/ no) ')
#     if repeat == 'no':
#         polling_active = False
#
# print('\n--- Poll Results ---')
# for name, response in responses.items():
#     print(name + ' would like to climb ' + response + '.')

#---------------------------------------------------------------------------
                                   # for in
# a = [1, 3, 5, 4, 3, 7, 8, 6 ,2]
# for item in a:
#     if item <= 5:
#         print(item)
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
                                  # list
                                  # .append(), .insert() del , .pop()
                                  # remove(), .sort(), .sort(reverse=True)
                                  # sorted(), sorted(cars, reverse=True))
                                  # cars.reverse(), len(cars)

# zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# zoo_animals[3] = "cat"
# print(zoo_animals)


# letters = ['a', 'b', 'c']
# letters.append('d')
# print(len(letters))
# print(letters)


# letters = ['a', 'b', 'c', 'd', 'e']
# slice = letters[1:3]
# print(slice)
# print(letters)


# my_list[:2]
# # Grabs the first two items
# my_list[3:]
# # Grabs the fourth through last items


# a = 'канатоходец'
# print(a[::3])


# a = "ABCDE"
# b = a[::-1]
# print(b)


# animals = "catdogfrog"
# # The first three characters of animals
# cat = animals[:3]
# # The fourth through sixth characters
# dog = animals[3:6]
# # From the seventh character to the end
# frog = animals[6:]


# animals = ["ant", "bat", "cat"]
# print(animals.index("bat"))
# animals.insert(1, "dog")
# print(animals)


# my_list = [1,9,3,8,5,7]
# for number in my_list:
#   print(2 * number)


# animals = ["cat", "ant", "bat"]
# animals.sort()
# for animal in animals:
#   print(animal)


# residents = {'Puffin': 104, 'Sloth': 105, 'Burmese Python': 106}
# print(residents['Puffin'])


# menu = {} # Empty dictionary
# menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
# print(menu['Chicken Alfredo'])


# inventory = {}
# inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# print(inventory)


# zoo_animals = {
# 'Unicorn': 'Cotton Candy House',
# 'Sloth': 'Rainforest Exhibit',
# 'Bengal Tiger': 'Jungle House',
# 'Atlantic Puffin': 'Arctic Exhibit',
# 'Rockhopper Penguin': 'Arctic Exhibit'
# }
# del zoo_animals['Unicorn']
# del zoo_animals['Sloth']
# del zoo_animals['Bengal Tiger']
# zoo_animals['Rockhopper Penguin'] = 'Plains Exhibit'
# print(zoo_animals)


# beatles = ["john","paul","george","ringo","stuart"]
# beatles.remove("stuart")
# print(beatles)


# my_dict = {
#   "fish": ["c", "a", "r", "p"],
#   "cash": -4483,
#   "luck": "good"
# }
# print(my_dict["fish"][0])


# inventory = {
#   'gold' : 500,
#   'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
#   'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# }
# # Adding a key 'burlap bag' and assigning a list to it
# inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# # Sorting the list found under the key 'pouch'
# inventory['pouch'].sort()
# # Your code here
# inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# inventory['backpack'].sort()
# inventory['backpack'].remove('dagger')
# inventory['gold'] = inventory['gold'] + 50


# names = ["Adam","Alex","Mariah","Martine","Columbus"]
# for name in names:
#   print(name)
# for name in ["Adam","Alex","Mariah"]:
#   print(name)


# # A simple dictionary
# d = {"foo" : "bar", "too" : "port"}
# for key in d:
#    print(d[key])  # prints "bar"
# for key in {"foo" : "bar", "too" : "port"}:
#     print(d[key])


# numbers = [1, 3, 4, 7]
# for number in numbers:
#   if number > 6:
#     print (number)
# print("We printed 7.")


# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# for item in a:
#     if item % 2 == 0:
#         print(item)


# def count_small(numbers):
#   total = 0
#   for n in numbers:
#     if n < 10:
#       total = total + 1
#   return total
#
# lotto = [4, 8, 15, 16, 23, 42]
# small = count_small(lotto)
# print(small)


# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# def compute_bill(food):
#     total = 0
#     for item in food:
#         if stock[item] > 0:
#             total += prices[item]
#             stock[item] -= 1
#     return total
#---------------------------------------------------------------------------
                                        # Двумерные списки(массивы)
# m = 5
# n = 3
# a = [[1] * m] * n
# print(a)
# a = [[1] * m for i in range(n)]
# print(a)
# a = [[1 for i in range(m)] for j in range(n)]
# print(a)

# n = 4
# m = 4
# a = []
# for i in range(n):
#     a.append([1] * m)
# a[0][0] = 5
# print(a)
###############################################################
# n = 4
# a = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i < j:
#             a[i][j] = 0
#         elif i > j:
#             a[i][j] = 2
#         else:
#             a[i][j] = 1
# print(a)
# for row in a:
#     print(' '.join([str(elem) for elem in row]))

# for i in range(n):
#     a[i][i] = 1
# for i in range(n):
#     for j in range(i + 1, n):
#         a[i][j] = 0
# for i in range(n):
#     for j in range(0, i):
#         a[i][j] = 2
# for row in a:
#     print(' '.join([str(elem) for elem in row]))

# for i in range(n):
#     for j in range(i + 1):
#         a[i][j] = 0
#     a[i][i] = 1
#     for j in range(0, i):
#         a[i][j] = 2
# for row in a:
#     print(' '.join([str(elem) for elem in row]))
#############################################################
# n = 4
# a = [0] * n
# print(a)
# for i in range(n):
#     a[i] = [2] * i + [1] + [0] * (n - i - 1)
# print(a)
# for row in a:
#     print(' '.join([str(elem) for elem in row]))

# n = 4
# a = [0] * n
# a = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]
# for row in a:
#     print(' '.join([str(elem) for elem in row]))
#############################################################
# n, m = [int(i) for i in input().split()]
# a = [[int(j) for j in input().split()] for i in range(n)]
#
# # a = []
# # for i in range(n):
# #     a.append([int(j) for j in input().split()])
#
# st, r = 0, 0
# curr_max = a[0][0]
# for i in range(n):
#     for j in range(m):
#         if a[i][j] > curr_max:
#             curr_max = a[i][j]
#             st, r = i, j
# print(st, r)


#---------------------------------------------------------------------------
                                        # Кортеж tuple()

# a = tuple() # С помощью встроенной функции tuple()
# a = () # С помощью литерала кортежа
#---------------------------------------------------------------------------
                                        # s = set() созд. пустого множества
                                        # s.add(element), s.remove(element),
                                        # s.discard(element), s.clear()

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket) # {'orange', 'banana', 'pear', apple}
# if 'orange' in basket: # True
#     print('Yes')
# else:
#     print('No')
# if 'python' in basket: # False
#     print('Yes')
# else:
#     print('No')

# for i in basket:
#     print(i)

# print(len(set(input().split()) & set(input().split())))

# print(' '.join(sorted(set(input().split()) & set(input().split()))))


# A | B
# A.union(B)
# Возвращает множество, являющееся объединением множеств A и B.
# A |= B
# A.update(B)
# Добавляет в множество A все элементы из множества B.
# A & B
# A.intersection(B)
# Возвращает множество, являющееся пересечением множеств A и B.
# A &= B
# A.intersection_update(B)
# Оставляет в множестве A только те элементы, которые есть в множестве B.
# A - B
# A.difference(B)
# Возвращает разность множеств A и B (элементы, входящие в A, но не входящие в B).
# A -= B
# A.difference_update(B)
# Удаляет из множества A все элементы, входящие в B.
# A ^ B
# A.symmetric_difference(B)
# Возвращает симметрическую разность множеств A и B (элементы, входящие в A или в B, но не в оба из них одновременно).
# A ^= B
# A.symmetric_difference_update(B)
# Записывает в A симметрическую разность множеств A и B.
# A <= B
# A.issubset(B)
# Возвращает true, если A является подмножеством B.
# A >= B
# A.issuperset(B)
# Возвращает true, если B является подмножеством A.
# A < B
# Эквивалентно A <= B and A != B
# A > B
# Эквивалентно A >= B and A != B


#---------------------------------------------------------------------------
                                       # dict(), {}, del alien_0['points'],
                                       # .get(), del,
                                       # .keys(), .values(), .items()
                                       # for name in sorted(favorite_languages.keys()):,
                                       #

# Capitals1 = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
# Capitals2 = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')
# Capitals3 = dict([('Russia', 'Moscow'), ('Ukraina', 'Kiev'), ('USA', 'Washington')])
# Capitals4 = dict(zip(['Russia', 'Ukraine', 'USA'], ['Moscow', 'Kiev', 'Washington']))

# Capitals1.pop('as', None)

# key = 'Ukraine'
# print(Capitals1.get('Russia'))
# if 'Russia' in Capitals1:
#     print(Capitals1['Russia'])
# else:
#     print('NO')
# Capitals1 = [3, 5, 7, 8]
# for i in range(len(Capitals1)):
#     print(Capitals1[i])

# d = {'a': 239, 10: 'b', 12: 100, 'c': 'd'}
# print(d['c'])
#
# if 'a' in d:
#     print('Yes')
# if 'key' not in d:
#     print('Yes')
# d['a'] = 'value'
# print(d)
# d.get('key')
#
# del d[12]
# print(d)
#
# for key in d:
#     print(key, end=';')
# print()
# for key in d.keys():
#     print(key, end=';')
# print()
# for value in d.values():
#     print(value, end=';')
# print()
# for key, value in d.items():
#     print(key, value, end=';')
#---------------------------------------------------------------------------
                                 # function
# def greater_less_equal_5(answer):
#     if answer > 5:
#         return 1
#     elif answer < 5:
#         return -1
#     else:
#         return 0
# print(greater_less_equal_5(4))
# print(greater_less_equal_5(5))
# print(greater_less_equal_5(6))

# def shut_down(s):
#   if s == "yes":
#     return "Shutting down"
#   elif s == "no":
#     return "Shutdown aborted"
#   else:
#     return "Sorry"
# a = shut_down('no')
# print(a)

# def hotel_cost(nights):
#   return 140 * nights
#
# def plane_ride_cost(city):
#   if city == "Charlotte":
#     return 183
#   elif city == "Tampa":
#     return 220
#   elif city == "Pittsburgh":
#     return 222
#   elif city == "Los Angeles":
#     return 475
#
# def rental_car_cost(days):
#   costs = 40 * days
#   if days >= 7:
#     costs -= 50
#   elif days >= 3:
#     costs -= 20
#   return costs
#
# def trip_cost(city, days, spending_money):
#   return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
#
# print trip_cost('Los Angeles', 5, 600)

# def taxcolc(number):
#     if number <= 1000:
#         tax = number * 0.1
#     elif number >= 1001 and number <= 5000:
#         tax = number * 0.2
#     else:
#         tax = number * 0.3
#     return tax
# print(taxcolc(1000))
# print(taxcolc(5000))
# print(taxcolc(7000))

# def buterbrod(bred_pises, mas_gr, chiss_gr, colb_gr):
#     bred = bred_pises * 15 // 2
#     mas = mas_gr // 5
#     chiss = chiss_gr // 10
#     colb = colb_gr // 15
#     butmin = min(bred, mas, chiss, colb)
#     butmax = max(bred, mas, chiss, colb)
#     return butmin, butmax
# # print(buterbrod(15, 500, 1000, 1500))
#
# bred_pises = int(input('Enter bred: '))
# mas_gr = int(input('Enter mas: '))
# chiss_gr = int(input('Enter chiss: '))
# colb_gr = int(input('Enter colb: '))
#
# print(buterbrod(bred_pises, mas_gr, chiss_gr, colb_gr))

# def function_name(argument):
#     pass

# def function_name(argument):
#     global a
#     a = 20
# print(a)
##############################
# def make_album(name_musicion, name_album, number_roads=''):
#     album = {}
#     album[name_musicion] = name_album
#     if number_roads:
#         album['roads'] = number_roads
#     return album
#
# while True:
#     print('Enter musicion and name of album')
#     print('When you finish write (f)')
#     musicion = input('Enter musicion: ')
#     if musicion == 'f':
#         break
#     album_name = input('Enter name of album: ')
#     if album_name == 'f':
#         break
#     album_one = make_album(name_musicion=musicion, name_album=album_name)
#     print(album_one)

###################################

# def print_models(unprinted_designs, completed_models):
#     '''
#     Имитируем печать моделей, пока список не станет пустым.
#     Каждая модель после печати перемещается в completed_models.
#     '''
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         '''Иметация печати на принтере'''
#         print('Priring model: ' + current_design)
#         completed_models.append(current_design)
# def show_comleted_models(completed_models):
#     '''Выводит информацию обо всех напечатанных моделей'''
#     print('\nThe following models have been printed:')
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs=unprinted_designs, completed_models=completed_models)
# show_comleted_models(completed_models=completed_models)

#################################

# def make_pizza(size, *toppings):
#     print('\nMaking a ' + str(size) +
#           '-inch pizza with the following toppings:')
#     for topping in toppings:
#         print('- ' + topping)
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
#     '''Строит словарь с информацией о пользователе'''
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)

# from pizza import  *
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#
# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#
# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#
# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')


#---------------------------------------------------------------------------
                                        # class

# class Dog():
#     '''Простая модель собаки'''
#
#     def __init__(self, name, age):
#         '''Инициализируем атрибуты name и age'''
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         '''Собака садиться по команде'''
#         print(self.name.title() + ' is now sitting.')
#     def roll_over(self):
#         '''Собака перекатывается по команде'''
#         print(self.name.title() + ' rolled over!')
#
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
#
# print('My dog\'s name is ' + my_dog.name.title() + '.')
# print('My dog is ' + str(my_dog.age) + ' years old.')
# my_dog.sit()
# my_dog.roll_over()
#
# print('\nYour dog\'s name is ' + your_dog.name.title() + '.')
# print('Your dog is ' + str(your_dog.age) + ' years old.')
# your_dog.sit()
####################################################
# class Car():
#     '''Простая модель автомобиля'''
#     def __init__(self, make, model, year):
#         '''Иницифлизируем отрибуты описания автомобиля'''
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         '''Возвращает аккуратно отформатированное описание'''
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         '''Выводит пробег в милях'''
#         print('This car has ' + str(self.odometer_reading)
#               + ' miles on it.')
#     def update_odometer(self, mileage):
#         '''Устанавливает заданное значение на одометре'''
#         '''При попытке обработать подкрутки изменение отклоняется'''
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back odometer')
#     def increment_odometer(self, miles):
#         '''Увеличивает показание одометра с заданным приращением'''
#         self.odometer_reading += miles
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
#
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(33)
# my_new_car.read_odometer()



# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
##############################################
# class Car():
#     '''Простая модель автомобиля'''
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self. year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print('This car has ' + str(self.odometer_reading) + ' miles on it.')
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back an odometer!')
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
# class ElectricCar(Car):
#     '''Представляет аспекты машины, специфические для электромобтлей'''
#     def __init__(self, make, model, year):
#         '''Инициализирует атрибуты класса-родителя'''
#         super().__init__(make, model, year)
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
#####################################################

# class Car():
#     '''Простая модель автомобиля'''
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self. year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print('This car has ' + str(self.odometer_reading) + ' miles on it.')
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back an odometer!')
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class Battery():
#     '''Простая модель аккумулятора электромобиля'''
#
#     def __init__(self, battery_size=70):
#         '''Инициализация атрибутов аккумулятора'''
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         '''Выводит информацию о мощности аккумулятора'''
#         print('This car has a ' + str(self.battery_size) + '-kWh battery.')
#
#     def get_range(self):
#         '''Выводит приблезительныйзапас хода для аккумулятора'''
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#
#         message = 'This car can go approximately ' + str(range)
#         message += ' miles on a full charge.'
#         print(message)
#
#
# class ElectricCar(Car):
#     '''Представляет аспекты машины, специфические для электромобтлей'''
#
#     def __init__(self, make, model, year):
#         '''Инициализирует атрибуты класса-родителя'''
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#     # def describe_battery(self):
#     #     '''Выводит информацию о мощности аккумулятора'''
#     #     print('This car has a ' + str(self.battery_size) + '-kWh battery.')
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
#####################################################################
# import car
#
# my_new_car = car.Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#
# my_tesla = car.ElectricCar('tesla', 'model c', 2016)
#
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# from car import Car, ElectricCar
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#
# my_tesla = ElectricCar('tesla', 'model c', 2016)
#
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

#---------------------------------------------------------------------------
                                        # File object
                                        # json.dump(), json.load()

# r - только чтение
# rb - только чтение
# r+ - только читать и писать
# rb+ - только читать и писать
# w - писать, перезаписыват, создавать новый файл если он не существует
# wb - писать, перезаписыват, создавать новый файл если он не существует
# w+ - читать, писать, перезаписывает, создавать новый файл если он не существует
# wb+ - читать, писать, перезаписывает, создавать новый файл если он не существует
# a - курсор в конце, писать, создавать новый файл если он не существует
# ab - курсор в конце, писать, создавать новый файл если он не существует
# a+ - курсор в конце, читать, писать, создавать новый файл если он не существует
# ab+ - курсор в конце, читать, писать, создавать новый файл если он не существует

############################################################

# file_path = 'C:/Users/sletkin001/Desktop/5S/start/hacking.txt'
# with open(file_path) as file_hacing:
#     hacing = file_hacing.read()
#     print(hacing)

# with open('pi.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())
#

# with open('pi.txt') as file_object:
#     file_object = file_object.read()
#     print(file_object)

# with open('pi.txt') as file_object:
#     print(file_object.read().rstrip())

# filename = 'pi.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line)

# filename = 'pi.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())

# filename = 'pi.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# matthes = ''
# for line in lines:
#     matthes += line.strip()
#
# print(matthes)
# print(len(matthes))

# filename = 'empty.txt'
# with open(filename, 'w') as file_object:
#     file_object.write('I love programming.\n')
#     file_object.write('I love creating new games.\n')
#     file_object.write('Hello all!\n')
#
# filename = 'emptyfile.txt'
# with open(filename, 'a') as second_file_object:
#     second_file_object.write('\nI love creating apps that can run in a browser.\n')

# survey = True
# while survey:
#     answer = input('Why are you like programming? if you finish write (finish): ')
#     if 'finish' in answer:
#         survey = False
#     filename = 'guest_book.txt'
#     with open(filename, 'a') as file_object:
#         file_object.write(answer + '\n')

############################################################

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('You can\'t divide by zero')

# print('Give me wo numbers, and I\'ll divide them.')
# print('Enter \'q\' to quit')
#
# while True:
#     first_number = input('\nFirst number: ')
#     if first_number == 'q':
#         break
#     second_number = input('\nSecond number: ')
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print('You can\'t divide by 0!')
#     else:
#         print(answer)

# filename = 'alice.txt'
#
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = 'Sorry, the file ' + filename + ' does not exist.'
#     print(msg)

# def count_words(filename):
#     '''Подсчет приблизительного количества строк в файле'''
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         msg = 'Sorry, the file ' + filename + ' does not exist.'
#         print(msg)
#     else:
#         '''Подсчет приблизительного количества строк в файле'''
#         words = contents.split()
#         num_words = len(words)
#         print('The file ' + filename + ' has about ' + str(num_words) + ' words.')
#
# filename = 'empty.txt'
# count_words(filename)

# def count_words(filename):
#     '''Подсчет приблизительного количества строк в файле'''
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         pass
#     else:
#         '''Подсчет приблизительного количества строк в файле'''
#         words = contents.split()
#         num_words = len(words)
#         print('The file ' + filename + ' has about ' + str(num_words) + ' words.')
#
# filename = 'emptydd.txt'
# count_words(filename)

# def read_file(filename):
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         msg = 'Sorry, the file ' + filename + ' does not exist.'
#         print(msg)
#     else:
#         print(contents)
#
# filenames = ['cats.txt', 'dogs.txt']
# for filename in filenames:
#     read_file(filename)

# filename = 'dogs.txt'
# count_the(filename)
##############################################
# import json
#
# numbers = [2, 3, 5, 7, 11, 13]
#
# filename = 'numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

# import json
#
# filename = 'numbers.json'
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
# print(numbers)

# import json
#
# '''Программа загружает имя пользователя, если оно было сохранено ранее.
# Впротивном случае она запрашивате имя пользователя и сохраняет его.'''
# filename = 'username.json'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input('What is your name?: ')
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print('We\'ll remember you when you come back, ' + username + '!')
# else:
#     print('Welcome back, ' + username + '!')
###############################################
# import json
#
# def greet_user():
#     '''Приветствует пользователя по имени'''
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input('Whan is your name?: ')
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print('We\'ll remember you when you came back, ' + username + '!')
#     else:
#         print('Welcome back, ' + username + '!')
# greet_user()

# import json
#
# def get_stored_username():
#     '''Получает хранимое имя пользователя, если оно существует.'''
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
# def greet_user():
#     '''Приветствует пользователя по имени'''
#     username = get_stored_username()
#     if username:
#         print('Welcome back, ' + username + '!')
#     else:
#         username = input('What is your name?: ')
#         filename = 'username.json'
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print('We\'ll remember you when you come back, ' + username + '!')
# greet_user()

# import json
#
# def get_stored_username():
#     '''Получает хранимое имя пользователя, если оно существует.'''
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
# def get_new_username():
#     '''Запрашивает новое имя пользователя'''
#     username = input('Whan is your name?: ')
#     filename = 'username.json'
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#     return username
#
# def greet_user():
#     '''Приветствуе пользователя по имени'''
#     username = get_stored_username()
#     if username:
#         print('Welcome back, ' + username + '!')
#     else:
#         username = get_new_username()
#         print('We\'ll remember you when you come back, ' + username + '!')
# greet_user()


#---------------------------------------------------------------------------
                                        # unittest.TestCase,

# assertEqual(a, b) - Проверяет, что a == b
# assertNotEqual(a, b) - Проверяет, что a! = b
# assertTrue(x) - Проверяет, что значение х истинно
# assertFalse(x) - Проверяет, что значение х ложно
# assertIn(элемент, список) - Проверяет, что элемент входит в список
# assertNotIn(элемент, список) - Проверяетб что элемент не входит в список
# setUp()

#######################################

# import unittest
#
# from function import get_formatted_name
#
#
# class NamesTestCase(unittest.TestCase):
#     '''Тесты для \'function.py\'.'''
#
#     def test_first_last_name(self):
#         '''Имена вида \'Janis Joplin\' работают правильно?'''
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')
#
#
# unittest.main()
########################################
# import unittest
#
# from matthes import city_country_namecity
#
# class NamesTestCity(unittest.TestCase):
#     '''Тесты для  \'matthes.py\''''
#
#     def test_cuntryname_cityname(self):
#         '''Имена страны и города типа \'Russia, Moscow\' работаю правильно?'''
#         formatted_name = city_country_namecity('england', 'london')
#         self.assertEqual(formatted_name, 'England, London')
#
#     def test_countryname_cityname_population(self):
#         '''Имена страны, города и население типа
#         \'Russia, Moscow - population 50000.\' работаю правильно?'''
#         formatted_name = city_country_namecity('santiago', 'chile', 5000000)
#         self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000.')
#
# unittest.main()
###########################################

# import unittest
# from matthes import AnonymousSurvey
#
# class TestAnonmyousSurvey(unittest.TestCase):
#     '''Тесты для класса AnonymousSurvey'''
#
#     def test_store_three_response(self):
#         '''Проверяет, что один ответ сохранен правильно'''
#         question = 'What Language did you first learn to speak?'
#         my_survey = AnonymousSurvey(question)
#         responses = ['English', 'Spanish', 'Mandrid']
#         for response in responses:
#             my_survey.store_response(response)
#
#         for response in responses:
#             self.assertIn('English', my_survey.responses)
#
# unittest.main()

##########################################
# import unittest
# from matthes import Employee
#
# class TestEmployee(unittest.TestCase):
#
#     def setUp(self):
#         self.employee = Employee('alex', 'slet', 50000)
#
#     def test_give_default_raise(self):
#         self.assertEqual(self.employee.give_raise(), 55000)
#
#     def test_give_custom_raise(self):
#         self.assertEqual(self.employee.give_raise(6000), 56000)
#
# unittest.main()

#---------------------------------------------------------------------------
