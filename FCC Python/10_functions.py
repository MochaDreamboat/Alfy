# Functions

# Declaring a function
# def func(params*): {}
# *optional
def sayhi(name):
 print(f"Ayy {name}")


# Calling function
sayhi('Jerold')

# Default params
def power(x=2, y=3):
    print(x**y)


power() # Defaults to printing 8

# Format rule: Underscore between two or more words


# Return statement

def cube(num):
    return num*num*num


cube(3)