# 1
students = {}

for _ in range(int(input())): # 2
    # 3
    name = input()
    # 4
    grade = float(input())
    # 5
    students.setdefault(grade, []).append(name)

# 6
second_lowest_grade = sorted(students.keys())[1]
# 7
for name in sorted(students[second_lowest_grade]):
    print(name)


# Explanation
# 1 : 
    # Empty list created

# 2 :
    # Enter Number of students 

# 3 :
    # Getting name of student from the user

# 4 :
    # Getting marks of student form the user

# 5 :
    # When same grade matches, values will be appended instead of overwritten in students dictionary 
    # For example:
    # students = {
    #     10 : ["Uday"],
    #     8 : ["Kunj", "Jenish"],
    #     7 : ["Darshit", "Mihir"],
    #     5 : ["Vishv"]
    # }
    # if append() method is not being used then Jenish will be overwitten on Kunj and same in 3rd key-value pair

# 6 :
    # It will sotre second lowest grade in second_lowest_grade variable

# 7 :
    # Sorting all names(values) available in second_lowest_grade key