def num_digits(n):
    num_dig = 0
    if n == 0:
        return 1
    while n != 0:
        n = int(n / 10)
        num_dig += 1
    return num_dig



import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)



test_suite()