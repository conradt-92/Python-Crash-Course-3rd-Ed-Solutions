# Conrad T  
# using a program from chapter 4 add several lines to the end of the code that:
# print first 3 items in list
# print 3 items in middle of list
# print last 3 items in list

cubes = [number**3 for number in range(1,11)]

print(f'The first three cubes are {cubes[:3]}.\n')

middle = len(cubes)//2
print(f'Three items from the middle of the list are: {cubes[middle-1:middle+2]}.\n')

print(f'The last three cubes are {cubes[-3:]}.\n')