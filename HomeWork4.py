user = input('Введите имя пользователя ') # для указания суммы нужно ввести - Admin

def check(func):
    def check_user(*args, **kwargs):
        if args[0] != 'Admin':
            return 'Доступ запрещен!'
        value = func(*args, **kwargs)
        return value
    return check_user

@check
def my_money(lst):
    return '1000 BYN'

#my_money = check(my_money)

print(my_money(user))