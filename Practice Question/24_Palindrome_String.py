# Check the string whether it is palindrome or not

string = input("Enter string here :")
reverse = string[::-1]

if(string == reverse):
    print(string, " is a Palindrome String")
else:
    print(string, " is NOT a Palindrome String")