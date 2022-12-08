#программуа, которая принимает с клавиатуры 3 числа и выводит на экран количество уникальных чисел.


list = []

for i in range (3):
    a = int(input("введите номер:   "))
    list.append(a)
    
my_set = set(list)

unique = len(my_set)


print(f' Количество уникальных чисел равно {unique}')
