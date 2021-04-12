def words_before_same(word_list):
    word_count = 0
    for word in word_list:
        word_count += 1
        if word == "sam":
            break
    return word_count

import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():

    test(words_before_same(['a','bb','fadsfa','sam']) == 4)
    test(words_before_same(['a','bb','fadsfa','sam','adsf','323']) == 4)
    test(words_before_same(['sam', 'bb', 'fadsfa', 'a']) == 1)
    test(words_before_same(['a', 'bb', 'fadsfa', 'sf']) == 4)


test_suite()