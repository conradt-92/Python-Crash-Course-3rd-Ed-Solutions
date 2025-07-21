# Conrad T
# Create a list of destinations, in non alphabetical order
# Shows various method of sorting a list
# Alphabetical, reverse-alphabetical, reverse orders

destinations = ['japan', 'greece', 'scotland', 'spain', 'maldives']

print("The original list: ")
print(destinations)

print("\nThe list in alphabetical order: ")
print(sorted(destinations))

print("\nThe list in reverse alphabetical order: ")
print(sorted(destinations, reverse=True))

print("\nThe original list: ")
print(destinations)

destinations.reverse()
print("\nThe list in reverse order: ")
print(destinations)

destinations.reverse()
print("\nBack in original order: ")
print(destinations)

destinations.sort()
print("\nPermanently sorting the list in alphabetical order: ")
print(destinations)

destinations.sort(reverse=True)
print("\nPermanently sorting list in reverse alphabetical order: ")
print(destinations)