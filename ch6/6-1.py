import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def turn_clockwise(dir):
    if dir == "N":
        return "E"
    elif dir == "E":
        return "S"
    elif dir == "S":
        return "W"
    elif dir == "W":
        return "N"
    return None

def day_name(num):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if num < len(days):
        return days[num]
    return None

def day_num(day):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if day in days:
        return days.index(day)
    return None

def day_add(day_name,delta):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if day_name in days:
        day_num = days.index(day_name)
        return_day = days[(day_num + delta) % 7]
        return return_day
    return None

def days_in_month(month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    months = ['January','February','March','April','May','June','July',
              'August','September','October','November','December']
    if month in months:
        return month_days[months.index(month)]
    return None

def to_secs(h,m,s):
    total = (h*3600) + (m*60) + s
    if total:
        return int(total)
    return None

def hours_in(secs):
    hours =  secs // 3600
    if hours:
        return hours
    return None

def minutes_in(secs):
    minutes = int(60 * ((secs / 3600) - hours_in(secs)))
    if minutes:
        return minutes
    return None

def seconds_in(secs):
    seconds = secs % 60
    if seconds:
        return seconds
    return None

def compare(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    return -1

def hypotenuse(a,b):
    return (a ** 2 + b **2)**0.5

def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

def intercept(x1,y1,x2,y2):
    # y = mx + b
    m = slope(x1,y1,x2,y2)
    return (y1 - m * x1)


def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n%2 == 1

def is_factor(f,n):
    return n % f == 0

def is_multiple(dividend,divisor):
    return is_factor(divisor, dividend)

def f2c(t):
    c = 5/9 * (t-32)
    return(round(c))

def c2f(t):
    f = 9/5 * t + 32
    return round(f)
def test_suite():
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)

    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)

    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")

    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")

    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)

    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)

    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433, 0, 0) == 8758)

    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)

    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)

    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)

    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)

    test(is_even(2) == True)
    test(is_even(3) == False)
    test(is_even(15) == False)
    test(is_even(22) == True)

    test(is_odd(2) == False)
    test(is_odd(3) == True)
    test(is_odd(15) == True)
    test(is_odd(22) == False)

    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))

    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))

    test(f2c(212) == 100)  # Boiling point of water
    test(f2c(32) == 0)  # Freezing point of water
    test(f2c(-40) == -40)  # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)

    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)

test_suite()

