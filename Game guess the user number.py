import random

min_number = 1
max_number = 100
ansver = ['Может эта.', 'А если так.', 'Ну а вдруг.', 'Ну чем черт не шутит.', 'Да блин.']
input('Загадайте число от 1 до 100. Нажмите "Enter"')


while True:
    number = random.randint(min_number, max_number)
    print(f'Ваше число: {number}')
    symbol = input('Ваше число больше ">", меньше "<" или равно "="? Введите один из трех символов: ')
    if symbol == '=':
        print('Я выиграл!')
        break
    elif symbol == '>':
        min_number = number + 1
        print(f'{random.choice(ansver)} ')
    elif symbol == '<':
        max_number = number - 1
        print(f'{random.choice(ansver)}')
    else:
        input('Вы ввели неправильный символ. Готовы продолжить? Нажмите "Enter"')
