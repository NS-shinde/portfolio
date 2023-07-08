# my_list = [4, 2, 1, 3]
#
# my_list.sort(reverse=True)
#
# print('using sort method',my_list)
#
# sorted_list = sorted(my_list)
# print('using sorted funtion',sorted_list)




def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]

my_list = [4, 2, 1, 3]
sort_list(my_list)
# print(my_list)





def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                lst[i],lst[j]=lst[j],lst[i]

my_list = [12, 33, 3, 2, 0]
sort_list(my_list)
print(my_list)