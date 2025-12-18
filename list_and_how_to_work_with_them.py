g = ['hi', 'theb','with']
print(g)
#получем ответ не обработаный вышло: ['hi', 'theb', 'with']
names = ['nikita', 'liza', 'natali', 'sergey', 'nastya']
print(names[3])
#получаем более аккуратный и конкретный результат вышло: sergey
names = ['nikita', 'liza', 'natali', 'sergey', 'nastya']
print(names[3]. title())
#выводит такой же результат только с большой буквы
names = ['nikita', 'liza', 'natali', 'sergey', 'nastya']
print(names[-1])
#таким способом выводится последний элемент в списке вышло: nastya




#отдельные значения из списка исп. также, например с помощью строки f"" пример:
names = ['nikita', 'liza', 'natali', 'sergey', 'nastya']
history = f"мою младшую сестру зовут, {names[-1].title()}."
#обязательно не забывать указывать квадратные скобки
print(history)

# дальше расмотрим удаление и добавление разных объектов в список
#сейчас пример изменения имени в списке
names = ['nikita', 'liza', 'natali', 'sergey', 'nastya']

names[0] = 'timosha'
print(names)
#сейчас расмотрим добавление нового слова в список
names = ['nikita', 'liza', 'natali', 'sergey', 'nastya']
names.append('timosha')
print(names)
#снизу пример добавления нового имени в список
#names =[]
#names.append(input('введите имя'))
#print(names)
#вставка в список пример
magazin = ['lenta', 'dicsi','4 lap']
magazin.insert(2, 'casher')
print(magazin)
#теперь расмотрим удаление из списка
magazin = ['lenta', 'dicsi','4 lap']
del magazin[0]
print(magazin)
#удаление предмета при помощи pop()
magazin = ['lenta', 'dicsi','4 lap'] #1
popped_magazin = magazin.pop(1)#2
print(magazin)#3
print(popped_magazin)#4
#разбор: сначала определяется и выводится что было (1), затем значение вывадится и сохраняется под иминем"popped_magazin"(2)
#вывод изменного списка(3), показывввает что значение было удалено из списка. затем мы выводим извлеченное знаечение(4),
#демонстрируем что было устранено из списка значение остается доступным в программе



#для чего может понадобится: представьте что инф. о мотоциклах хранится в программе в хронологическом порядке,соответствующая дате
#покупки,в таком случае эта команда может исп для вывода сооб о последнем купленом мотоцикле
last_owned = magazin.pop()
print(f'последний магазин в котором я был {last_owned.title()}.')
#удаление элементов по назначению
magazin = ['lenta', 'dicsi','4 lap']
magazin.remove('lenta')
print(magazin)
#кроме того этого команда позволяет работать с удаленным значением из списка
magazin = ['lenta', 'dicsi','4 lap']#1
off_magazin='dicsi'#2
magazin.remove(off_magazin)#3
print(magazin)
print(f'\n "место где выключили свет", {off_magazin.title()}!')#4
#после определения списка 1 значение diksi сохранено в другую переменную 2 затем эта переменная сообщает пайтон какая переменная должна быть удалена
#из списка 3 это значение было удалено из списка 4  но продолжает хранится в переменной, что позволяет вывести сообщение
# изза чего была удалена переменная из списка


gosti = ['mama', 'papa', 'zlata']

priglashenie = f"приглашаем вас на свадьбу \n {gosti [0].title()} \n {gosti [1].title()} \n {gosti[2].title()}."
print(priglashenie)
#сначала мы сделали общее приглашение для всех, а в след примере поменяли злату на тимошу




gosti = ['mama', 'papa', 'zlata']
del gosti[2]
gosti.insert(2,'timosha')
priglashenie = f"приглашаем вас на свадьбу \n {gosti [0].title()} \n {gosti [1].title()} \n {gosti[2].title()}."
print(priglashenie)

gosti = ['mama', 'papa', 'zlata']

priglashenie = f"приглашаем вас на свадьбу \n {gosti [0].title()} \n {gosti [1].title()} \n {gosti[2].title()}."
print(priglashenie)
print('мы нашли стол по больше и решили пригласить еще людей!')



gosti = ['mama', 'papa', 'zlata']
gosti.insert(0,'mark')
gosti.insert(2,'vlad')
gosti.append('roma')
print(gosti)
print(f'приглашаем вас на свадьбу {gosti[0].title()}')
print(f'приглашаем вас на свадьбу {gosti[1].title()}')
print(f'приглашаем вас на свадьбу {gosti[2].title()}')
print(f'приглашаем вас на свадьбу {gosti[3].title()}')
print(f'приглашаем вас на свадьбу {gosti[4].title()}')
print(f'приглашаем вас на свадьбу {gosti[-1].title()}')


priglashonn = ['mark', 'mama', 'vlad', 'papa', 'zlata', 'roma']
last_owned= priglashonn.pop()
print(f'извините все места заняты {last_owned.title()}')
del priglashonn [0]
print(priglashonn)


#отсортировать список в алфавитном порядке при помощи sort
imena = ['mama', 'papa','audi']
imena.sort()
print(imena)
#а так же можно отсортировать в обратном алфавитном порядке
imena = ['mama', 'papa','audi']
imena.sort(reverse=True)
print(imena)
#эта команда позволяет понять количество списка
imena = ['mama', 'papa','audi','hi']
print(len(imena))

#вывод списка в обратном порядке
imena = ['mama', 'papa','audi']
imena.reverse()
print(imenar)







