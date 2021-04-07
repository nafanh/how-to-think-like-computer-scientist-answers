def sum_neg(num_list):
    neg_sum = 0
    for num in num_list:
        if num < 0:
            neg_sum += num
    return neg_sum

print(sum_neg([-3,45,32,-345,35,67,34,-31]))