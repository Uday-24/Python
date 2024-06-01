# Definition :- Print sum of natural number in range

lower = int(input("Enter lower limit : "))
upper = int(input("Enter upper limit : "))

sum = 0

if lower>0 and lower<=upper:
    for i in range(lower, upper+1):
        sum = sum + i
    print(f"Sum of natural number between {lower} and {upper} is {sum}")
else:
    print("Oops...Invalid input")