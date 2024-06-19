# Print the Transpose of matrix


# Method 1 : Aam Zindagi

# A = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# T = [
#     [0, 0],
#     [0, 0],
#     [0, 0]
# ]

# for i in range(len(A)):
#     for j in range(len(A[i])):
#         T[j][i] = A[i][j]
    
# for t in T:
#     print(t)


# Method 2 : Mentos Zindagi
# Using List Comprehension

A = [
    [1, 2, 3],
    [4, 5, 6]
]

T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

for i in T:
    print(i)