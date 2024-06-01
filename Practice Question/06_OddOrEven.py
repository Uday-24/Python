# Definition :- Check the number if it is ODD or EVEN

num = int(input("Enter number :"))
if num!=0:
    if num%2 == 0:
        print(f"{num} is EVEN number")
    else:
        print(f"{num} is ODD number")
else:
    print(f"{num} is neither ODD nor EVEN")