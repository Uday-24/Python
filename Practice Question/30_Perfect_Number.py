# Find the perfect number
# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. In other words, if you list all the divisors of a number (including 1 but excluding the number itself), the sum of these divisors should equal the number.

num = int(input("Enter number : "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(f"{num} is Perfect Number")
else:
    print(f"{num} is NOT Perfect Number")