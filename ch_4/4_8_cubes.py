# Conrad T
# make a list of the first 10 cubes (1^3, 2^3,...10^3)
# use a foor loop to print out the value of each cube

numbers = list(range(1,11))
cubes = []

for number in numbers:
    cube = number**3
    cubes.append(cube)
    print(cube)

print(cubes)