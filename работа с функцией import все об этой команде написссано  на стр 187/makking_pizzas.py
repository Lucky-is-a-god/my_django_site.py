import pizza
pizza.make_pizza(15, 'peperoni')
pizza.make_pizza(19,'extra chease', 'ananas')

#назначение псевдонима для функции
from pizza import make_pizza as mp
mp(116, 'peperoni')
mp(15, 'extra chease', 'ananas')