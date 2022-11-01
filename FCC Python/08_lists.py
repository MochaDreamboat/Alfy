# Making a list
friends = ["Peyton", "Sowji", "Annie", "Robert"]

# Accessing array values
print(friends[1:]) # Returns ['Sowji', 'Annie', 'Robert']
print(friends[1:3]) # Returns ['Sowji', 'Annie']

# Changing array value at an index
# friends[2] = 'Roberta'
# print(friends[2])

numbers = [1, 2, 3, 4, 5]

numbers.extend(friends) # Extends numbers param w/ friends list (returns None)
print(numbers)