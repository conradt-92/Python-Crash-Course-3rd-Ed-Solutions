# CT
# the original code avoids using loops, to save space

#foods.py from pg 63

""" my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] 

print("My favorite foods are:") 
print(my_foods) 
print("\nMy friend's favorite foods are:") 
print(friend_foods) """

# print the items in each list using for loops

my_foods = ['pizza','falafel','carrot cake']
friends_foods = my_foods[:]

my_foods.append('burger')
friends_foods.append('bacon')

print("\nMy favorite foods are: ")
for food in my_foods:
    print(f"\t{food}")

print("\nMy friend's favorite foods are: ")
for food in friends_foods:
    print(f"\t{food}")

    