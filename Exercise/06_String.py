# Check whether the string is Palindrome or not

def palinrome(s):
    start = 0
    mid = len(s)//2
    last = len(s)-1

    while(start < mid):
        if s[start] == s[last]:
            start+=1
            last-=1
        else:
            return False
    return True


s = "racecar"
print("Palindrome" if palinrome(s) else "Not Palindrome")