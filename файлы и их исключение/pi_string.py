#работа с содержимым файла
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

pi_string = ''
for line in lines:
    if line.strip():  # Пропускаем пустые строки
        pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#более простой код

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

pi_string = ''
for line in contents.splitlines():
    if line.strip():  # Пропускаем пустые строки
        pi_string += line.strip()

print(pi_string)
print(len(pi_string))