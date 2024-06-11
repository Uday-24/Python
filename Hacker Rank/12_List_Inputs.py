if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        string = input()
        string = list(string.split(" "))
        if string[0] == "print":
            print(lst)
        elif string[0] == "insert":
            lst.insert(int(string[1]), int(string[2]))
        elif string[0] == "remove":
            lst.remove(int(string[1]))
        elif string[0] == "append":
            lst.append(int(string[1]))
        elif string[0] == "sort":
            lst.sort()
        elif string[0] == "pop":
            lst.pop()
        elif string[0] == "reverse":
            lst.reverse()