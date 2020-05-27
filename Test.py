'''

def user_profiles(name, age, town):
    return (f'{name}, {age} год(а), проживающий в городе {town}')

name = input('name?: ')
age = int(input('Age?: '))
town = input('town?: ')

print(user_profiles(name, age, town))

'''
def biggest(a, b, c):
    if a < b and b > c:
        return b
    elif a < c and c > b:
        return c
    else:
        return a

print(biggest(12, 8, 61))

player_name = input('Введите имя игрока: ')
enemy_name = input('Введите имя противника: ')

player = {"name": player_name, "helth": 100, "damage": 50}
enemy = {"name": enemy_name, "helth": 100, "damage": 50}
print(player)
print(enemy)

def attack():
    person_1 = input(f'Кто ходит первым? {player_name} или {enemy_name}: ')
    if person_1 == player_name:
        enemy['helth'] == enemy['helth'] - player['damage']
    else:
        player['helth'] == player['helth'] - enemy['damage']
    return player, enemy

print(attack())
