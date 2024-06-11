# Python program to interchange first and last elements in list

lst = [1, 2, 4 , 5, 3]

lst[0], lst[len(lst)-1] = lst[len(lst)-1], lst[0]

print(lst)