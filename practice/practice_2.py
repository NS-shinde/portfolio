
# #factors of number program 
# num = 12

# for i in range(1,num+1):
#     if num % i == 0:
#         print(i) 



#find string palindrome or not palindrome
# a = input('enter your string: ')
# b = a[::-1]#sling 
# print(b)
# if a==b:
#     print('it is a palindrome string')
# else:
#     print('it is not a palindrome string')



# display the calendar
import calendar
year = int(input('year:' ))
month = int(input('month:'))

calendar = calendar.month(year)
print(calendar)