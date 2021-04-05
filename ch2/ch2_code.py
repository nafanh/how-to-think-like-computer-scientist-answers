'''
1) Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print.
'''

a = 'All'
b = ' work'
c = ' and'
d = ' no'
e = ' play'
f = ' makes'
g = ' Jack'
h = ' a'
i = ' dull'
j = ' boy'

print(a+b+c+d+e+f+g+h+i+j)


'''
Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.
'''
print(6*(1-2))

'''
Assign a value to bruce so that bruce + 4 evaluates to 10.

'''
bruce = 6
bruce = bruce + 4

'''Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, 
and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that the 
money will be compounded for. Calculate and print the final amount after t years. '''

years = int(input("Enter number of years: "))
amount = 10000*(1 + (0.08/12))**(12*years)
print("Final amount after {} years: {:.2f}".format(years,amount))


'''You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm 
go off? (Hint: you could count on your fingers, but this is not what we’re after. If you are tempted to count on your 
fingers, change the 51 to 5100.) 
'''
hour_remaining = 51 % 24
time_alarm = 2 + hour_remaining
if time_alarm <= 12:
    print("Alarm goes off at {} PM".format(time_alarm))
else:
    print("Alarm goes off at {} AM".format(time_alarm-12))
'''
Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), 
and ask for the number of hours to wait. Your program should output what the time will be on the clock when the alarm 
goes off. '''

time_hours = int(input("Input time in hours: "))
time_wait = int(input("Input number of hours to wait: "))
time_alarm = (time_hours + time_wait) % 24
if time_alarm >= 12:
    if time_alarm == 12:
        print("The alarm will go off at 12 PM")
    else:
        print("The alarm will go off at {} PM".format(time_alarm-12))
else:
    if time_alarm == 0:
        print("The alarm will go off at 12 AM")
    else:
        print("The alarm will go off at {} AM".format(time_alarm))
