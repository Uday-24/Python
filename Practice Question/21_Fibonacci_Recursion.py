# Find Fibonacci series in range using recursion

def printFibonacci(num, t1=0, t2=1, t3=0):
    if(num==0):
        return
    print(t3, end=" ")
    t3 = t1 + t2
    num -= 1
    printFibonacci(num, t2, t3, t3)

printFibonacci(10)