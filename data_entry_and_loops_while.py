#содержание подсказки
#promt = "if you share your name, we can personalize the messages you see"
#promt+= '\n what you name?'
#name = input(promt)
#print(f"\n hello,{name}!")


#исп. функции int() для получения числового ввода
# = input("how tall are you, in inchess?")
#god = int(god)
#if god >= 48:
  #  print("\n good")
#else:
   # print('\n entrance close!')

#оператор деления по модулю

#even_or_odd = input("enter a number, and I tell you if it even or odd:")
#even_or_odd=int(even_or_odd)
#if even_or_odd % 2 == 0:
 #   print(f"\nThe number {even_or_odd} is even.")
#else:
#    print(f"\nThe number {even_or_odd} is odd.")

#задачи 7.1-7.3
#cars = input('введите машину которую хотели бы взять на прокат!')
#print(f"Посмотрим смогу ли я найти вам {cars}")

#stol = input ('введите количество людей которое будет сидеть за столом!')
#stol =int(stol)
#if stol <= 8:
 #   print('есть свободный столик!')
#else:
 #   print('извините для такого количества людей столиков нет ')


#number = input("введите число а я скажу кратно ли оно 10 или нет")
#number =  int(number)
#if number %10 == 0:
 #   print('число введенное вами кратно 10')
#else:
 #   print('число введенное вами не кратно 10')

#циклы while() стр 154
#current_number= 1
#while current_number<= 5:
 ##  current_number+=1

#пользователь решает прервать работу программы
##prompt = "tell me something, and i will repeat back to you."
#prompt+="\n enter 'quit' to end program"
#messages = ""
#while messages!='quit':
 #   messages=input(prompt)
 #   #программа работает не плохо если не считать что 'quit' выводит как обычное сообщение if решит эту проблему
    #if messages!='quit':
 #   print(messages)

#флаги
#prompt = "tell me something, and i will repeat back to you."
#prompt+="\n enter 'quit' or 'stop' to end program"
#active= True
#while active:
 #   messages = input(prompt)
 #   if messages == 'quit':
  #      active=False
   # elif messages =='stop':
    #    active=False
    #else:
     #   print(messages)

# операторы break() и выход из цикла
#prompt = "please enter the name of a city you have visited:"
#prompt+="\n enter 'quit' to end program"
#while True:
   #city = input(prompt)
   #if city == 'quit':
  #  break
 #  else:
#     print(f"i like you see in {city.title()}! ")
#оператор continue() и продолжение цикла
#data = 0#пример как сделать список только из нечетных чисел
#while data <10:
 #   data +=1
  #  if data %2 ==0:
   #     continue
    #print(data)
#
#burger="давайте составим ваш личный бургер напишите какие начинки хотите увидеть"
#burger+="\n когда закончите с начинками напишите 'stop'"
#while True:
 #   nachinka= input(burger)
  #  if nachinka == 'stop':
   #     break
    #else:
     #   print(f'начинка добавлена{nachinka.title()}')

#закончил делать задание 7.5 на стр 160
#### перемещение циклов между списками
neprovereanae_polizovatel = ['alica','mike','nike']
provereanae_polizovatel= []
while neprovereanae_polizovatel:
    current_users= neprovereanae_polizovatel.pop()
    print(f"verifying user {current_users.title()}")
    provereanae_polizovatel.append(current_users)
print("\n the flowing users have been confirmed :")
for provereanae_polizovatel in provereanae_polizovatel:
    print(provereanae_polizovatel.title())


#удаление всех вхождений конкретного значения из списка
# remove() исп. для удаления конкретного значения из списка
pets = ['cat', 'dog','goldfish','cat','cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#заполнение словаря данными введеными пользователями
#acounts = {}
#polling_active = True
#while polling_active:
 #   name = input("\n What you name ? " )
  #  acount = input("\n which mountain would you like to climb someday? ")
   # acounts[name]= acount
    #repeat = input("would you like to let another person respond (yes \ no )")
    #if repeat == 'no':
     #   polling_active = False
    #print("\n --- poll results ---")
   # for name, acount in acounts.items():
    #    print(f"{name} would like to climb {acount}")