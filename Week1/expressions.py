# Imported Regex library for use in quadratic_equation_solver_from_user()
import re

def calc_math_expression(num1, num2, operator):
    # Operators: + - * :
    if (type(num1) is not float) or (type(num2) is not float) or (type(operator) is not str):
        return None
    
    if operator == ':' and (num1 == 0 or num2 == 0):
        return None

    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        ':': num1 / num2
    }

    return operations[operator]


def calc_math_expression_from_str(str_input):
    valid_ops = ['*', ':', '+', '-']
    expressions = str_input.split(' ')

    # Operators cannot be at the beginning or end
    if expressions[0] in valid_ops or expressions[-1] in valid_ops:
        return None

    for char in valid_ops:
        while char in expressions:
            operation = expressions.index(char)
            x = expressions[operation - 1]
            y = expressions[operation + 1]
            if x in valid_ops or y in valid_ops:
                return None
            
            expressions.pop(expressions.index(x))
            expressions.pop(expressions.index(y))
            expressions[expressions.index(char)] = calc_math_expression(float(x), float(y), char)

    if len(expressions) > 1:
        return None

    return expressions[0]


def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    nums = [num1, num2, num3]
    nums.sort()
    return (nums[-1], nums[0])


def quadratic_equation_solver(a, b, c):
    n_1 = -(b)
    n_2 = b**2
    n_3  = (4 * a * c)

    if a == 0 or n_2 < n_3:
        return (None, None)

    sol_1 = (n_1 + ((n_2 - n_3)**0.5)) / (2 * a)
    sol_2 = (n_1 - ((n_2 - n_3)**0.5)) / (2 * a)

    if sol_1 == sol_2:
        return (sol_1, None)

    return (sol_1, sol_2) if sol_1 > sol_2 else (sol_2, sol_1)


def quadratic_equation_solver_from_user(str): # Did not have any tests
    values = str.split(' ')

    # RegEx for correct number format
    r = re.compile(r"^\d*[.,]?\d*$")

    for value in values:
        if r.match(value) == False:
            return (None, None)
        
    return quadratic_equation_solver(float(values[0]), float(values[1]), float(values[2]))


def temp_checker(min_temp, temp_1, temp_2, temp_3):
    temps = [temp_1, temp_2, temp_3]
    sufficient_temps = 0

    for x in temps:
        if x > min_temp:
            sufficient_temps += 1
    
    return True if sufficient_temps >= 2 else False