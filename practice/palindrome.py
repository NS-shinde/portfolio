def palindrome(s):
    temp = s[::-1] # temp = ''.join(reversed(s)) #using inbuild funtion and join 
    if temp == s:
        print('its palindrome string')
    else:
        print( "it is not palindrome string")
    
    
s = 'nagesh'      
# palindrome(s)


#by using indexing / using for loop 
def  palindrome2(s):
    n = len(s)
    for i in range(n):
        if s[i] == s[n-i-1]:
            return True
        return False
    
s = 'nitin'
print(palindrome2(s)) 


def palindrome3(s):
    n = len(s)
    for i in range(n):
        if s[i] == s[n-i-1]:
            return True
        else: False

s = 'nitin'
print(palindrome3(s))


#by using reversed and join 
def palindrome4(s):
    temp = ''.join(reversed(s))
    if temp == s:
        print('it is palindrome string ...')
    else: print('it is not palindrome string')
    
    
s = 'madam'
palindrome4(s)