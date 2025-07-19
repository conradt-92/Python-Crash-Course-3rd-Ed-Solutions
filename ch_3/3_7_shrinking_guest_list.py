# Conrad T
# We invited 6 people to dinner, the table is unavailable, we can only invite 2
# We will remove 4 people from the list
# We will invite the remaining 2

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

print(f'Bad news! The restaurant downsized our table, I can only bring 2 people! :(')

rem1 = dinner_guests.pop(0)
print(f'Sorry, {rem1}, I can no longer invite you to dinner!')

rem2 = dinner_guests.pop(1)
print(f'Sorry, {rem2}, I can no longer inivte you to dinner!')

rem3 = dinner_guests.pop(2)
print(f'Sorry, {rem3}, I can no longer invite you to dinner!')

rem4 = dinner_guests.pop(2)
print(f'Sorry, {rem4}, I can no longer invite you to dinner!')

print(f'{dinner_guests[0].title()}, I would like to invite you to dinner!')
print(f'{dinner_guests[1].title()}, I would like to invite you to dinner!')