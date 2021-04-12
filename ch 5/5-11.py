def is_rightangled(side1,side2,side3):
    sum = side1 ** 2 + side2 ** 2
    sq_longest = side3 ** 2
    return sum == sq_longest

print(is_rightangled(6,3,10))