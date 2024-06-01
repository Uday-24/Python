# Definition :- Find the factors of a number

num = int(input("Enter the nmber :"))
for i in range(1, num+1):
    if num%i==0:
        print(i, end=" ")
