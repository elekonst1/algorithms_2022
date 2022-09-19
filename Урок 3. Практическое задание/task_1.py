"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

from time import time


def time_decor(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} '
              f'составило {end - start}')
        return result
    return timer

some_number = 10000
new_list = []

@time_decor
def filling_list(some_list, n):
    for i in range(n):              # O(N)
        some_list.append(i)           # O(1)
    return new_list

filling_list(new_list, some_number)

new_dict = {}

@time_decor
def filling_dict(some_dict, n):
    for i in range(n):             # O(N)
        some_dict[i] = i + 10        # O(1)
    return new_dict

filling_dict(new_dict, some_number)


#Время выполенения функции filling_list составило 0.001341104507446289
#Время выполенения функции filling_dict составило 0.001886129379272461

# Операция заполнения словаря и списка заняли примерно одинаковое время, так как имеют О(1) сложность



numb = 1000
@time_decor
def getting_elem_list(some_list, n):
    for i in range(n):                         # O(N)
        some_list[i] = some_list[i] + 10       # O(1)

getting_elem_list(new_list, numb)



@time_decor
def get_elem_dict(some_dict, n):
    for i in range(n):                        # O(N)
        some_dict[i] = some_dict[i + 10]      # O(1)

get_elem_dict(new_dict, numb)

#Время выполенения функции getting_elem_list составило 0.00014781951904296875
#Время выполенения функции get_elem_dict составило 0.000186920166015625

# Операция по получению элемента словаря и списка заняли примерно одинаковое время, так как имеют О(1) сложность

@time_decor
def del_elem_list(some_list):
    for i in range(1000):                    # O(N)
        del some_list[i]                     # O(N)

del_elem_list(new_list)



@time_decor
def del_elem_dict(some_dict):
    for i in range(1000):                   # O(N)
        del some_dict[i]                    # O(1)


del_elem_dict(new_dict)


#Время выполенения функции del_elem_list составило 0.0032320022583007812
#Время выполенения функции del_elem_dict составило 0.0001327991485595703

"""
В отличии от функции def del_elem_list(some_list) где все операции имеют сложноть О(N),
в функции del_elem_dict(some_dict) одна операция имеет сложность О(N), вторая О(1),
поэтому удаление элемента словаря происходит быстрее.
"""