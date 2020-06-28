#Write a program that repeatedly prompts a user
#for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try / except and put out an appropriate message and ignore the number.



def computepay(h,r):
    if h > 40:
        total = (((1.5 * r) * (h-40)) + (40 * r))
    else:
        total = h * r

    return total

hours = input('Hours')
h = float(hours)
rate = input('Rate')
r = float(rate)

total = computepay(h,r)
print ("Pay",total)


