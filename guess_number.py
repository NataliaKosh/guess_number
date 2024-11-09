# Импорт функции получения случайных чисел
# из модуля random.
from random import randint

# Получаем случайное число в диапазоне от 1 до 100.
number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    # Получаем число от пользователя и сохраняем его в переменную.
    lol = int(input('Введите число: '))
    
    # Если число меньше загаданного...
    if lol < number:
        # ...выводим сообщение.
        print('Ваше число меньше того, что загадано.')
    
    # Если число больше загаданного...
    if lol > number:
        # ...выводим сообщение.
        print('Ваше число больше того, что загадано.')
    
    # Если число угадано...
    if lol == number:
        # ...прерываем выполнение программы и...
        break
# ...выводим сообщение.
print('Отличная интуиция! Вы угадали число :)')