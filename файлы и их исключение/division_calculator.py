#from importlib.resources import contents

#print("give me two numbers, and i divide them.")
#print('enter "q" to quit')
#while True:
 #   first_number= input("\n first number:")
  #  if first_number =='q':
   #     break
    #second_number= input("\n second number: ")
    #if second_number =='q':
     #   break
    #answer = int (first_number) / int(second_number)
    #print(answer)

#Блок else более улучшанная часть прошлого кода
#print("give me two numbers, and i divide them.")
#print('enter "q" to quit')
#while True:
 #   first_number= input("\n first number:")
  #  if first_number =='q':
   #     break
    #second_number= input("\n second number: ")
    #if second_number =='q':
     #   break
    #try:
     #   answer = int (first_number) / int(second_number)
    #except ZeroDivisionError:
     #   print("you can't divide by 0!")
    #else:
     #   print(answer)

# обработка исключения FileNotFoundError
'''избежание ошибки что такого документа нет'''
#from pathlib import Path
#path = Path('alice.txt')
#try:
 #   contents= path.read_text(encoding='uf-8')
#except FileNotFoundError:
 #   print(f"Sorry, the filr {path} does not exist.")

#анализ текста
''''''
from  pathlib import Path
path = Path('alice.txt')
try:
    contents= path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the filr {path} does not exist.")
else:
    '''подсчет приблизительного строк в файле'''
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words")

    #остановился на стр 239 тема "функции ison.dumps()"