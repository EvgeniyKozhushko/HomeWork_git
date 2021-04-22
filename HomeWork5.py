DATABASE = {
    'Anna': {'height': 160, 'weight': 50, 'sex': 'W'},
    'Michael': {'height': 180, 'weight': 100, 'sex': 'M'},
    'Conchita': {'height': 160, 'weight': 57, 'sex': 'W'},
    'Olga': {'height': 169, 'weight': 48, 'sex': 'W'},
    'Iren': {'height': 179, 'weight': 88, 'sex': 'W'},
    'Evgeniy': {'height': 175, 'weight': 59, 'sex': 'W'},
    'Nicola': {'height': 202, 'weight': 102, 'sex': 'W'},
    'Britney': {'height': 156, 'weight': 86, 'sex': 'W'},
    'Valentino': {'height': 188, 'weight': 90, 'sex': 'W'},
}

def show_menu():
    MENU = """
    1. List users (Press 1)
    2. View user info (height, weight, BMI) (Press 2)
    3. Change user data (Press 3)
    4. Create user (Press 4)
    5. Delete user (Press 5)
    6. Exit (Press 6)
    """
    print(MENU)
    return int(input("Your choise: "))

def list_users():
    print(', '.join(DATABASE.keys()))

def info_users():
    selected_user = DATABASE[str(input("Enter username: "))]
    w = float(selected_user.get('weight'))
    h = float(selected_user.get('height'))
    bmi = w / ((h/100)**2)
    bmi = round(bmi, 1)
    bmi_int = int(round(bmi,0))
    print('BMI user: ' + str(bmi))
    a = '='*(bmi_int - 20)
    b = '='*(60 - bmi_int)
    print('20' + str(a) + '|' + str(b)  + '60')

def read_users():
    change_user_date = {}
    change_user_name = input('Enter user name for change: ')
    change_user_height = int(input("Enter height, cm: "))
    change_user_weight = int(input("Enter weight, kg: "))
    change_user_date['height'] = change_user_height
    change_user_date['weight'] = change_user_weight
    DATABASE[change_user_name]= change_user_date
    print('User data changed')
    #print(change_user_name + str(DATABASE.get(change_user_name, )))


def create_users():
    new_user_date = {}
    user_name = input("Enter name: ")
    user_height = int(input("Enter height, cm: "))
    user_weight = int(input("Enter weight, kg: "))
    user_sex = input("Enter sex: ")
    
    new_user_date['height'] = user_height
    new_user_date['weight'] = user_weight
    new_user_date['sex'] = user_sex
    DATABASE[user_name] = new_user_date
    print('Date have been update')


def delete_users():
    delete_name = input("Enter the name of the user to be deleted: ")
    del DATABASE[delete_name]
    print('User deleted')

def exit_prog():
    import sys
    sys.exit()

ACTIONS = {
    1: list_users,
    2: info_users,
    3: read_users,
    4: create_users,
    5: delete_users,
    6: exit_prog,
}    

def select_action(answer: int):
    return ACTIONS.get(answer, show_menu)

def main():
    answer = 0
    while True:
        action = select_action(answer)
        answer = action()

main()        