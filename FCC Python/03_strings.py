# Line break
print("Line one\n Line two")

# Literal
print("\"Jerold Macaya\"")

# Lower method
string_one = "PIZZA"
print(string_one.lower())
print(string_one.lower().islower()) # Returns true

#Upper method
string_two = "pancakes"
print(string_two.upper())
print(string_two.upper().isupper()) # Returns true

#length
print(len(string_one)) # Returns 5

#index
print(string_one[0]) # Returns 'P'
print(string_one[1]) # Returns 'I'
print(string_one[2]) # Returns 'Z'

print(string_one.index('Z')) # Returns 2 (first Z)
print(string_one.index('ZA')) # Returns 3

#replace
print(string_one.replace("IZZ", "IS")) #Returns "PISA"