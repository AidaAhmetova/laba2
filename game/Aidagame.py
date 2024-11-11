import random

def get_user_choice():
    user_input = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    while user_input not in ['камень', 'ножницы', 'бумага']:
        print("Неверный ввод. Пожалуйста, выберите камень, ножницы или бумагу.")
        user_input = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    return user_input

def get_computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return "Вы победили!"
    else:
        return "Компьютер победил!"

def play_game():
    print("Добро пожаловать в игру 'Камень-ножницы-бумага'!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Запуск игры
play_game()