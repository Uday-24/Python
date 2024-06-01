# Definition :- Fing the largest number among Three

def logic1(n1, n2, n3):
    if n1>n2 and n1>n3:
        print(f"{n1} is the largest number of all")
    elif n2>n3:
        print(f"{n2} is the largest number of all")
    else:
        print(f"{n3} is the largest number of all")

def logic2(n1, n2, n3):
    if n1>n2:
        if n1>n3:
            print(f"{n1} is the largest number of all")
        else:
            print(f"{n3} is the largest number of all")
    else:
        if n2>n3:
            print(f"{n2} is the largest number of all")
        else:
            print(f"{n3} is the largest number of all")

num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
num3 = int(input("Enter number 3 :"))

logic1(num1, num2, num3)
logic2(num1, num2, num3)