# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr)
    uniq = list(set(arr)) #Removing duplicates
    print(uniq[len(uniq)-2])