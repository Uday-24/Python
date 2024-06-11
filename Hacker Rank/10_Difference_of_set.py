if __name__ == '__main__':
    eng = int(input())
    eng_roll = set(map(int, input().split()))
    fch = int(input())
    fch_roll = set(map(int, input().split()))
    
    diff = eng_roll.difference(fch_roll)
    print(len(diff))
