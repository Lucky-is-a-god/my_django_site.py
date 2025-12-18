#в этом юните узнаем как качественно реализовать
#подробно рассмотрим метод __init__
class User:
    def __init__(self,login, password, name, email,role):
        self.login= login
        self.password=password
        self.email=email
        self.name=name
        self.role=role
    def create_task(self, project, description):
        project.add_task(self,description)
user1= User('JohnD', 'gh34392b', 'Jphn Doe', 'eojfekfj@jsj.ru', 'python')
print(user1.__dict__)
#user1= User('nike','ofdkfjkf', 'mike')
#print(user1.__dict__)
'''если мы будем заполнять не полностью то выйдет ошбика
в том случае если мы сразу введем этому аргументу какое либо значение
пример снизу'''

class User:
    def __init__(self, login, name, password, role=None, email=None):
        self.login=login
        self.role=role
        self.name=name
        self.password=password
        self.email=email
    def create_task(self, project, description):
        project.add_task(description)
user1= User('kill', 'mikimaus', 'qwer43')
print(user1.__dict__)
'''теперь наша программа работает без ошибок. при этом в инициализаторе 
мы можем создавать не только те аргументы которые были переданы значения
например добавим атрибут Location'''
class User:
    def __init__(self, login, name, password, role=None, email=None):
        self.login=login
        self.role=role
        self.name=name
        self.password=password
        self.email=email
        self.location='moscow'
    def create_task(self, project, description):
        project.add_task(description)
user1= User('kill', 'mikimaus', 'qwer43')
print(user1.__dict__)
#теперь сделаем прототип приложения часть 2
class User:
    def __init__(self,login, name, password, email,role ):
        self.role= role
        self.name=name
        self.login=login
        self.password=password
        self.email=email
    def create_task(self,project, description):
        project.add_task(self, description)
class Team:
    def __init__(self, name, member=[]):
        self.name=name
        self.member=member
    def add_member(self,user):
        self.member.append(user)
    def show_member(self):
        print(f'Team {self.name} member:')
        for i, user in enumerate(self.member):
            print(f'№{i + 1}, login:{user.login}, name:{self.name}')
    def get_team_size(self):
        return len(self.member)
class Task:
    def __init__(self,description):
        self.description= description
class Project:
    def __init__(self, name, team):
        self.name=name
        self.team=team
        self.tasks=[]
    def add_task(self, user, description):
        if user in self.team.members:
            task= Task(description)
            self.tasks.append(task)
            print(f"'{description}' added to project '{self.name}'")
        else:
            print(f"Task'{user.name}' is not a member of the tem working on project'{self.name}'")


user1=User('Johnd', 'mloz512qyt', 'john Doe', 'hon@po.yu', 'TechLead')
user2 = User('Janed', 'qw1lbz','Jane Guf', 'kol@go.lo', 'Python Developer')
user3=User('LizaM','lok456po', 'Liza Milyahina','mi@pol.fm', 'Python Developer')
team = Team('Research Group')
team.add_member(user1)
team.add_member(user2)

project=Project("UAV Detectron", team)

user1.create_task(project, 'Find best model')
user2.create_task(project, 'Setup Environment')
user3.create_task(project, 'Optimization')