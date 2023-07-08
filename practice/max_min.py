def find_max_min(numbers):
    if not numbers:
        return None, None
    else:
        max_num = min_num = numbers[0]
        for num in numbers:
            if num  > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        return max_num, min_num

numbers = [5, 3, 9, 2, 7]
max_num, min_num = find_max_min(numbers)
print('max:', max_num)
print('min:', min_num)