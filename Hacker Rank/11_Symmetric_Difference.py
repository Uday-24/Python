if __name__ == '__main__':
    eng = int(input())
    eng_roll = set(map(int, input().split()))
    fch = int(input())
    fch_roll = set(map(int, input().split()))
    
    print(len(eng_roll.symmetric_difference(fch_roll)))