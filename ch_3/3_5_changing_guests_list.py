# Conrad T
# create a list of dinner guests
# invite each one to dinner, one guest cant make it
# change the list and invite everyone again, with the new member of the list

dinner_guests = ['Arsene Wenger','Thierry Henry','Ian Wright']

print(f'{dinner_guests[0].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[1].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[2].title()}, I would like to invite you to dinner!')
print(f'Unfortunately, {dinner_guests[1].title()} is unable to make it to dinner!')

dinner_guests[1] = 'Bukayo Saka'

print(f'{dinner_guests[0].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[1].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[2].title()}, I would like to invite you to dinner!')