# Check whether the string is Palindrome or not

# Method 1
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
print(f"{s} is Palindrome" if palinrome(s) else f"{s} is Not Palindrome")


# Method 2
s = "malayalam"         # s stands for string
rs = s[::-1]            #rs stands for reversed stringr

print(f"{s} is Palindrome" if s==rs else f"{s} is Not Palindrome")