n = 7016489410
tmp = n
words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tmp_words = []
while tmp > 0:
    rem = tmp % 10
    tmp_words.append(words[rem])
    tmp = tmp // 10

for i in tmp_words[::-1]:
    print(i, end=" ")