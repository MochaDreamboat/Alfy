# New variable, same refereence
org = 5
copy = org
copy = 6
print(copy) # 6
print(org) # 5

# Same place in memory, both mutated
org2 = [0, 1, 2, 3, 4]
copy2 = org2
copy2[0] = -10
print(copy2) # [-10, 1, 2, 3, 4]
print(org2) # [-10, 1, 2, 3, 4]

#Shallow Copy: one level deep, only references of nested child objects

#Deep copy: full independent copy