from importlib.resources import contents
from pathlib import Path
import json
username= input('введите свое имя ')
'''программа запрашивает имя пользователя чтобы сохранить его '''
path= Path('username.json')
'''далее собранные данные собираются и записываются в файл username.json'''
contents=json.dumps(username)
path.write_text(contents)
print(f"приветствуем тебя, {username}!")
'''далее выводится сообщение что имя было сохранено '''


#теперь программа приветствовает пользователя имя которого уже было сохранено
from pathlib import Path
import json
path= Path('username.json')
'''считываем содержимое файла'''
contents=path.read_text()
username =json.loads(contents)
'''а затем с помощью функции json.loads присваиваеи извлечённые данные переменной username'''
print(f"welcome back, {username}")
#мы исп. метод path.exists чтобы узнать сохранено ли имя пользователя
from pathlib import Path
import json
path = Path('username.json')
if path.exists():
    contents= path.read_text()
    username= json.loads(contents)
    print(f"Welcome back, {username}")
else:
    username= input('What is your name ?')
    contents= json.dumps(username)
    path.write_text(contents)
    print(f" We remember you you come back {username}!")
# рефакторинг разбиваем код на более маленькие функции изза этого код становиттся чище
from pathlib import Path
import json
def greet_user():
    '''приветствовать пользователя по имени '''
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username= json.loads(contents)
        print(f"welcome back, {username}!")
    else:
        username = input('как тебя зовут?')
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We remember you when come back, {username}!")
greet_user()
# теперь мы эту функцию пеработаем чтобы она не решала столько разных задач
#начнем с перемещении кода загрузки хранимого имени пользователя в отдельную функцию
from pathlib import Path
import  json
def get_stored_username(path):
    '''получает хранимое имя пользоваетля если оно существует '''
    if path.exists():
        contents= path.read_text()
        username= json.loads(contents)
        return username
    else:
        return None
def greet_user():
    '''приветствовать пользователя по имени'''
    path=Path('username.json')
    username=get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username=input(" what you name")
        contents= json.dumps(username)
        path.write_text(contents)
        print(f"We remember you when you come back {username}!")
greet_user()
