def odd_num(num_list):
    odd_count = 0
    for num in num_list:
        if num % 2 == 1:
            odd_count += 1
    return odd_count


print(odd_num([1,2,3,4,5,6,7,8,9,10]))