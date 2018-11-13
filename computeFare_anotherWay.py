def computeFare(zone , ticketType):
    computeFare = ""
    if zone == 1 and ticketType == "peak":
        computeFare = "6.75"
        print("The fare is " , computeFare)
    elif zone == 1 and ticketType == "off-peak":
        computeFare = "5.00"
        print("The fare is " , computeFare)
    elif zone == 1 and ticketType == "senior":
        computeFare = "3.35"
        print("The fare is " , computeFare)
    elif zone == 2 and ticketType == "peak":
        computeFare = "7.50"
        print("The fare is " , computeFare)
    elif zone == 2 and ticketType == "off-peak":
        computeFare = "5.75"
        print("The fare is " , computeFare)
    elif zone == 2 and ticketType == "senior":
        computeFare = "3.75"
        print("The fare is " , computeFare)
    elif zone == 3 and ticketType == "peak":
        computeFare = "9.25"
        print("The fare is " , computeFare)
    elif zone == 3 and ticketType == "off-peak":
        computeFare = "7.00"
        print("The fare is " , computeFare)
    elif zone == 3 and ticketType == "senior":
        computeFare = "4.50"
        print("The fare is " , computeFare)
    else:
        return computeFare
    return computeFare

x = int(input("input zone"))
y = str(input("peak/off-peak/senior"))
computeFare(x,y)
