# Difinition :- Find the power of 2 in series using anonymous function

nterms = int(input("Enter number of terms : ")) 
result = list(map(lambda x : 2**x, range(nterms)))

print(result)