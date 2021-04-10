
def reverse(str):
    rev = ""
    for i in range(len(str)-1,-1,-1):
        rev += str[i]
    return rev

def is_palindrome(str):
    return str == reverse(str)



import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))    # Is an empty string a palindrome?

test_suite()