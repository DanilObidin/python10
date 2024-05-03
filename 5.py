try:
    a = int(input())
    b = int(input())
    c = int(input())
    print(a/b+c)
except ValueError:
    print('dataerror')
except ZeroDivisionError:
    print('division by 0')

