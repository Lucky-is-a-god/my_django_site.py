#вызов функции сигнализируя о том что данная метод был вызван
class User:
    login='user_login'
    role='Python Develoeper'
    '''объявление метода'''
    def demo_method_print(self):
        print('Method call')
u1=User()
print(u1)
u1.demo_method_print()
'''таким образом через аргумент self мы можем получить 
атрибуты этого экземпляра класса и работать с ним'''
class User:
    login='user_login'
    role='Python Developer'
    def demo_method_print(self):
        print(f'Method call by {self}')
    def show_attrs(self):
        print(f'Login:{self.login}, role:{self.role}')
u1=User()
u1.show_attrs()
'''стоит обратить внимание что приведеный в ввыше наш объект
u1 хранит ссылку на атрибут класса если же мы 
зададим конкретные локальные свойства этому объекту
то выводится будут именно они'''
class User:
    login='user_login'
    role='Python Developer'
    def demo_method_print(self):
        print(f'Method call by {self}')
    def show_attrs(self):
        print(f'Login:{self.login}, role:{self.role}')
u1=User()
u1.login='Gridin'
u1.role='Techlead'
u1.show_attrs()
'''теперь давайте расширим функционал нашего класса
например добавим возможность изменять имя и специализацию объекта
при помощи методов set_name и set_specialization, избавившись
при этом от демонстрационного метода demo_method_print'''
class User:
    login= 'user_login'
    role= 'Python Developer'
    def set_login(self,login):
        self.login=login
    def set_role(self, role):
        self.role= role
    def show_attrs(self):
        print(f'Login:{self.login}, role:{self.role}')
u1=User()
u1.set_login('Gridin')
u1.set_role('TechLead1')
u1.show_attrs()
'''отличие от примера сверху что многие наши атрибуты
будут сокрыты для доступа вне класса,когда мы подробнее познакомимся
с инскапсуляцией и будем ее импользовать '''
#Реализуем прототип приложения. Часть 1
'''начнем с класса User. Внутри него реализуем два метода
один для установки всех необходимых локальных атрибутов экземплярра класса 
а другой для добавления задач в проекте'''
class User:
    def set_attrs(self,login,password,name,email,role):
        self.login=login
        self.password=password
        self.name=name
        self.email=email
        self.role=role
    def create_task(self,project,description):
        project.add_task(self,description)
        '''здесь методом set_attrs() мы осуществляем установки
заданных локальных атрибутов(он является вспомогательным методом для работы класса
и поэтому не отображается на диаграмме'''
'''В методе create_task() принимаются аргументы project — ссылка на экземпляр класса Project (который мы пока не реализовали) и description — строка, описание задания.
Далее мы будем вызывать у экземпляра класса Project метод add_task() и передавать ему self — ссылку на пользователя, который добавил задачу, и само описание задачи.'''
#также давайте добавим метод show_members, благодаря которому
#будет осуществляется вывод на экран состоящих в команде - значение их
#атрибутов login и name а так же вспомогательный метод get_team_size,
#который будет возвращать кол=во участников в команде
class Team:
    def init_team(self,name,members=[]):
        self.name=name
        self.members=members
    def add_member(self,user):
        self.members.append(user)
    def show_members(self):
        print(f'Team {self.name} members:')
        for i, user in enumerate(self.members):
            print(f'№{i +1}, login: {user.login}, name: {user.name}')
    def get_team_size(self):
        return len(self.members)
user1= User()
user1.set_attrs('user1', 'password1', 'John Doe','pol@ya.ri', 'Python Developer')
user2 = User()
user2.set_attrs('user2', 'password2', 'Jone Dae', 'POL@gm.yu', 'Python Developer')
user3=User()
user3.set_attrs('user3', 'password3', 'Bob Smith', 'Liza@ko.po', 'Python Developer')
team=Team()
team.init_team('my_team')
team.add_member(user1)
team.add_member(user2)
team.add_member(user3)
print(f'Size of team "{team.name}" : {team.get_team_size()}')
team.show_members()
'''с задачей все просто. Объекты класса Task будут 
содержать описание, которое будет задаваться при помощи метода 
create_task()'''
class Task:
    def create_task(self,description):
        self.description =description

'''Переходим к классу Project. Он должен содержать атрибуты name — название
 проекта, team — ссылку на команду, которая его выполняет, и атрибут tasks — изначально
  пустой список, который далее будет хранить все текущие задачи. Атрибуты будут устанавливаться методом create_project().

Метод add_task() необходим для добавления задачи (и ее создания внутри этого метода) в проект, при этом метод будет 
проверять, состоит ли пользователь, который хочет добавить задачу, в команде, которая выполняет проект (вспомните метод 
create_task() в классе Team, из него мы и будем вызывать метод add_task() у экземпляра класса Project.'''
class Project:
    def create_project(self,name,team):
        self.name=name
        self.team=team
        self.task=[]
    def add_task(self,user,description):
        if user in self.team.members:
            task=Task()
            task.create_task(description)
            self.task.append(task)
            print(f'Task "{description}" addded to project "{self.name}"')
        else:
            print(f"User '{user.name}' is not a member of the team working on project'{self.name}' ")



#И полная цепочка взаимодействия выглядит так
user1= User()
user1.set_attrs('Johnd', 'mloz512qyt', 'john Doe', 'hon@po.yu', 'TechLead')
user2 = User()
user2.set_attrs('Janed', 'qw1lbz','Jane Guf', 'kol@go.lo', 'Python Developer')
user3=User()
user3.set_attrs('LizaM','lok456po', 'Liza Milyahina','mi@pol.fm', 'Python Developer')
team = Team()
team.init_team('Research Group')
team.add_member(user1)
team.add_member(user2)
team.show_members()
project=Project()
project.create_project("UAV Detectron", team)

user1.create_task(project, 'Find best model')
user2.create_task(project, 'Setup Environment')
user3.create_task(project, 'Optimization')
'''таким образом мы и реализовали диаграмму, объявленную в самом начале:
определили все 4 класса с их сопутствующими атрибутами а так же установили отношения:
  1- команда состоит из пользователч
  2- команды работают над проектами 
  3- проект состоит из задач 
  4- пользователь состоящий в команде может добавлять задачи в проект '''
