# def is_palindrome(string):
#     string = string.lower()  # Convert the string to lowercase
#     reversed_string = string[::-1]  # Reverse the string
#     return string == reversed_string
#
# # Test cases
# print(is_palindrome("radar"))  # Output: True
# print(is_palindrome("python"))  # Output: False

def palindrome(string):

    string = string.lower()
    reverse_s = string[::-1]
    if string == reverse_s:
        print('it is palindrome string ')
    else:
        print('not palindrome')


string = input('enter your string :')
palindrome(string)