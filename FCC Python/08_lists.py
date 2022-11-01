# Making a list
friends = ["Peyton", "Sowji", "Annie", "Robert"]

# Accessing array values
print(friends[1:]) # Returns ['Sowji', 'Annie', 'Robert']
print(friends[1:3]) # Returns ['Sowji', 'Annie']

# Changing array value at an index
# friends[2] = 'Roberta'
# print(friends[2])

numbers = [1, 2, 3, 4, 5]

# .extend(iterable)
numbers.extend(friends) # Extends list with iterable (list, tuple, string, etc.)
print(numbers)

# .append(element)
numbers.append('add me!') # appends element to end of List

#.insert(index, element)
numbers.insert(3, "Tracey") # Adds element at given index position

#.remove(element)
numbers.remove("Tracey") # Removes first instance of element in list

# .pop()
numbers.pop() # Removes last element from list

#.index("element")
numbers.index("Sowji") # Returns index of element's first appearance

#.clear()
numbers.clear() # Removes ALL items in List. Careful!

#.count(element)
numbers.count("Sowji") # Counts number of instances of element

# .sort()
numbers.sort() # Sorts List in ascending order

# .reverse()
numbers.sort() # Reverse list (back to front)