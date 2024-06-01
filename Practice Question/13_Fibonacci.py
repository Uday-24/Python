# Difinition :- Print the fibonacci series
# Fibonacci series : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 .....
# Basically first two terms are 0 and 1
# Next term is equals to previous two terms

element = int(input("Enter the number of an element : ")) 
t1 = 0
t2 = 1
t3 = t1 + t2
if element > 2:
    print(f"Fibonacci series : {t1} {t2}", end=" ")
    for i in range(3, element+1):
        print(f"{t3}", end=" ")
        t1 = t2
        t2 = t3
        t3 = t1 + t2
elif element == 1:
    print(f"Fibonacci series : {t1}")
elif element == 2:
    print(f"Fibonacci series : {t1} {t2}")
else:
    print("Sorry...invalid Input...")