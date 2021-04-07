def num_even_digits(n):
    num_even = 0
    if n == 0:
        return 1
    while n != 0:
        dig = n % 10
        if dig % 2 == 0:
            num_even += 1
        n = n // 10
    return num_even


import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)


test_suite()