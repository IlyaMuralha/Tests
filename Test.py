import random

number = random.randint(1, 100)
print(number)

while True:
    user_number = int(input('your number: '))

    if user_number == number:
        print('you win!')
        break
    elif user_number > number:
        print('my number is smaller')
    else:
        print('my number is bigger')