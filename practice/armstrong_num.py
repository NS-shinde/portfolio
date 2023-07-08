num = int(input('enter your num:')) #8891
order = len(str(num))
copy_num = num
sum = 0
while(num>0):
    digit = num % 10
    sum += digit **order
    num= num//10
    # print(sum)
    
    
if (sum == copy_num):
        print('armstrong number')
else:
        print('it is not an armstrong')