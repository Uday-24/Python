# 1 Simple Pyramid   #2 Flipped Simple Pyramid   #3 Inverted Pyramid    #4 Flipped Inverted Pyramid  
# *                 #         *                  # * * * * *            # * * * * *
# * *               #       * *                  # * * * *              #   * * * *
# * * *             #     * * *                  # * * *                #     * * *
# * * * *           #   * * * *                  # * *                  #       * * 
# * * * * *         # * * * * *                  # *                    #         * 


def loop1to4():
    print("1: Simple Pyramid")
    size = 5
    for i in range(1, size+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
    
    print("2: Flipped Simple Pyramid")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size):
            print(end="  ")
        for j in range(1, i+1):
            print("*", end=" ")
        print()
    
    print("3: Inverted Pyramid")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size+1):
            print("*", end=" ")
        print()

    print("4: Flipped Inverted Pyramid")
    size = 5
    for i in range(1, size+1):
        for j in range(1, i):
            print(end="  ")
        for j in range(i, size+1):
            print("*", end=" ")
        print()

loop1to4()

# 5 Triangle        #6 Inverted Triangle      #7 Half Diamond        #8 Flipped Half Diamond 
#     *                  * * * * *                  *                             *
#    * *                  * * * *                   * *                         * *
#   * * *                  * * *                    * * *                     * * *
#  * * * *                  * *                     * *                         * *
# * * * * *                  *                      *                             *

def loop5to8():
    print()
    print("5: Triangle")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size):
            print(end=" ")
        for j in range(1, i+1):
            print("*", end=" ")
        print()

    print()
    print("6: Inverted Triangle")
    for i in range(1, size+1):
        for j in range(1, i):
            print(end=" ")
        for j in range(i, size+1):
            print("*", end=" ")
        print()

    print()
    print("7: Half Diamond Pattern")
    n = 5
    size = n // 2 + 1
    for i in range(1, size+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
    size -= 1
    for i in range(1, size+1):
        for j in range(i, size+1):
            print("*", end=" ")
        print()

    print()
    print("8:Flipped Half Diamond Pattern")
    n = 9
    size = n // 2 + 1
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(end="  ")
        for j in range(1, i+1):
            print("*", end=" ")
        print()
    size -= 1
    for i in range(1, size+1):
        for j in range(1, i+2):
            print(end="  ")
        for j in range(i, size+1):
            print("*", end=" ")
        print()
    
loop5to8()



# 9 Diamond Pattern         #10 Hourglass Pattern           #11 Number Pyramid          #12 Continuous Number Pyramid
#     *                            * * * * *                       1                           1
#    * *                            * * * *                        2 2                         2 3
#   * * *                            * * *                         3 3 3                       4 5 6
#  * * * *                            * *                          4 4 4 4                     7 8 9 10
# * * * * *                            *                           5 5 5 5 5                   11 12 13 14 15
#  * * * *                            * *
#   * * *                            * * *
#    * *                            * * * *
#     *                            * * * * *
def loop9to12():
    print()
    print("9: Diamond pattern")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size):
            print(end=" ")
        for j in range(1, i+1):
            print("*", end=" ")
        print()
    size-=1
    for i in range(1, size+1):
        for j in range(1, i+1):
            print(end=" ")
        for j in range(i, size+1):
            print("*", end=" ")
        print()

    print()
    print("10: Hourglass Pattern")
    size = 5
    for i in range(1, size+1):
        for j in range(1, i+1):
            print(end=" ")
        for j in range(i, size+1):
            print("*", end=" ")
        print()
    size-=1
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(end=" ")
        for j in range(1, i+2):
            print("*", end=" ")
        print()

    print()
    print("11: Number Pyramid")
    size = 5
    for i in range(1, size+1):
        for j in range(1, i+1):
            print(i, end=" ")
        print()

    print()
    print("12: Continuous Number Pyramid")
    size = 5
    k = 1
    for i in range(1, size+1):
        for j in range(1, i+1):
            print(k, end=" ")
            k+=1
        print()

loop9to12()


# 13 Rotated Number Pyramid        #14 Palindrome Triangle        #15 Alphabet Pyramid        #16 Continuous Alphabet Pyramid
#         1                                  1                          A                           A
#       2 3                                2 3 2                        B B                         B C
#     3 4 5                              3 4 5 4 3                      C C C                       D E F
#   4 5 6 7                            4 5 6 7 6 5 4                    D D D D                     G H I J

def loop13to16():
    print()
    print("13: Rotated Number Pyramid")
    size = 4
    k = 1
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(end="  ")
        l = k
        for j in range(1, i+1):
            print(l, end=" ")
            l += 1
        k+=1
        print()

    print()
    print("14: Palindrome Triangle")
    size = 4
    k=1
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(end="  ")
        l = k
        for j in range(1, i):
            print(l, end=" ")
            l += 1
        k+=1
        for j in range(1, i+1):
            print(l, end=" ")
            l-=1
        print()

    print()
    print("15: Alphabet Pyramid")
    size = 4 + 65
    for i in range(65, size+1):
        for j in range(65, i+1):
            print(chr(i), end=" ")
        print()

    print()
    print("16: Continuous Alphabet pyramid")
    size = 4
    k=65
    for i in range(1, size+1):
        for j in range(1, i+1):
            print(chr(k), end=" ")
            k+=1
        print()

loop13to16()


# 17 Rhombus Pattern
# * * * * *
#  * * * * *
#   * * * * *
#    * * * * *
#     * * * * *
def loop17():
    print()
    print("17: Rhombus Pattern")
    sized = 5
    for i in range(1, sized+1):
        for j in range(1, i):
            print(end=" ")
        for j in range(1, sized+1):
            print("*", end=" ")
        print()

loop17()


# 18 Hollow Square Pattern
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
def loop18():
    print()
    print("18: Hollow Square Pattern")
    size = 5
    for i in range(1, size+1):
        for j in range(1, size+1):
            if i==size or i==1 or j==size or  j==1:
                print("*", end=" ")
            else:
                print(end="  ")
        print()

loop18()


# 19 Hollow Full  Pyramid
#     *
#    * *
#   *   *
#  *     *
# * * * * *

def loop19():
    print()
    print("19: Hollow Full Pyramid")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size+1):
            print(end=" ")
        for j in range(1, i+1):
            if j==1 or i==5 or j==i:
                print("*", end=" ")
            else:
                print(end="  ")
        print()

loop19()


# 20 Hollow Inverted  Pyramid
# * * * * *
#  *     *
#   *   *
#    * *
#     *

def loop20():
    print()
    print("20: Hollow Inverted Pyramid")
    size = 5
    for  i in range(1, size+1):
        for j in range(1, i):
            print(end=" ")
        for j in range(i, size+1):
            if i==1 or j==i or j==size:
                print("*", end=" ")
            else:
                print(end="  ")
        print()

loop20()


# 21 Hollow Diamond Pyramid
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

def loop21():
    print()
    print("21: Hollow Diamond Pyramid")
    size = 5
    for i in range(1, size+1):
        for j in range(i, size):
            print(end=" ")
        for j in range(1, i+1):
            if j==i or j==1:
                print("*", end=" ")
            else:
                print(end="  ")
        print()
    size-=1
    for i in range(1, size+1):
        for j in range(1, i+1):
            print(end=" ")
        for j in range(i, size+1):
            if j==i or j==size:
                print("*", end=" ")
            else:
                print(end="  ")    
        print()

loop21()