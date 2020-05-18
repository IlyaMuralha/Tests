#version_1
'''
import random
number = random.randint(1, 100)
#print(number)

while True:
    user_number = int(input('your number: '))

    if user_number == number:
        print('you win!')
        break
    elif user_number > number:
        print('my number is smaller')
    else:
        print('my number is bigger')
'''

#version_2
'''
import random
number = random.randint(1, 100)
print(number)

#user_number = None
while user_number != number:
    user_number = int(input('your number: '))

    if user_number > number:
        print('my number is smaller')
    elif user_number < number:
        print('my number is bigger')

print('you win!')
'''

#version_3

import random
number = random.randint(1, 100)
print(number)

user_number = None
count = 0

while number != user_number:
    count += 1
    print(f'Try № {count}')

    user_number = int(input('your number: '))

    if user_number > number:
        print('my number is smaller')
    elif user_number < number:
        print('my number is bigger')

print('you win!')