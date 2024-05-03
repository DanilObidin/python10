with open("C:/Users\dan27\OneDrive\Рабочий стол\haha7.txt", encoding='utf-8') as f:
    for l in f:
        if not l.startswith('100'):
            print(l, end='')