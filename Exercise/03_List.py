# Python | Ways to find length of list

lst = [10, 20, 40, 50, 30]

# 1
print("1) ",len(lst))

# 2
count = 0
for _ in lst:
    count = count + 1
print("2) ",count)

# 3
lst_len = sum(1 for _ in lst)
print("3) ",lst_len)

# 4
s=0
for _ in enumerate(lst):
    s+=1
print("4) ",s)

# 5
from collections import Counter
lst_len = sum(Counter(lst).values())
print("5) ", s)