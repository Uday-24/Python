# Definition :- Take input form user and print table of that number

num = int(input("Enter number : "))
i=1
while(i<=10):
    print(f"{num} * {i} = {num*i}")
    i+=1