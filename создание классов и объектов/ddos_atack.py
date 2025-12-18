from классы.dog import result


class User:
    login = 'user_login'
    role= 'Python Developer'

u1 = User()
u2 =User()
print(u1.login, u1.role)
print(u2.login, u2.role)
print(id(u1), id(u2))
#пространство имен класса
class User:
    login = 'user_login'
    role= 'Python Developer'

u1 = User()
u2 =User()
print(u1.login, u1.role)
print(u2.login, u2.role)
User.login = 'form_login'
User.role='Designer'
print(u1.login, u1.role)
print(u2.login, u2.role)

# пример разницы атрибутов класса и атрибуты экземпляра
class User:
    login = 'user_login'
    role = 'Python Developer'
u1 = User()
u2= User()
print(u1.login, u1.role)
print(u2.login, u2.role)


User.login = 'from_login'
User.role='Designer'

print(u1.login, u1.role)
print(u2.login, u2.role)

#теперь перейдём к атрибутам экземпляров классов -
#локальным атрибутаам \

class User:
    login = 'user_login'
    role = 'Python Developer'

u1= User()
u2 = User()
print(u1.login, u1.role)
print(u2.login, u2.role)


u1.login='polyakov.n1kitushcka@yandex.ru'
u1.role= 'Python rasrabotchik'
print(u1.login, u1.role)
print(u2.login, u2.role)
print(u1.__dict__,u2.__dict__)
'''команда __dict__ вызывает содержимое словаря как видно ввыше'''
#остановился добавление новых атрибуттов класса
'''избежание ошибки Attributeerror'''
class User:
    login= 'user_login'
    role='Python Develorer'
print(getattr(User,'email', False))
#удаление атрибуттов класса
#важно поле удаления атрибута проверять его наличие функцией
#hasattr() которая которая принимает в себя имя класса или объекта и его атрибута
class  User:
    login= 'user_login'
    role= 'Pythone Developer'
User.email= 'polyakov.n1kitushcka@yandex.ru'
print(hasattr(User,'email'))
del User.email
print(hasattr(User,'email'))
#так жеможно удалять атрибут при помощи delattr()
class  User:
    login= 'user_login'
    role= 'Pythone Developer'
User.email= 'polyakov.n1kitushcka@yandex.ru'
print(hasattr(User,'email'))
delattr(User,'email')
print(hasattr(User,'email'))
'''разниц между hasattr() and getattr()
hasattr() выводит либо правда или ложь, а 
getattr() либо значения атрибута если она существует 
либо значение третьего параметрапереданного ей, если не существует'''
#класс как тип данных. объектная модель Python
class User:
    login= 'user_login'
    role= 'Python Developer'
u1= User()
print(type(u1)==User)
print(isinstance(u1,User))
'''функция вернет True если проверяемый объект является экземпляром указанного класса'''
#При разработке платформы онлайн-школы вам поручили реализовать класс Student c атрибутом course. Значение атрибута — "Data Science".
#После объявления класса создайте экземпляр класса s1 и добавьте ему локальные атрибуты:

#name со значением "Иван";
#surname со значением "Иванов";
#semester со значением 1.
#Запишите в переменную result локальные атрибуты
#(как служебные, так и пользовательские) экземпляра s1 в виде
#словаря.
class Student:
    course='Data Science'
s1=Student()
s1.name='Иван'
s1.surname='Иванов'
s1.semester=1

result=vars(s1)