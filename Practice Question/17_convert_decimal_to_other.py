# Definition :- Convert decimal to binary, octal and hexadecimal
# Use built in function
decimal = int(input("Enter number : "))
print(f"{decimal} = {bin(decimal)} (binary)")
print(f"{decimal} = {oct(decimal)} (octal)")
print(f"{decimal} = {hex(decimal)} (hexadecimal)")