
from pathlib import Path

path= Path('pi_digits.txt')
contents = path.read_text()
'''эта команда удаляет последнюю пустую сстроку'''
contents=contents.rstrip()
print(contents)
#относительные и абсолютные пути к файлам
'''в относительном пути используется такая команда '''
path= Path('text_files/имя файла.txt')
'''абсолютнфе пути болле длинные ииза того что начинают с корнего каталога системы'''
path= Path('/home/eric/data_files/text_files/имя файла.txt')
'''используя абсолютный путь сможете читать файл из любого каталога вашей системы '''

#построчное считывание исп. для находки в документах определенные слова или тэги
from pathlib import Path
path=Path ('pi_digits.txt')
contents=path.read_text()
lines=contents.splitlines()
for line in lines:
    print(line)

#использовние имключений для для предотвращения аварийного завершения программы
