string = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"

count = len(string) # шаг 1
invert = string[::-1] # шаг 2
# шаг 3 в строке 13
# шаг 4 в строке 14
count_nd = string.count("нд")
count_am = string.count("ам")
count_o = string.count("о") # шаг 5
#  шаг 6 в строке 16
print("Шаг 1 - Количество символов - " + str(count))
print("Шаг 2 - " + str(invert))
print("Шаг 3 - " + string.title())
print("Шаг 4 - " + string.lower())
print(f'Шаг 5 - Количество вхождений "нд" - {str(count_nd)}\nШаг 5 - Количество вхождений "ам" -  {str(count_am)}\nШаг 5 - Количество вхождений "о" -  {str(count_o)}')
print("Шаг 6 - " + string.upper())
print("Шаг 7 - " + string)