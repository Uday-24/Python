# Reverse words in python

string = "geeks quiz practice code"

# Method 1
s = string.split()[::-1]
for i in s:
    print(i, end=" ")

# Mthod 2
print()
s = " ".join(reversed(string.split()))
print(s)


# Method 3
stack = []
for i in string.split():
    stack.append(i)

reversed_words = []
while stack:
    reversed_words.append(stack.pop())

print(" ".join(reversed_words))