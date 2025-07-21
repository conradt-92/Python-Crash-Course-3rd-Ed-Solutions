# CT
# store 5 foods in a tuple
# use for loop to print items
# try to modify an item in the tuple
# menu changes, replace 2 items with new items

foods = ('chicken','fries','burger','hot dog','pizza')

print('\nCurrent menu: ')
for food in foods:
    print(f'\t{food.title()}')

# foods[3] = "spaghetti"    #try to change value in tuple, python wont allow this

foods = ('baked potato','fries','burger','spaghetti','pizza')
print('\nNew Menu: ')
for food in foods:
    print(f'\t{food.title()}')