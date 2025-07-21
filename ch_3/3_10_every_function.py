# Conrad T
# create a list of the earth's continents
# use every function in this chapter

continents = ['Europe','Australia','South America', 'Asia', 'North America', 'Africa']

print(f'There are {len(continents)} continents on the Earth. \n')
print("They are: \n")
print(continents)

print('\nWait, thats not right!')
continents.append("Antarctica")

print(f'There are {len(continents)} continents on the Earth. \n')
print('They are: \n')
print(continents)

continents.reverse()
print('The list in reverse order: \n')
print(continents)

print('The list in Alphabetical order: \n')
print(sorted(continents))

print('The list in reverse alphabetical order: \n')
print(sorted(continents, reverse=True))