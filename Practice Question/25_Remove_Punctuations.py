# Remove Punctuations From the String

punc = '''!@#$%^&*()_-=+[]{};':",.<>/?'''
string = input("Enter string here : ")
for i in string:
    if i not in punc:
        print(i, end="")