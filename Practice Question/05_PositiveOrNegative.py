# Definition :- Check number if Positive or Negative

num = int(input("Enter number :"))
if num>0:
    print(f"{num} is positive number")
elif num<0:
    print(f"{num} is negative number")
else:
    print(f"{num} is neither positive nor negative")