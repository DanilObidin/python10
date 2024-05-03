with open("C:/Users\dan27\OneDrive\Рабочий стол\haha4.txt", encoding='utf-8') as f:
    for l in f:
        if len(l) > 20:
            print(l, end='')