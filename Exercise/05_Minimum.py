# Find the minimum of two numbers

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))

# Method 1
if a < b:
    print(a)
else:
    print(b)

# Method 2
print(min(a, b))

# Method 3 
print(a if a<b else b)