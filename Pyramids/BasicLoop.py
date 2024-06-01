global size
size = 6
def loop1to4():
    print("Loop 1 :")
    for i in range(1, size):
        for j in range(1 , i+1):
            print(j , end=" ")
        print()

    print()
    print("Loop 2 :")
    for i in range(size-1, 0, -1):
        for j in range(size-1, i-1, -1):
            print(j , end=" ")
        print()
    
    print()
    print("Loop 3 :")
    for i in range(1, size):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    print()
    print("Loop 4 :")
    for i in range(size-1, 0, -1):
        for j in range(i, size):
            print(j, end=" ")
        print()

def loop5to8():
    print("Loop 5 :")
    s = "abcde"
    size = len(s)
    for i in range(size):
        for j in range(i+1):
            print(s[j-1], end=" ")
        print()
    
    print()
    print("Loop 6 :")
    for i in range(97, 102):
        for j in range(97, i+1):
            print(chr(j),end=" ")
        print()
    
    print()
    print("Loop 6 :")
    s = "ABCDE"
    size = len(s)
    for i in range(size):
        for j in range(i+1):
            print(s[j], end=" ")
        print()

    print()
    print("Loop 7 :")
    s="abcde"
    size = len(s) + 1
    for i in range(1, size):
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()    

    print()
    print("Loop 8 :")
    s="ABCDE"
    size = len(s) + 1
    for i in range(1, size):
        for j in range(i, 0, -1):
            print(s[j-1], end=" ")
        print()

def loop9to14():
    print("Loop 9 :")
    size = 5
    for i in range(1,size+1):
        for j in range(i, 0, -1):
            print(i, end=" ")
        print()

    print()
    print("Loop 10 :")
    size = 9
    for i in range(size, 0, -1):
        for j in range(i, size+1):
            print(i, end=" ")
        print()
    
    print()
    print("Loop 11 :")
    s = "abcde"
    size = len(s)
    for i in range(1, size+1):
        for j in range(i, 0, -1):
            print(s[i-1], end=" ")
        print()

    print()
    print("Loop 13 and 14 :")
    s = "ABCDE"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(i, size+1):
            print(s[i-1], end=" ")
        print()
        
def loop15():
    size = 5
    c = 1
    for i in range(1, size+1):
        for j in range(1, i+1):
            print(c, end=" ")
            c+=1
        print()

