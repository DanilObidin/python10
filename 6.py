try:
    with open("C:/Users\dan27\OneDrive\Рабочий стол\haha6.txt") as f:
        l = f.readline()
        k = 0
        for i in f:
            k += 1
        if int(l) == k:
            print("yes")
        if int(l) != k:
            print("no")
except ValueError:
    print("error")