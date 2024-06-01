# Definition :- Find the Factorial of a number
# Factorial number 
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 0! = 1
num = int(input("Enter number : "))
fact = 1
if num>1:
    for i in range(num, 0, -1):
        fact = fact * i
elif num == 0 or num == 1:
    fact = 1
else:
    print(f"{num} is invalid input for Factorial")
    print()

if num>=0:    
    print(f"{num}! = {fact}")