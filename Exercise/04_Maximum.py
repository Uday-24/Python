# Find the maximum of two numbers

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))

# Method 1
if a > b:
    print(a)
elif b > a:
    print(b)

# Method 2
print(max(a, b))

# Method 3
print(a if a>=b else b)