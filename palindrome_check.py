# check whether the input string is a palindrome or not

def palindrome_check(string):
    string_value = string.lower()

    if(string_value == string_value[::-1]):
        print("The String is a palindrome")
    else:
        print("The string is not palindrome")

input_string = input("Enter a string to check whether the string is palindrome or not:")

palindrome_check(input_string)