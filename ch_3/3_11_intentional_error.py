# Conrad T
# intentionally create an indexing error

dog_breeds = ['dachshud', 'german shepherd', 'rottweiler', 'french bulldog', 'english bulldog']


# the code below contains and index error
#print(f'Breeds I have never owned: \t{dog_breeds[5]} \t{dog_breeds[4]}')
#print(f'\nBreeds I have owned: \t{dog_breeds[1]} \t{dog_breeds[2]} \t{dog_breeds[3]}')

# the corrected code
print(f'Breeds I have never owned: \t{dog_breeds[4].title()} \t{dog_breeds[3].title()}')
print(f'\nBreeds I have owned: \t{dog_breeds[0].title()} \t{dog_breeds[1].title()} \t{dog_breeds[2].title()}')