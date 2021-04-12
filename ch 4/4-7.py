'''
Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and including n.
So sum_to(10) would be 1+2+3...+10 which would return the value 55.
'''

def sum_to(n):
    sum = 0
    for num in range(1,n+1):
        sum += num
    return sum

print(sum_to(10))