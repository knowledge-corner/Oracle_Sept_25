# Write utility function for mathematical operations

# Assuming this is multiple level validation check
def is_valid(fn):
    def check(*numbers):
        if all(map(lambda num : type(num) == int, numbers)):
            return fn(*numbers)
        else:
            return None
            # raise ValueError("Input must be an integer")
    return check  # returns object of inner function

# Factorial function
@is_valid
def factorial(num):
    result = 1
    for i in range(num, 1, -1):
        result *= i
    return result

# Even or odd function
@is_valid
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Prime check function
@is_valid
def is_prime(num):  
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

    
# Addition function
@is_valid
def add(a, b):  
    return a + b

