def is_prime(n):
    for i in range(2,n//2 + 1):
        if n % i == 0:
            return False
    return True




import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():

    test(is_prime(3) == True)
    test(is_prime(5) == True)
    test(is_prime(12) == False)
    test(is_prime(36) == False)
    test(is_prime(11) == True)
    test(not is_prime(35) == True)
    test(is_prime(19911121))



test_suite()