# Task
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Constrain 1 <= n <=100

if __name__ == '__main__':
    n = int(input().strip()) # Strip() function is used to remove white space
    
    if n%2==1:
        print("Weird number")
    elif n<=5:
        print("Not weird")
    elif n>=6 and n<=20:
        print("Weird")
    else:
        print("Not weird")
    