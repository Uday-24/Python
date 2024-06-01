# Definition :- Find ASCII value of given character using built in function

try:
    char = input("Enter a charcter : ")
    print(f"ASCII of {char} = {ord(char)}")
except:
    print("You might have entered more than one character, please enter only single character")