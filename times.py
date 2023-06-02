n=int(input("the"))
if n < 1582:
	print("Not within the Gregorian calendar period")
else:
    if n%4!=0:
	    print("Common year")
    elif n%100!=0:
	    print("Leap year")
    elif n%400!=0:
    	print("Common year")
    else:
	    print("Leap year")