def loop16to20():
    print("Loop 16 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(i, size+1):
            print(j%2, end=" ")
        print()


    print()
    print("Loop 17 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(i, size+1):
            if j%2==0:
                print(1,end=" ")
            else:
               print(0, end=" ")
        print()

    print()
    print("Loop 18 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, 0, -1):
            print(i%2, end=" ")
        print()

    print()
    print("Loop 19 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, 0, -1):
            if i%2==0:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()

    print()
    print("Loop 20 :")
    size = 5
    for i in range(size , 0, -1):
        for j in range(i, size+1):
            print(i, end=" ")
        print()

def loop21():
    print("Loop 21 :")
    size = 5
    c=1
    for i in range(1, size+1):
        for j in range(1, i+1):
            print(c , end=" ")
            c = c + 1
        c = c - 1
        print()

def loop22to27():
    print("Loop 22 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    
    print()
    print("Loop 23 :")
    for i in range(1, size+1):
        for j in range(size, i-1, -1):
            print(j, end=" ")
        print()

    print()
    print("Loop 24 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(j, end=" ")
        print()

    print()
    print("Loop 25 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    print()
    print("Loop 26 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(j%2, end=" ")
        print()

    print()
    print("Loop 27 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(i, end=" ")
        print()

def loop28to31():
    print("Loop 28 :")
    for i in range(101, 96, -1):
        for j in range(97, i+1):
            print(chr(j), end=" ")
        print()

    print()
    print("Loop 29 :")
    s = "abcde"
    size = len(s)
    for i in range(1,size+1):
        for j in range(i, size+1):
            print(s[j-1], end=" ")
        print()

    print()
    print("Loop 30 :")
    s = "ABCDE"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(1, i+1):
            print(s[j-1], end=" ")
        print()

    print()
    print("Loop 31 :")
    s = "ABCDE"
    size = len(s)
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(s[j-1], end=" ")
        print()


def loop32to34():
    print("Loop 32 :")
    s = "abcde"
    size = len(s)
    for i in range(1,size+1):
        for j in range(i, size+1):
            print(s[i-1], end=" ")
        print()
    
    print()
    print("Loop 33 :")
    s = "abcde"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(1, i+1):
            print(s[i-1], end=" ")
        print()

    print()
    print("Loop 33 :")
    s = "ABCDE"
    size = len(s)
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(s[i-1], end=" ")
        print()

    print()
    print("Loop 34 :")
    s = "ABCDE"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(1, i+1):
            print(s[i-1], end=" ")
        print()

    
def loop35to38():
    print("Loop 35 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(j%2, end=" ")
        print()

    print()
    print("Loop 36 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(i%2, end=" ")
        print()

    print()
    print("Loop 37 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size+1):
            if(i%2==0):
                print(1,end=" ")
            else:
                print(0,end=" ")
        print()

    print()
    print("Loop 38 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(i, 0, -1):
            if(j%2==0):
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()



def loop39to40():
    print("Loop 39 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(1, i+1):
            print(i, end=" ")
        print()

    print()
    print("Loop 40 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def loop41to45():
    print("Loop 41 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    print()
    print("Loop 42 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

    print()
    print("Loop 43 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size+1):
            print(j, end=" ")
        print()

    print()
    print("Loop 44 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

    print()
    print("Loop 45:")
    size = 5
    for i in range(size, 0, -1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size+1):
            print(j, end=" ")
        print()


def loop46to47():
    print("Loop 46 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i+1):
            print(j%2, end=" ")
        print()

    print()
    print("Loop 47 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i+1):
            if(j%2==0):
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()

def loop48to52():
    print("Loop 48 :")
    size = 69
    for i in range(65, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(65, i+1):
            print(chr(j), end=" ")
        print()

    print()
    print("Loop 49 :")
    s = "abcde"
    size = len(s)
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i+1):
            print(s[j-1], end=" ")
        print()

    print()
    print("Loop 50 :")
    s = "ABCDE"
    size = len(s)
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i+1):
            print(s[i-1], end=" ")
        print()

    print()
    print("Loop 51 :")
    s = "abcde"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size+1):
            print(s[i-1], end=" ")
        print()

    print()
    print("Loop 52 :")
    s = "ABCDE"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size+1):
            print(s[i-1], end=" ")
        print()


def looop54to57():
    print()
    print("Loop 54")
    size = 5
    for i in range(size, 0, -1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

    print()
    print("Loop 55 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(i, size):
            print(end="  ")

        for j in range(i, 0, -1):
            print(j, end=" ")    
        print()

    print()
    print("Loop 56 :")
    size = 5
    for i in range(1, size+1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size+1):
            print(j, end=" ")
        print()

    print()
    print("Loop 57 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(i, size):
            print(end="  ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


def loop58to61():
    print("Loop 58 :")
    size = 5
    for i in range(size, 0, -1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i+1):
            print(i, end=" ")
        print()

    print()
    print("Loop 59 :")
    size = 5
    for i in range(1, size+1):
        for j in range(1, i):
            print(end="  ")
        
        for j in range(i, size+1):
            print(i, end=" ")
        print()

    print()
    print("Loop 60 :")
    size = 5
    for i in range(1, size+1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size+1):
            print(j%2, end=" ")
        print()

    print()
    print("Loop 61 :")
    size = 5
    for i in range(1, size+1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size+1):
            if(i%2==0):
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()


def loop62to65():
    print("Loop 62 :")
    s = "abcde"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(i, size):
            print(end="  ")
        for  j in range(1, i+1):
            print(s[j-1], end=" ")
        print()

    print()
    print("Loop 63 :")
    s = "ABCDE"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i+1):
            print(s[j-1], end=" ")
        print()

    print()
    print("Loop 64 :")
    s = "abcde"
    size = len(s)
    for i in range(1, size+1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size+1):
            print(s[j-1], end=" ")
        print()

    print()
    print("Loop 65 :")
    s = "ABCDE"
    size = len(s)
    for i in range(1, size+1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size+1):
            print(s[j-1], end=" ")
        print()


def loop66to71():
    print("Loop 66 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i+1, size+1):
            print(end=" ")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

    print()
    print("Loop 67 :")
    s = "abcde"
    size = len(s)
    for i in range(1, size+1):
        for j in range(i+1, size+1):
            print(end=" ")
        for j in range(1, i+1):
            print(s[j-1], end=" ")
        print()

    print()
    print("Loop 68 :")
    size = 5
    for i in range(1, size+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

    print()
    print("Loop 69 :")
    size = 5
    for i in range(1, size+1):
        for j in range(i+1, size+1):
            print(end=" ")
        for j in range(1, i+1):
            print("*", end=" ")
        print()

    print()
    print("Loop 70 :")
    s = "ABCDE"
    size = len(s)
    for i in range(1, size+1):
        for j in range(i+1, size+1):
            print(end=" ")
        for j in range(1, i+1):
            print(s[j-1], end=" ")
        print()
    
    print()
    print("Loop 71 :")
    s = "abcde"
    size = len(s)
    for i in range(size, 0, -1):
        for j in range(1+1, i+1):
            print(end=" ")
        for j in range(size, i-1, -1):
            print(s[j-1], end=" ")
        print()

loop66to71()
