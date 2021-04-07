import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)




def sum_before_even(num_list):
    sum = 0
    for num in num_list:
        if num % 2 == 0:
            break
        sum += num
    return sum
def test_suite():

    test(sum_before_even([2,3,2]) == 0)
    test(sum_before_even([0,3,2]) == 0)
    test(sum_before_even([3,3,3]) == 9)
    test(sum_before_even([3,2,3,2]) == 3)


test_suite()