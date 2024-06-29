# Convert Days into Years, Weeks and Days

days = int(input("Enter day : "))
years = days // 365
weeks = 0
if years != 0:
    temp_days = days - (years * 365)
    weeks = temp_days // 7
else:
    weeks = days // 7

res_days = days % 7
res_days -= years

print(f"{years} Years(s) {weeks} Weeks(s) {res_days} Day(s)")