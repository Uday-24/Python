# Definition :- Check the number is prime number of not

num = int(input("Enter number : "))
count=0
for i in range(2, num):
    if num%i == 0:
        count += 1

if count == 0:
    print(f"{num} is a prime number")
else:
    print(f"{num} is NOT a prime number")