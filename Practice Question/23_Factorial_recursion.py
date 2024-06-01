# Find the factorial using recursion

def factorial(num, fact = 1):
    if num == 0:
        return 1
    if num == 1:
        return fact
    fact = fact * num
    num -= 1
    return factorial(num, fact)

print(factorial(5))