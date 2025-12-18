#просто словарь
alien_0 = {'color' : 'red', 'points': 5 }
print(alien_0['color'])
print(alien_0['points'])
# обращение к значениям в словаре
prishelec = {'color': 'blue', 'points': 10}
new_points= prishelec['points']
print(f'you just earned {new_points} points')


#добавление новых пар "ключ - значений"
ali = {'colorr' : 'yellow', 'points' : 15}
print(ali)
ali['x_position'] = 0
ali['y_position']=25
print(ali)



#создание пустого словаря
pol ={}
pol['color']='green'
pol['points']=45
print(pol)
#обычно его исп. при хранении данных введеных пользователем или написании кода автомотически генерирующих значений


#изменений значений в словаре
kol = {'color': 'green'}
print(f'the alien is{kol["color"]}')
kol['color']='yellow'
print(f'the alien is now {kol["color"]}.')



#отслеживание позиции пришельца с разной скоростью передвижения

vol = {'x_position':0, 'y_position':25, 'speed': 'slow'}
print(f"original position{vol['x_position']}")
if vol['speed'] == 'slow':
    x_increment = 1
elif vol['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
vol['x_position']= vol['x_position'] + x_increment
print(f'new position {vol["x_position"]}')


#удаление ключ пары
rol = {'color': 'red', 'speed':4}
print(rol)
del rol['speed']
print(rol)
#удаление пары "ключ-значения"отменить уже не удастся

#словарь с одно типном объктами

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edvard' : 'rust',
    'phil' : 'python',
}
language = favorite_languages['jen'].title()
print(f"Sarah's favorite language is {language}")

#обращение к значению методом get()

zebra = {'color' : 'black', 'ves' : 154}
point_value= zebra.get('points','no point value assigned')
print(point_value)

chisla = {
    'Liza': '45',
    'Vadim': '13',
    'sergey': '89',
    'Nikita' : '10',
}
ugadai= chisla['Nikita'].title()
print(f"you loved nomber {ugadai}")

#перебор всех пар значений ключ значений

user_0= {
    'user_name': 'nik',
    'first': 'jek',
    'last': 'ken',
    }
for key, value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")

# перебор всех ключей в словаре
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edvard' : 'rust',
    'phil' : 'python',
    }
for name, love in favorite_languages.items():
    print(f"{name.title()} love language {love.title()}.")

#перебор ключей в определеном порядке
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edvard' : 'rust',
    'phil' : 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f" {name.title()} parol.")

reki = {
    'nile': 'egipet',
    'oka': 'mos.obl',
    'evs': 'voronesh',
}
for far,vodoem in reki.items():
    print(f"{far}, protekaet in {vodoem}")

# список словарей
spisok_0 = {'color': 'green', 'points': 25}
spisok_1 = {'color': 'red', 'pointd': 15}
spisok_2 = { 'color': 'black', 'points': 18}
spisoks = [spisok_0,spisok_1,spisok_2]
for spisok in spisoks:
    print(spisok)


#генерируем 30 новых пришельцев

oil = []
for oil_numbers in range(30):
    new_oil ={'color': 'red', 'points': 12, 'speed': 'meed'}
    oil.append(new_oil)
for oils in oil [:5]:
    print(oils)
print('...')


#как работать с таким множеством? представим что некоторый меняют цвет и двиг. быстрее

oil = []
for oil_numbers in range(30):
    new_oil ={'color': 'red', 'points': 12, 'speed': 'meed'}
    oil.append(new_oil)
for oils in oil [:15]:
    if oils ['color']== 'red':
        oils ['color'] = 'yelow'
        oils ['speed'] = 'slow'
        oils ['points'] = 10
    #так же можно добавить и других пришельцев через команду elif (пример на 143 стр.)

for oils in oil [:20]:
    print(oils)
print('...')


#список в словаре
love_laguage = {
    'krt': ['python', 'cc+'],
    'bin': ['ui', 'mk'],
    'juy': ['kj','ji'],
}
for name, langage in love_laguage.items():
    print(f'\n {name.title()} favorite languages are ')
    for languagess in langage:
        print(f'\t {languagess.title()}')

# вложение словарей
people = {
    'polizovatel_1': {
        'first': "mike",
        'last': "lover",
        'location' :"moscow",
    },
    'polizovatel_2':{
        'first' :"nike",
        'last': "dead",
        'location': "domodedovo",
    },
}
for people_name, people_info in people.items():
    print(f'\n username:{people_name}')
    full_name = f"{people_info['first']} {people_info['last']}"
    location = people_info['location']
    print(f"\t Full name: {full_name.title()}")
    print(f"\t Location: {location.title()}")