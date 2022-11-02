from socket import IOCTL_VM_SOCKETS_GET_LOCAL_CID


is_male = True
is_tall = True

# if/else/else if syntax
# Logical operators: and / or / not(value)

if (is_male and is_tall):
    print("You are a male")
elif (is_male and not(is_tall)):
    print("Hey, short king!")
else:
    print("You are not a male")

# Comparison (>=, <=, ==, !==)
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    None