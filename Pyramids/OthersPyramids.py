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