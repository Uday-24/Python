# Difinition :- Print the series of the Armstrong numbers

element = int(input("Enter number of elements : "))
start = 0
i=1
while(True):
    num = i
    temp = num
    sum = 0
    while(temp!=0):
        rem = temp%10
        sum = sum + (rem**3)
        temp = temp // 10
    if sum == num:
        print(f"{num} ",end="")
        start = start + 1
    i = i+1
    if element <= start:
        break