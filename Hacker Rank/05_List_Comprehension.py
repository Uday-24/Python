if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # It is normal zindagi
    # list_ = []
    # for i in range(0, x+1):
    #     for j in range(0, y+1):
    #         for k in range(0, z+1):
    #             if(i+j+k !=n ):
    #                 list_.append([i, j, k])

    # It is mentos zindagi
    list_ = [[i,j,k] for i in range(0, x+1) for j in range(0,y+1) for k in range (0,z+1) if i+j+k !=n ]
    print(list_)