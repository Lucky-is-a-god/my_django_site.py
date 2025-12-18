from importlib.resources import contents
from pathlib import Path
path= Path('programming.txt')
path.write_text('I love programming, I love Elizaveta')
#запись нескольких строк
from pathlib import Path
contents='I love\n'
contents+='liza\n'
contents+='Milyohina'

path = Path('programming.txt')
path.write_text(contents)
'''при этом вторая команда игнорирует первую
то есть в итоге первой команды нет в документе'''

from pathlib import Path
contents=(str(input('введите свое имя! \n')))
contents+=f"  Hello new players {contents.title()}"
path= Path('guest.txt')
path.write_text(contents)

