from list_and_how_to_work_with_them import names


class car:
    def __init__(self, make,model,year):
        '''атрибуты описания автомобиля'''
        self.make=make
        self.model=model
        self.year=year
    def polnoe_name(self):
        '''возвращение отфоррматированного описания '''
        long_name=f"{self.make} {self.model} {self.year}"
        return long_name.title()
my_new_car=car('fision','ford','2008')
print(f"я сегодня купил себе машину {my_new_car.polnoe_name()}")
# назначение атрибуту значение по умолчанию(в данном примере сделаем пробег для машин)
class car:
    def __init__(self, make, model, year, odometr_reading=0):  # Добавляем значение по умолчанию
        '''атрибуты описания автомобиля'''
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = odometr_reading

    def polnoe_name(self):
        '''возвращение отфоррматированного описания '''
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometr(self):
        '''выводит данные о пробеге машины в милях'''
        print(f"this car has {self.odometr_reading} km on it")


# Эти строки должны быть вне класса
my_new_car = car('fision', 'ford', '2008')  # Теперь работает, так как odometr_reading имеет значение по умолчанию
print(f"я сегодня купил себе машину {my_new_car.polnoe_name()}")
my_new_car.read_odometr()
# создание генератора случайных чисел
#from random import randint

#result = randint(1,6)
#print(result)
#создание генератора который в случайном порядке выбирает имя

#from random import choice
#players=['red','blow','yellow']
#first_up=choice(players)

