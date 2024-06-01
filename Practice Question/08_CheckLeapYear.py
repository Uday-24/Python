# Definition :- Check the year if it is leap year or not
# Leap Year : If the year (is divisible by 400) or (divisible by 4 AND not divisible by 100) 
# For example : 2000 is leap year, 2100 is not leap year
# For example : 2024 is leap year, 2022 is not leap year

year = int(input("Enter the year : "))

if year%400 == 0:
    print(f"{year} is a leap year")
elif year%4 == 0 and year%100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")