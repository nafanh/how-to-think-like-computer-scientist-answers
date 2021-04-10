

def count(sub,str):
    count = 0
    for i in range(len(str)-len(sub)+1):
        if sub in str[i:i+len(sub)]:
            count += 1
    return count

def remove(sub,str):
    if str.find(sub) == -1:
        return str
    return str[:str.find(sub)] + str[str.find(sub) + len(sub):]

def remove_all(sub,str):
    occur = count(sub,str)
    b = str
    for i in range(occur):
        b = remove(sub,b)
    return b


import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")

test_suite()