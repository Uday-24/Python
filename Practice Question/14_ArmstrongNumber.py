# Difinition :- An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 1 + 125 + 9 = 153

num = int(input("Enter number :"))
armstrong = 0
temp = num
while(temp!=0):
    rem = temp%10
    armstrong = armstrong + (rem ** 3)
    temp = temp // 10

if num == armstrong:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")