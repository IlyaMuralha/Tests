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

user_number = None
while user_number != number:
    user_number = int(input('your number: '))

    if user_number > number:
        print('my number is smaller')
    elif user_number < number:
        print('my number is bigger')

print('you win!')
'''

#version_3
'''
import random
number = random.randint(1, 50)
print(number)

user_number = None
levels = {1: 3, 2: 5, 3: 10}
count = 0
level = int(input('Choose your level: '))
max_count = levels[level]

while number != user_number:
    count += 1
    if count > max_count:
        print('you lost')
        break

    user_number = int(input(f'attempt № {count}. Your number: '))

    if user_number > number:
        print('my number is smaller')
    elif user_number < number:
        print('my number is bigger')

else:
    print('you win!')
'''

#version_4

import random
number = random.randint(1, 50)
print(number)

user_number = None
levels = {1: 3, 2: 5, 3: 10}
count = 0
level = int(input('Choose your level: '))
max_count = levels[level]

user_count = int(input('Enter the number of users: '))
users = []

for i in range(user_count):
    users_name = input(f'enter username {i + 1}: ')
    users.append(users_name)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('you are lost')
        break
    for user in users:
        print(f'Move user {user}')
        user_number = int(input(f'attempt № {count}. Your number: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif user_number > number:
            print('my number is smaller')
        else:
            print('my number is bigger')

else:
    print(f'User {user} win!')