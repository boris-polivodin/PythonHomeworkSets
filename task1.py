# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 

import random

first_list_size = int(input("Задайте размер первого массива: "))
first_list =[random.randint(0, 10) for i in range(first_list_size)]

second_list_size = int(input("Задайте размер второго массива: "))
second_list =[random.randint(0, 10) for i in range(second_list_size)]

print(first_list)
print(second_list)

result_list = sorted(list(set(first_list).intersection(second_list)))
print(result_list)