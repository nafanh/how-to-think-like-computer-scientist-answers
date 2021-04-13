import unit_tester

def myreplace(old,new,s):
    if old == " ":
        return new.join(s.split())
    return new.join(s.split(old))


unit_tester.test(myreplace(",", ";", "this, that, and some other thing") ==
                         "this; that; and some other thing")
unit_tester.test(myreplace(" ", "**",
                 "Words will now      be  separated by stars.") ==
                 "Words**will**now**be**separated**by**stars.")