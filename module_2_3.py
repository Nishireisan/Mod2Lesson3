my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print('Дан список чисел:', my_list, '. Выписать положительные до отрицательного числа')
n = 0
while n < len(my_list):
    if my_list[n] >= 0:
        if my_list[n] == 0:
            n += 1
            continue
        print(my_list[n])
        n += 1
        continue
    else:
        print('Следующее число отрицательное')
        break
