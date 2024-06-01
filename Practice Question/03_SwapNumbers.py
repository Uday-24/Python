# Definition :- Swap two numbers

x = 10
y = 20

print("Before Swap")
print(f"X = {x}")
print(f"Y = {y}")

# 1 - Using third variable
# temp = x
# x = y
# y = temp

# 2 - Without using third variable
x, y = y, x

print("After Swap")
print(f"X = {x}")
print(f"Y = {y}")