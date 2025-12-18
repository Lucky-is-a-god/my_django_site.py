#короткий пример как организовать обрботку специальных ситуаций с помощью опретора if
cars = ['audi', 'bmw','ford','omoda']
for car in cars:
    if car == 'omoda':
        print(car.upper())
    else:
        print(car.title())
#проверка условия двух чисел
#chislo = 25
#if chislo != int(input('введите число')):
   # print('число не правильное')
# что бы узнать состоит ли данное слово в списке
mashin = ['redbull','burn', 'volt']
if "volt" in mashin:
    print('hg')
else:
    print('no')
#проверка отсутствия в списке
user = ['nab','mer','ken']
ban = 'gfd'
if ban not in user:
    print(f'{ban.title()}, you can a response if you with')


# операторы if-else
age = 15
if age >= 18:
    print('you old')
else:
    print('sorry you yong')

#цепочки if-elif-else
vosrast = 8#int(input('введите свой возраст!'))
if vosrast <= 5:
    print('вход для дет. сада запрещен')
elif vosrast < 18:
# команды elif может быть бесконечное множество
    print('вы не совершенно летний вход запрещен!')
else:
    print('вы до росли входте!')
#эта цепочка не всегда требует что бы вы всегда заканчивали на else

#проверка нескольких условий на примере с пиццами
pizzas =['extra cheese', 'peperoni']
if 'student' in pizzas:
    print('adding student')
if 'extra cheese' in pizzas:
    print('adding extra cheese')
if 'peperoni' in pizzas:
    print('adding peperoni')
print('\nFished your pizza!')
# если бы исп. цепочку то код был бы выполнен не коректно так как обарвался сразу как нашел првый истенный результат


# представьте что в вашей компьютерной игре был подбит вражеский корабль
# и за подбитого корабля вам начислется 5 очков

alien_color= 'green'
if alien_color == 'green' :
    print('вы заработали 5 очков')
elif alien_color == "yellow":
    print('вы заработали 10 очков')
else:
    print('вы заработали 15 очков')

#напишите цепочку для определения возраста человека
rost = int(input('введите возраст'))
if rost < 2:
    print('младенец!')
elif rost <=2 or rost <4:
    print('пизд*к!')
elif rost <=4 or rost <13:
    print('головняк с учебой!')
elif rost <=13 or rost <20:
    print('долбо*б!')
elif rost<=20 or rost<65:
    print('начал любить ниву!')
else:
    print('пожилой человек!')


