if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    ls = list(integer_list)
    t = ()
    for i in ls:
        t+=(i,)
    hashed = hash(t)
    print(hashed)