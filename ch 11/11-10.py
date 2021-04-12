

def replace(s,old,new):
    wrd_list = s.split(old)
    return new.join(wrd_list)





import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)




def test_suite():
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")

    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") ==
        "I love spam! Spam is my favorite food. Spam, spam, yum!")

    test(replace(s, "o", "a") ==
        "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

test_suite()