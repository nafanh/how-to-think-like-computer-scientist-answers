def sum_of_squares(xs):
    sum = 0
    if len(xs) == 0:
        return sum
    for num in xs:
        sum += (num **2)
    return sum




import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)

test_suite()