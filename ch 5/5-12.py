def is_rightangled(side1,side2,side3):
    sq_1 = side1 ** 2
    sq_2 = side2 ** 2
    sq_3 = side3 ** 2
    if sq_1 > sq_2 and sq_1 > sq_3:
        return sq_2 + sq_3 == sq_1
    elif sq_2 > sq_1 and sq_2 > sq_3:
        return sq_1 + sq_3 == sq_2
    elif sq_3 > sq_2 and sq_3 > sq_1:
        return sq_1 + sq_2 == sq_3

print(is_rightangled(6,8,10))

