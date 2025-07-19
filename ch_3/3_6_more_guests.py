# Conrad T
# We invited 3 people to dinner, but we got a bigger table
# We will add 3 people to the dinner guest list
# We will invite everyone again

dinner_guests = ['Arsene Wenger','Thierry Henry','Ian Wright']

print(f'{dinner_guests[0].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[1].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[2].title()}, I would like to invite you to dinner!')

print("We're in luck! The restaurant has a bigger table, we can now seat 6!")
dinner_guests.insert(0, 'Bukayo Saka')
dinner_guests.insert(2, 'Dennis Bergkamp')
dinner_guests.append('Tony Adams')

print(f'{dinner_guests[0].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[1].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[2].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[3].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[4].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[5].title()}, I would like to invite you to dinner!')
