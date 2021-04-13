w = float(input("Введите вес, кг "))
h = float(input("Введите рост, см "))
sex = input("Введите пол, М или Ж ")

bmi = w / ((h/100)**2)
bmi = round(bmi, 1)
bmi_int = int(round(bmi,0))
print('Ваш индекс массы тела: ' + str(bmi))

if sex == "М":
    if bmi <= 16:
        print ('Выраженный дефицит массы тела')
    elif bmi > 16 and bmi <= 18.5:
        print ('Недостаточная масса тела (дефицит)')
    elif bmi > 18.5 and bmi <= 24:
        print ('Нормальная масса тела')
    elif bmi > 24 and bmi <= 30:
        print ('Избыточная масса тела (предожирение)')
    elif bmi > 30 and bmi <= 35:
        print ('Ожирение I степени')
    elif bmi > 35 and bmi <= 40:
        print ('Ожирение II степени')
    elif bmi > 40:
        print ('Ожирение III степени')   

elif sex == "Ж":
    if bmi <= 15:
        print ('Выраженный дефицит массы тела')
    elif bmi > 15 and bmi <= 17.5:
        print ('Недостаточная масса тела (дефицит)')
    elif bmi > 17.5 and bmi <= 23:
        print ('Нормальная масса тела')
    elif bmi > 23 and bmi <= 29:
        print ('Избыточная масса тела (предожирение)')
    elif bmi > 29 and bmi <= 34:
        print ('Ожирение I степени')
    elif bmi > 34 and bmi <= 39:
        print ('Ожирение II степени')
    elif bmi > 39:
        print ('Ожирение III степени')   

else:
    print("Неверно введен пол")

a = '='*(bmi_int - 20)
b = '='*(60 - bmi_int)
print('20' + str(a) + '|' + str(b)  + '60')