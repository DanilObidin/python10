import os

with open("C:/Users\dan27\OneDrive\Рабочий стол\haha9.txt", encoding='utf-8') as f:
    l = 1
    for i in f:
        if l % 2 == 0:
            print(i, end='')
        l += 1