def add_vectors(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

def scalar_mult(s,v):
    for (idx,val) in enumerate(v):
        v[idx] = val * s
    return v

def dot_product(u,v):
    sum = 0
    for i in range(len(u)):
        sum += u[i] * v[i]
    return sum

def cross_product(u,v):
    first = (u[1]*v[2]) - (u[2]*v[1])
    second = (u[2]*v[0]) - (u[0] * v[2])
    third = (u[0] * v[1]) - (u[1] * v[0])
    c = [first,second,third]
    return c
import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    print()

    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    print()

    test(dot_product([1, 1], [1, 1]) == 2)
    test(dot_product([1, 2], [1, 4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    print()

    test(cross_product([3,0,2],[-1,4,2]) == [-8,-8,12])
    test(cross_product([3,4,5],[3,2,1]) == [-6,12,-6])
    test(cross_product([6,8,5],[4,2,3]) == [14,2,-20])


test_suite()