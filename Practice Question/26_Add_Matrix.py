a = [
    [1, 5, 3],
    [2, 4, 8],
    [7, 5, 4]
]

b = [
    [6, 4, 9],
    [3, 7, 2],
    [1, 7, 8]
]

c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]

for r in c:
    print(r)