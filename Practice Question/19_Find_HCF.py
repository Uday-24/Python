# Definition :- Find the HCF (Highest Common Factor) of two numbers

num1 = 15
num2 = 30
if num1<num2:
    for i in range(1, num1+1):
        if num1%i==0 and num2%i==0:
            hcf = i
else:
    for i in range(1, num2+1):
        if num2%i==0 and num1%i==0:
            hcf = i
print(hcf)