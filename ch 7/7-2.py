def sum_even(num_list):
    even_sum = 0
    for num in num_list:
        if num % 2 == 0:
            even_sum += num
    return even_sum

print(sum_even([1,2,3,4,5,6,7,8,9,10]))