# Convert Lowercase Characters by Uppercase and Vice-Versa

char = input("Enter character(s) : ")

try:
    if ord(char) >= 65 and ord(char) <= 90:
        print(char.lower())
    elif ord(char) >= 97 and ord(char) <= 122:
        print(char.upper())
    else:
        print("Please enter only alphabet")
except:
    print("Please enter only single alphabet")