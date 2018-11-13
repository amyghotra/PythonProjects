import turtle

def welcomeMessage():
    print()
    print("Welcome to our herd of turtles demonstration!")
    print()

def getInput():
    n = eval(input("Please enter the number of turtles: "))
    return n


def setUpScreen():
    w = turtle.Screen()
    w.bgcolor("pink")
    return w

def setUpTurtles(n):
    tList = []
    #Create turtles:
    for i in range(n):
        t = turtle.Turtle()
        t.shape("turtle")       #Make the turtle appear turtle-shaped
        tList.append(t)

    #Change their color from the blue default and default direction
    for i in range(n):
        tList[i].color(0,0,i/(2*n)+.5)
        tList[i].right(i*360/n)

    return tList

def moveForward(tList):
    for t in tList:
        t.forward(30)

def stamp(tList):
    for t in tList:
        t.stamp()

def main():
    welcomeMessage()            #Writes a welcome message to the shell
    numTurtles = getInput()     #Ask for number of turles
    w = setUpScreen()           #Set up a green turtle window
    turtleList = setUpTurtles(numTurtles) #Make a list of turtles, different colors
    for i in range(10):
        moveForward(turtleList) #Move each turtle in the list forward
        stamp(turtleList)       #Stamp where the turtle stopped


if __name__ == "__main__":
    main()

#basic outline of program (use comments for guidance):
#def welcomeMessage():
#this function should welcome the user to the program
    #Empty placeholder until function is defined
#    return()

#def getInput():
#this function should ask the user for the number of turtles
    #Empty placeholder until function is defined
#    return()

#def setUpScreen():
#set up the turtle window and color the background; background color = "BGCOLOR"
    #Empty placeholder until function is defined
#    return()

#def setUpTurtles(num):
#set up a list of turtles:
    #cerate a liste of turtles
    #make each turtle appear turtle-shaped
    #change the color of it and the direction it's facing
    #return the list
    #Empty placeholder until function is defined
#    return()

#def moveForward(tList):
#move turtles forward using a for loop
    #Empty placeholder until function is defined
#    return()

#def stamp(tList):
    #Empty placeholder until function is defined
#    return()

#def main():
#    welcomeMessage()            #Writes a welcome message to the shell
#    numTurtles = getInput()     #Ask for number of turles
#    w = setUpScreen()           #Set up a green turtle window
#    turtleList = setUpTurtles(numTurtles) #Make a list of turtles, different colors
#    for i in range(10):
#        moveForward(turtleList) #Move each turtle in the list forward
#        stamp(turtleList)       #Stamp where the turtle stopped


#if __name__ == "__main__":
#    main()

