num = int(input("Enter a number here :"))

for i in  range(1, num+1):
    for j in range(1, num+1):
        print(i*j, end=" ")
    print()