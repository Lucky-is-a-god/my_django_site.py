#передача данных функции
#def greet_user(username):
  #  '''выводит простое приветсвование'''
  #  print(f"Hello, {username.title()}")
#greet_user(str(input('введите имя')))
from working_with_dictionaries import full_name


# задание 8.1 и 8.2
def display_message():
    '''выводит сообщение'''
    print('Сегодня разберем функции ')
display_message()

def favorite_book(book):
    print(f"одга из моих любимых книг - '{book.title()}'")
favorite_book('алиса в стране чудес')
#позиционные аргументы
def animal(typ_animal,home, name_animal):
    print(f"у меня дома {typ_animal.title()}")
    print(f"мою {home.title()}, ее зовут {name_animal.title()}!")
animal("собака","собаку","тимоша")
#многократные вызовы функций
def animal(typ_animal,home, name_animal):
    print(f"у меня дома {typ_animal.title()}")
    print(f"мою {home.title()},  зовут {name_animal.title()}!")
animal("собака","собаку","тимоша")
animal('кошка','кошку','рыжик' )

#именнованые аргументы ее удобством в том что мы сразу пишем название определенного аргумента
def animal(typ_animal,home, name_animal):
    print(f"у меня дома {typ_animal.title()}")
    print(f"мою {home.title()},   зовут {name_animal.title()}!")
animal(typ_animal='кошка',home='кошку',name_animal='рыжик')
# значение по умолчанию удобно тем что назначаем сразу пару аргумента при упоминании его он сразу будет нести его значение
def animal(typ_animal,home , name_animal="тимоша" ):
    print(f"у меня дома {typ_animal.title()}")
    print(f"мою {home.title()},   зовут {name_animal.title()}!")
animal(typ_animal="собака", home ='собаку' )
'''если вы используете значение по умолчанию то оно должно быть крайним'''
#задание 8.3, 8.4 и 8.5
def make_shirt (nadpus,size  ):
    print(f"ваша футболка размером {size} и с надписью '{nadpus.title()}'")
make_shirt('momente more', 46)
make_shirt('я люблю python','L')

def describe(city, country = 'Россия'):
    print(f"{city.title()} находтся в {country.title()}")
describe('domodedovo')
# возращение простого значения
def  get_formated_name (first_name, last_name):
    '''возвращает отформатированное полное имя '''
    full_name= f"{first_name} {last_name}"
    return full_name.title()
musician = get_formated_name('liza','milyokhina')
print(musician)
# необязательные аргументы
def family (first_name,last_name,midle_name=""):
    '''возвращает полное отформатированое имя'''
    if midle_name:
        full_name= f"{first_name} {midle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()
hot = family('liza' , 'milyokhina')
print(hot)
hot = family('liza','milyokhina','vasylievna')
print(hot)
#закончил на 175 стр
#возвращение словаря
def build_person (first_name, last_name):
    """возвращает словарь с информацией о человеке"""
    person= {'first': first_name, "last": last_name}
    return person
musician = build_person ('jimi','hendrix')
print(musician)


#def get_formated_name(first_name, last_name):
 #   full_name = f'{first_name} {last_name}'
  #  return full_name.title()


#while True:
 #   print('\nPlease tell me your name:')
  #  print('enter "q" to quit')
   # f_name = input('First name: ')
    #if f_name.lower() == 'q':
     #   break
   # l_name = input('Last name: ')
    #if l_name.lower() == 'q':
     #   break

   # formatted_name = get_formated_name(f_name, l_name)
    #print(f'\nHello {formatted_name}!')




#передача списка
def new_user(names):
    '''выводим простое приветствие для каждого пользователя.'''
    for name in names:
        messages = f"hello new users :{name.title()}"
        print(messages)
user_name= ['nike','mike']
new_user(user_name)

# передачча произвольного набор аргументов

def make_pizza(*topping):
    '''выводим список заказаных начинок.'''
    print(topping)
make_pizza('peproni')
make_pizza('student','chees','green peppers')

#тепрь функцию print() можно заменить циклом

def make_pizza(*nacinka):
    '''выводим состав начинки'''
    print("\n вы выбрали пиццу со вкусом:")

    for toppings in nacinka:

        print(f" - {toppings}")

make_pizza(input("введите начинку которую хотите "))
make_pizza('extra cheasse','gren peper','student')

