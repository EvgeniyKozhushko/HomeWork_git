a = int(input("Введите число a "))
b = int(input("Введите число b "))
c = int(input("Введите число c "))

# шаг 1
not_zero = a and b and c
print('Есть нулевое значение' if not_zero == False else 'Нет нулевых значений')

# 3 варивнта как мне не нравится

#not_zero = a and b and c and 'Нет нулевых значений'
#print(not_zero)

#not_zero = a == 0 or b == 0 or c == 0
#print('Есть нулевое значение' if not_zero == True else 'Нет нулевых значений')

#not_zero = (a == 0 and b == 0 and c ==0) or "Нет нулевых значений"
#print(not_zero)

# шаг 2
first_no_zero = a or b or c
print('Введены все нули' if first_no_zero == False else first_no_zero)

# вариант, который не нравится
#first_no_zero = a or b or c or 'Введены все нули'
#print(first_no_zero)

# шаг 3
if a > (b+c):
    print(f'{a - b - c}')

# шаг 4
if a < (b+c):
    print(f'{b + c - a}')

# шаг 5
if a > 50 and (b > a or c > a):
    print("Вася")

# шаг 6
if a > 5 or (b == 7 and c == 7):
    print("Петя")