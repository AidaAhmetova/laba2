from datetime import datetime

def calculate_age():
    # Запрашиваем дату рождения у пользователя
    birth_date_str = input("Введите дату рождения в формате день/месяц/год: ")
    
    # Преобразуем введенную строку в объект datetime
    birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
    
    # Получаем текущую дату
    today = datetime.now()
    
    # Рассчитываем возраст
    age = today.year - birth_date.year
    
    # Проверяем, был ли день рождения в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    # Выводим результат
    print(f"Ваш возраст: {age} лет.")

# Вызов функции
calculate_age()