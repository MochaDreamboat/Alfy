# r - read-only, r+w - read/write, a - append (only new info)

employee_file = open("FCC Python/employees.txt", "r")

# Returns boolean that tells us whether or not we can read file
print(employee_file.readable())

# Returns all information in file
print(employee_file.read())

# Returns first line / next line if called repeatedly
print(employee_file.readline())

# Iterating over info in a file
for employee in employee_file.readlines():
    print(employee)

# Make sure you close file
employee_file.close()