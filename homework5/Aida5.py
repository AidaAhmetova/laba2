def get_number():
    for number in range(30):
        if number % 2 != 0:  # Проверяем, является ли число нечетным
            yield number  # Возвращаем нечетное число

# Создаем генератор
odd_numbers = get_number()

# Находим и выводим первое, пятое и последнее нечетные числа
first_odd = None
fifth_odd = None
last_odd = None

# Используем цикл for для итерации по генератору
for i, value in enumerate(odd_numbers):
    if i == 0:
        first_odd = value
    if i == 4:
        fifth_odd = value
    last_odd = value  # последнее число будет всегда обновляться на каждом шаге

# Выводим результаты
print(f"Первое нечетное число: {first_odd}")
print(f"Пятое нечетное число: {fifth_odd}")
print(f"Последнее нечетное число: {last_odd}")