# Aliasing - second name for piece of data.
# Easier (and more useful) than making a second copy.
# If data is immutable, aliases don't matter
# Because data can't change.
#But if data, can change, can lead to bugs

first = "Isaac"
second = first
second = "Newton"

# Not mutable, creates new string
first = first + "Newton"

# List is mutable, both first and second point to same list in memory.
#Changes in first will affect second.

first = ["Isaac"]
second = first
# Only appending list....
first.append("Newton")

#But returns mutated list!
print(second)