def loop72to73():
    print("Loop 72 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i+1, size+1):
            print(end="  ")
        for j in range(1, i+1-1):
            print(j, end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    print()
    print("Loop 73 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i+1, size+1):
            print(end="  ")
        for j in range(i, 0+1, -1):
            print(j, end=" ")
        for j in range(1, i+1):
            print(j, end=" ")
        print()


def loop73to77():
    print("Loop 74 :")
    s = "abcde"
    size = len(s)

    for i in range(1, size+1):
        for j in range(i+1, size+1):
            print(end="  ")
        for j in range(1, i):
            print(s[j-1], end=" ")
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()

    print()
    print("Loop 75 :")
    size = 10
    for i in range(65, 65+size):
        for j in range(i+1, 65+size):
            print(end="  ")
        for j in range(65, i+1-1):
            print(chr(j), end=" ")
        for j in range(i, 65-1, -1):
            print(chr(j), end=" ")
        print()

    print()
    print("Loop 76 :")
    s = "abcde"
    size = len(s)
    
    for i in range(size, 0, -1):
        for j in range(1, i):
            print(end="  ")
        for j in range(size, i, -1):
            print(s[j-1], end=" ")
        for j in range(i, size+1):
            print(s[j-1], end=" ")
        print()
    

    print()
    print("Loop 77 :")
    s = "ABCDE"
    size = len(s)

    for i in range(size, 0, -1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size):
            print(s[j-1], end=" ")
        for j in range(size, i-1, -1):
            print(s[j-1], end=" ")
        print()


def loop78to82():
    print("Loop 78 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(1, i):
            print(end="  ")
        for j in range(size, i, -1):
            print(j, end=" ")
        for j in range(i, size+1):
            print(j, end=" ")
        print()

    print()
    print("Loop 79 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i):
            print(j, end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    print()
    print("Loop 80 :")
    size = 5
    for i in range(1, size+1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size):
            print(j, end=" ")
        for j in range(size, i-1, -1):
            print(j, end=" ")
        print()

    print()
    print("Loop 81 :")
    s = "ABCDE"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i):
            print(s[j-1], end=" ")
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()

    print()
    print("Loop 82 :")
    s = "abcde"
    size = len(s)
    for i in range(1, size+1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size):
            print(s[j-1], end=" ")
        for j in range(size, i-1, -1):
            print(s[j-1], end=" ")
        print()


def loop83to86():
    print("Loop 83 :")
    s = "ABCDE"
    size = len(s)

    for i in range(size, 0, -1):
        for j in range(1, i+1):
            if i==size and j==size:
                continue
            print(s[j-1], end=" ")
        for j in range(i+1, size):
            print(end="  ")
        for j in range(i, size):
            print(end="  ")
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()

    
    print()
    print("Loop 84 :")
    size = 5+96
    for i in range(size, 96, -1):
        for j in range(97, i+1):
            if j==size and i==size:
                continue
            print(chr(j), end=" ")
        for j in range(i+1, size):
            print(end="  ")
        for j in range(i, size):
            print(end="  ")
        for j in range(i, 96, -1):
            print(chr(j), end=" ")
        print()

    
    print()
    print("Loop 85 :")
    s = "ABCDE"
    size = len(s)
    for i in range(1, size+1):
        for j in range(1, i+1):
            if i==size and j==size:
                continue
            print(s[j-1], end=" ")
        for j in range(i+1, size):
            print(end="  ")
        for j in range(i, size):
            print(end="  ")
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()


    print()
    print("Loop 86 :")
    size = 101
    for i in range(97, size+1):
        for j in range(97, i+1):
            if(j==size and i==size):
                continue
            print(chr(j), end=" ")
        for j in range(i+1, size):
            print(end="  ")
        for j in range(i, size):
            print(end="  ")
        for j in range(i, 96, -1):
            print(chr(j), end=" ")
        print()



def loop87to89():
    print("Loop 87:")
    size = 5
    for i in range(size, 0, -1):
        for j in range(1, i+1):
            if(i==size and j==size):
                continue
            print(j, end=" ")
        for j in range(i+1, size):
            print(end="  ")
        for j in range(i, size):
            print(end="  ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    print()
    print("Loop 88 :")
    size = 5
    for i in range(1, size+1):
        for j in range(1, i+1):
            if(i==size and j==size):
                continue
            print(j, end=" ")
        for j in range(i+1, size):
            print(end="  ")
        for j in range(i, size):
            print(end="  ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


    print()
    print("Loop 89 :")
    s = "abcde"
    size = len(s)
    for i in range(1, size+1):
        for j in range(size, i-1, -1):
            if(i==1 and j==1):
                continue
            print(s[j-1], end=" ")
        for j in range(2, i):
            print(end="  ")
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size+1):
            print(s[j-1], end=" ")
        print()


def loop90to91():
    print("Loop 90 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i):
            print(j, end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
    size = size-1
    for i in range(size, 0, -1):
        for j in range(i, size+1):
            print(end="  ")
        for j in range(1, i+1):
            print(j, end=" ")
        for j in range(i-1, 0, -1):
            print(j, end=" ")
        print()

    print()
    print("Loop 91 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    size = size - 1
    for i in range(size, 0, -1):
        for j in range(i, size+1):
            print(end="  ")
        for j in range(i, 1, -1):
            print(j, end=" ")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

def loop92to93():
    print("Loop 92 :")
    s = "abcde"
    size = len(s)
    
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i):
            print(s[j-1], end=" ")
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()
    
    size = size - 1
    for i in range(size, 0, -1):
        for j in range(i, size+1):
            print(end="  ")
        for j in range(1, i):
            print(s[j-1], end=" ")
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()


    print()
    print("Loop 93 :")
    size = 69
    for i in range(65, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(65, i):
            print(chr(j), end=" ")
        for j in range(i, 64, -1):
            print(chr(j), end=" ")
        print()

    size -= 1
    for i in range(size, 64, -1):
        for j in range(i, size+1):
            print(end="  ")
        for j in range(65, i):
            print(chr(j), end=" ")
        for j in range(i, 64, -1):
            print(chr(j), end=" ")
        print()


def loop94to96():
    print("Loop 94 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i):
            print(j, end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    size -= 1
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i+2):
            print(j, end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


    print()
    print("Loop 95 :")
    s = "ABCDE"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i):
            print(s[j-1], end=" ")
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()

    for i in range(1, size):
        for j in range(i, size-1):
            print(end="  ")
        for j in range(1, i+2):
            print(s[j-1], end=" ")
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()

    print()
    print("Loop 96 :")
    s = "abcde"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i):
            print(s[j-1], end=" ")
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()

    for i in range(1, size):
        for j in range(i, size-1):
            print(end="  ")
        for j in range(1, i+2):
            print(s[j-1], end=" ")
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()


def loop97():
    print("Loop 97 :")
    size = 5
    k = 97
    l = 96
    for i in range(size, 0 , -1):
        for j in range(1, i+1):
            if j == size:
                continue
            print(j, end=" ")
        k = 97
        for j in range(i+1, size):
            print(chr(k), end=" ")
            k+=1
        
        k = 97
        for j in range(i, size):
            if j == i:
                l += 1
                k = l
            print(chr(k), end=" ")
            k -= 1
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    size = size -1
    k = 97
    l = 96
    for i in range(1, size+1):
        for j in range(1, i+2):
            if j == size+1:
                continue
            print(j, end=" ")
        for j in range(i+1, size):
            if j == i+1:
                k = 97
            print(chr(k), end=" ")
            k += 1
    
        for j in range(i, size):
            if j == i:
                l = 97
                l = l + (size - i - 1)
            print(chr(l), end=" ")
            l-=1
        for j in range(i+1, 0, -1):
            print(j, end=" ")
        print()



def loop98():
    print("Loop 98 :")
    s = "uday"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(1, i+1):
            if j == size and i == size:
                continue
            print(s[j-1], end=" ")
        k = 1
        for j in range(i+1, size):
            print(k, end=" ")
            k+=1
        k = size-1
        for j in range(i, size):
            print(k+1-i, end=" ")
            k-=1
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()

    for i in range(2, size+1):
        for j in range(1, i+1):
            print(s[j-1], end=" ")
        k = 1
        for j in range(i, size):
            print(k, end=" ")
            k+=1
        k = size-1
        for j in range(i+1, size):
            print(k-i,end=" ")
            k-=1
        for j in range(i, 0, -1):
            if(i==size and j==size):
                continue
            print(s[j-1], end=" ")
        print()



def loop99():
    print("Loop 99 :")
    size = 5
    k = 1
    for i in range(1, size+1):
        for j in range(1, i+1):
            print(k, end=" ")
            k+=1
        k-=1
        print()


def loop100():
    print("Loop 100 :")
    size = 5
    sum=0
    k=1
    for i in range(1, size+1):
        for j in range(1, i+1):
            print(k, end=" ")
            sum = sum + k
            k = k + 1
        k = sum
        sum = 0
        print()

loop72to73()
loop73to77()
loop78to82()
loop83to86()
loop87to89()
loop90to91()
loop92to93()
loop94to96()
loop97()
loop98()
loop99()
loop100()