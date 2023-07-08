str1 = 'Sky is blue'
print(' '.join(str1.split()[::-1]))
# n_str = ' '.join(r_list)
# print(r_list)

list = [1,2,2,3,3,4,5,5,5,6,6]
new_list = []
for num in list:
    if list.count(num)==1:
        new_list.append(num)

print(new_list)
# using list comprehension
lst = [num for num in list if list.count(num)==1]
print(lst)


mystr = 'a,a,a,b,b,c,c,c'
mylist=mystr.split(',')
visited = []
# print(mylist)
for ch in mylist:
    if ch not in visited:
