# my_list = [1, 2, 3, 4, 5]
# total_sum = 0

# for num in my_list:
#     total_sum = num + total_sum
# print(total_sum)

#
#
# my_list = [5, 12, 9, 3, 21, 7]
# largest = my_list[0]



# for num in my_list:
#     if num > largest:
#         largest = num
        
        
# print(largest)





# char = input('enter your string:')
# print('ther ASCII value is ',char, ord(char))


# #factor of numbers
# num = int(input('factor:'))
# for i in range(1, num+1):
#     if num % i == 0:
#         print(i)


# n = int(input('enter your number:'))
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)


# decimal = int(input('enter your decimal:'))
# print(bin(decimal))#prepix 0b
# print(oct(decimal))#0o
# print(hex(decimal))#0h



# my_list = [1, 2, 3, 4, 5]
# # my_list.reverse()
# reverse_list = my_list[::-1]
# # print(my_list)
# print(reverse_list)



# my_list = [1, 2, 3, 4, 5]
# reverse_list = my_list[::-1]
# print(reverse_list)


# my_list = [1, 2, 3, 4, 5]
# reversed_list = []

# for i in range(len(my_list)-1,-1, -1,):
#     reversed_list.append(my_list[i])
    
# print(reversed_list)
# # my_list.reverse()
# # print(my_list)

#using sort methon..
# my_list = [5, 2, 9, 1, 3]
#my_list.sort()
# # print(my_list)
# # sorted_list=sorted(my_list)#sort list using sorted function
# # print(sorted_list)

# # element = 9
# index = my_list.index(9)
# # print(index)

# length = len(my_list)
# # print(length)
# # my_list.remove(9)
# # print(my_list)
# my_list.insert(0, 45)
# my_list.append(88)
# # my_list.append(29)
# print(my_list)




# list = [1, 2 , 33, 55, 66, 77,4,6]
# # list.sort()
# # print(list)
# # print(list[-2])

# list.remove(max(list))
# list.remove(min(list))
# print(list)





# def reverse_integer(num):
#     reverse_num = int(str(num)[::-1])
#     return reverse_num

# number = 12345
# print(reverse_integer(number))
#
# def reverse_integer(num):
#    reverse_num = int(str(num)[::-1] )
#    return reverse_num
#
# number = 123456678
# reverse_number= reverse_integer(number)
# print(reverse_number)