class Dog:
    '''простая модель собаки '''
    def __init__(self,name,age):
        '''Иниацилизирует атрибуты name и age'''
        self.name = name
        self.age= age
    def sit(self):
        '''иммитируем как собака садится по комманде'''
        print(f"{self.name} is now sitting.")
    def roll(self):
        '''иммитируем то как собака делает переворот по команде'''
        print(f"{self.name} rolled over")


#создание экземпляра класса
#class dog:
 #   my_dog=Dog(name=input('введите имя своей собаки'),age=(int(input('введите возраст вашей собаки'))))
  #  print(f"Мою собаку зовут {my_dog.name} ")
   # print(f"возраст моей собаки {my_dog.age}")

#вызов методоов
#class dog:
 #   my_dog = Dog(name=input('введите имя своей собаки'), age=(int(input('введите возраст вашей собаки'))))
  #  my_dog.sit()
   # my_dog.roll()

#создание нескольких экземпляров

class Dog:
    my_dog=Dog('Тимоша',12)
    your_dog=Dog('Шарик',2)
    print(f"мою собаку зовут {my_dog.name}")
    print(f"она с нами уже{my_dog.age}")
    my_dog.sit()
    print(f"\n ее собаку зовут {your_dog.name}")
    print(f"наши собаки дружат {your_dog.age} уже года")
    your_dog.sit()


class restourant:
    '''создали класс ресторана в котром будет его название и тип кухни'''
    def __init__(self,name,type):
        self.name= name
        self.type= type
    def open(self):
        print(f"{self.name} открывается с 09:00")


class restourant:
    my_restoran=restourant('кишмиш','Russia')
    your_restoran= restourant('джим-бим','Japan')
    print(f"{my_restoran.name} очень хорошее заведение с {my_restoran.type} типом кухни")
    my_restoran.open()
    print(f"лучший ресторан с {your_restoran.type} кухней  и не обычным названием {your_restoran.name}")
    your_restoran.open()

#выводит рандомное значение из представленных значений
from random import choice
players=['f','g','a','s']


first_up=choice(players)
print(first_up)

from  random import randint
result=randint(1,6)
print(result)