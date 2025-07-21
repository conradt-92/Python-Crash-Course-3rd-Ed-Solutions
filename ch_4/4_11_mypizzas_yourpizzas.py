# CT
# make a copy of a list
# add new pizza to original, add different pizza to new list
# prove you have 2 different lists

my_pizzas = ['pepperoni' , 'mushroom' , 'supreme']

friend_pizzas = my_pizzas[:]

my_pizzas.append('meatlovers')

friend_pizzas.append('hawaiian')

print('\nMy favorite pizzas are: ')
print(my_pizzas)

print("\nMy friend's favorite pizzas are")
print(friend_pizzas)