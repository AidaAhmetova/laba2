import random

def find_multiples_of_x():
    # Генерируем случайный список чисел от 0 до 200 размером 10
    numbers = [random.randint(0, 200) for _ in range(10)]
    print(f"Сгенерированные числа: {numbers}")

    # Запрос пользователя для ввода цифры X
    x = int(input("Введите число X: "))

    # Используем лямбда-функцию для поиска чисел, кратных X
    multiples_of_x = list(filter(lambda num: num % x == 0, numbers))

    # Выводим результат
    print(f"Числа, кратные {x}: {multiples_of_x}")

# Вызов функции
find_multiples_of_x()