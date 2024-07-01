# Python program to swap two elements in list

lst = [10, 20, 50, 40, 30,70]
print(lst)
pos1 = int(input("Enter position 1 :"))-1
pos2 = int(input("Enter position 2 :"))-1

if pos1 < len(lst) and pos2 < len(lst):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    print(lst)
else:
    print("Position should be less than size of list")