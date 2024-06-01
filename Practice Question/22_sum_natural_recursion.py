# Find sum of natural number in range using recursion

def sumNatural(num, sum=0):
    if num < 0:
        print("Negative number are not allowed")
        return
    if(num==0):
        return sum
    sum = sum + num
    num = num - 1
    return sumNatural(num, sum)

print(sumNatural(10))