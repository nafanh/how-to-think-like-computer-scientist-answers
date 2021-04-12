
def count(sub,str):
    count = 0
    for i in range(len(str)-len(sub)+1):
        if sub in str[i:i+len(sub)]:
            count += 1
    return count



import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)
    # test(is_palindrome(""))    # Is an empty string a palindrome?

test_suite()