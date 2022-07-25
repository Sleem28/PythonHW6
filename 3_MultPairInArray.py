# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# from random import randint
#
#
# def fill_list(items: int) -> list:  # Get the filled array
#     output_list = list()
#     counter = 0
#
#     while counter < items:
#         output_list.append(randint(1, 50))
#         counter += 1
#
#     return output_list
#
# def mult_opposite_items(input_list:list) -> list:
#     output_list = list()
#     neg_counter = len(input_list)-1
#     half_counter = int(len(input_list)/2)
#
#     if len(input_list)%2 == 0:
#         is_odd = False
#     else:
#         is_odd = True
#
#     for i in range(0,half_counter):
#         output_list.append(input_list[i] * input_list[neg_counter])
#         neg_counter -= 1
#
#     if is_odd:
#         output_list.append(input_list[neg_counter] * input_list[neg_counter])
#     return output_list
#
# #------------------------------------------------------------------------------------------------------------------+
# int_list = fill_list(int(input('Введите размер генерируемого массива: ')))
# print(f'Сгенерированный массив имеет вид {int_list}.')
# print(f'Массив с перемноженными противоположными элементами имеет вид {mult_opposite_items(int_list)}.')

# Это заменяет весь код сверху
from random import randint
rnd_list = [randint(1, 9) for i in range(int(input('Введите количество элементов')))]

print(f'В сгенерированном массиве {rnd_list} произведение противоположных элементов имеет вид '
      f'{list(rnd_list[i] * rnd_list[len(rnd_list)-i-1] for i in range(0, (len(rnd_list) + (0 if len(rnd_list)%2 == 0 else 1))//2))}')
