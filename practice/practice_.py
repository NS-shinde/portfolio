# num = 12

# for i in range(2, num):
#     if num % 2 == 0:
#         print('NOT PRIME ')
#         break
#     else:
#         print('its prime')
#         break


# using third variable
# x = 12
# y = 13

# temp = x
# # print('value of x, ', temp)

# x = y
# print('value of x, ', x)

# y  = temp
# print('value of y ', y)


# x = 10
# y = 12

# x, y = y , x
# print(x)
# print(y)


# km = int(input('enter kilometers:'))

# miles = km * (0.621371)

# print(km,'kms in miles will be  :',miles)


# num = int(input(':'))

# if num == 0:
#     print('it is zero')

# elif num > 0:
#     print('it is positive number')

# else:
#     print('-')



# num = 21

# if num % 2 == 0:
#     print('it is even number')
# else:
#     print('it is odd number')


# num1 = 12
# num2 = 56
# num3 = 34

# if num1 > num2 & num1 >num3:
#     print(num1)
# elif num2 >  num3:
#     print(num2)
# else:
#     print(num3)


# num = 11

# for i in range(2, num):
#     if num % i == 0:
#         print('its not prime')
#     else:
#         ('it is prime')

# celsius  = int(input('enter temp in celsius:'))
# fahrenheit = (celsius * (9/5)) + 32
# print(fahrenheit)



# num = int(input('enter your number:'))
# fact = 1

# if num < 0:
#     print('factorial of less than zero does not exist')
# if num == 0:
#     print('factorial of zero is', 1)
# if num > 0 :
#     for i in range(1, num +1):
#         fact = fact * i
        
# print(fact)



# solution using recursion

# def fact(a):
#     if a == 0:
#         return 1
#     else:
#         return ((a)*fact(a-1))
  
  
# num = 5    
# result = fact(num)
# print(result)    
    

    
# python program to generate random numbers

# import random

# num = random.randint(0, 10)
# print(num)




# display multiplication table
# num = 7

# for i in range(1, 11):
#     print(num, "x", i, '=', num*i)
    
    
    
# n = 7 
# i = 1

# while i<= 10:
#     print(n, "x", i, "=", n * i)
#     i = i + 1



# fiboncci sequence

# a = 0 
# b = 1

# num = 7

# if num ==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range (2, num+1):
#         c = a + b
#         a = b 
#         b = c
#         print(c)


         
         
 
 
 
# my_list = []

# if not my_list:#usig boolean
#     print("the list i empty")        


# list = []

# if len(list) == 0:#using len fun
#     print('list is empty')

# using squere brackets
# list = [77,]
# if list == []:
#     print("list is empty")
# else:
#     print("list is not empty")




# marks = {'john':23,  'lisa': 56, 'sid': 48}
# print(marks)

# sv = sorted(marks.items(), key = lambda x: x[1])#1 is value of dictionary
# print(sv)



# # using sorted functions
# v = sorted(marks.values())
# print(v)






# copy all data if any one connect my laptop    
# import shutil
# import os

# def copy_usb_data(source_dir, destination_dir):
#     # Copy all files and directories from the USB device to the destination directory
#     shutil.copytree(source_dir, destination_dir)
#     print(f"Successfully copied all data from {source_dir} to {destination_dir}")

# # Specify the source directory (USB device) and destination directory
# source_directory = "/path/to/usb/device"
# destination_directory = "/path/to/destination/folder"

# # Check if the source directory exists (i.e., USB device is connected)
# if os.path.exists(source_directory):
#     copy_usb_data(source_directory, destination_directory)
# else:
#     print("No USB device connected.")



# from shutil import copyfile
# copyfile("C:/Users/nagesh shinde/Desktop/gmwar_w.txt", "C:/Users/nagesh shinde/Desktop/interview.txt")



# # how to remove punctuation from string
# punc = ''', . ? ! : ; - — – ' " ‘ ’ “ ” ( ) [ ] { } / \ | & @ # $ % * ^ _ ~ < > = + ` ...'''

# string = input('enter anythig here:')
# empty_str = ''

# for i in string:
#     if i not in punc:
#         empty_str = empty_str + i 
        
# print(empty_str)



# # python program to add to matrics
# A = [[4,8,9],
#      [4,5,7],
#      [1,3,4]]
# B = [[3,6,9],
#      [3,2,1],
#      [9,7,6]]

# result = [[0,0,0],
#           [0,0,0],
#           [0,0,0]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         result[i][j] = A[i][j] + B[i][j]
        
        
# print(result)
# for r in result:
#     print (r)



# num = 5

# if num < 0:
#     print()


