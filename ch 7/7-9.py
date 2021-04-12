def print_triangular_numbers(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
        print(i,'\t',sum)

print_triangular_numbers(10)