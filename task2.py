# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

import random

size = int(input("Задайте размер грядки: "))
if size < 3:
  print('Размер грядки не должен быть менее 3')
elif size == 3:
  berry_bushes =[random.randint(0, 10) for i in range(size)]
  print(berry_bushes)
  print(f'Максимальное количество ягод = {berry_bushes[0]+berry_bushes[1]+berry_bushes[2]}')
else:
  shift = 1
  berry_bushes =[random.randint(0, 10) for i in range(size)]
  print(berry_bushes)
  maximum = berry_bushes[0]+berry_bushes[1]+berry_bushes[2]
  left_bush = berry_bushes[0]
  central_bush = berry_bushes[1]
  rigth_bush = berry_bushes[2]
  for i in range(1, size):
    berry_bushes = berry_bushes[shift:] + berry_bushes[:shift]
    if berry_bushes[0]+berry_bushes[1]+berry_bushes[2] > maximum:
      maximum = berry_bushes[0]+berry_bushes[1]+berry_bushes[2]
      left_bush = berry_bushes[0]
      central_bush = berry_bushes[1]
      rigth_bush = berry_bushes[2]
    # print(berry_bushes)
  print(f'Максимальное количество ягод = {maximum} в кустах {left_bush} {central_bush} {rigth_bush}')
