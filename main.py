# By Kai Ferrer

from turtlesetup_plot import *

#Asks the user how many data points they want to enter
points = int(input("How many data points do you want to plot? "))

#Creates a list for data points entered
years = []
birthRates = []

#Adjusts turtle size for marking data points
t.shape("circle")
t.shapesize(0.25, 0.25)

if points > 0: #Error checks that data points entered by user are a positive integer [STEP 1]
    for i in range(points):
        xValue = int(input("What is the x coordinate of data point {}? ".format(i+1)))
        
        if xValue < 1910 or xValue > 2022: #Checks if year entered is NOT within range. If so, "error" is outputted. [STEP 1]
            print("Error.")
            t.hideturtle()
            screen.exitonclick()
        else:
            years.append(int(xValue)) #If year is within range, the entered year is added to a list

            if(years != sorted(years)): #Checks if all years entered are NOT in chronological order. If so, "error" is outputted. [STEP 1]
                print("Error.")
                t.hideturtle()
                screen.exitonclick()

            if len(set(years)) != len(years): #Checks if there are any duplicates in years entered. If so, "error" is outputted. [STEP 1]
                print("Error.")
                t.hideturtle()
                screen.exitonclick()

            #Obtains birth rate data point
            yValue = float(input("What is the y coordinate of data point {}? ".format(i+1)))
            yValue = round(yValue, 2) #Rounds the birth rate to 2 decimal places [STEP 2]
            birthRates.append(yValue) #Adds birth rate to a list

            if yValue < 0.2 or yValue > 4.5: #Checks if birth rate is NOT in range. If so, "error" is outputted. [STEP 1]
                print("Error.")
                t.hideturtle()
                screen.exitonclick()

            #If user's data points (years and birth rates) pass all error checks, data points are marked [STEP 3]
            t.goto(xValue,yValue)
            t.stamp()
            t.down()
else: #"Error" outputted if data points entered by user are NOT a positive integer
    print("Error.") 
    t.hideturtle()
    screen.exitonclick()

t.up()
t.hideturtle() #Hides turtle after step 3

#The program asks the user to enter two years they want to use to interpolate as integers [STEP 4]
startYear = int(input("Which year would you like to start with? "))
if startYear < 1910 or startYear > 2022: #Checks if start year is NOT within range. If year is not in range, "Error." is outputted.
    print("Error.")
    t.hideturtle()
    screen.exitonclick()
if startYear not in years: #Checks if start year is NOT in existing data. If year was not inputted earlier, "Error." is outputted.
    print("The entered data point does not exist.")
    t.hideturtle()
    screen.exitonclick()

endYear = int(input("Which year would you like to end with? ")) 
if endYear != startYear: #Ensures that end year is different from start year. If end and start year is the same, nothing outputs and program exits when graph is clicked.
    if endYear < 1910 or endYear > 2022: #Checks if end year is NOT within range. If year is not in range, "Error." is outputted.
        print("Error.")
        t.hideturtle()
        screen.exitonclick()
    if endYear not in years:  #Checks if end year is NOT in existing data. If year was not inputted earlier, "Error." is outputted.
        print("The entered data point does not exist.")
        t.hideturtle()
        screen.exitonclick()
else:
    screen.exitonclick()

#Obtains index of years chosen for interpolation (used later for interpolation equation)
startIndex = years.index(startYear)
endIndex = years.index(endYear)

#Creates a new list that combines both the year and the birth rate in (x,y) format
existingData = []

for years, birthRates in zip(years, birthRates):
    existingData.append([years] + [birthRates])


#Determines estimated birth year for every year in between start and end year chosen [STEP 5]
if startYear < endYear: 
    numYears = endYear - startYear
    estimateYears = int(numYears-1) #Determines number of years to interpolate

    for x in range(estimateYears):
        def estimate(entry, predictYear): #Custom function using interpolation equation
            result = entry[startIndex][1] + (predictYear - entry[startIndex][0]) * ((entry[endIndex][1] - entry[startIndex][1])/(entry[endIndex][0] - entry[startIndex][0]))
            return result
        
        predictYear = startYear + (x+1) 

        predictBirthRate = estimate(existingData, predictYear)

        estimateX = int(predictYear)
        estimateY = float(predictBirthRate)

        #Prints the estimate for every year between chosen start and end years
        print(estimateX, '{:.2f}'.format(round(estimateY, 2)))

        t.goto(estimateX, estimateY)
        t.stamp()
        t.up()
else: #Accounts for the event that the user's start year and end year is chosen in reverse chronological order
    numYears = startYear - endYear
    estimateYears = int(numYears-1) #Determines number of years to interpolate

    def estimate(entry, predictYear): #Custom function using interpolation equation
            result = entry[endIndex][1] + (predictYear - entry[endIndex][0]) * ((entry[startIndex][1] - entry[endIndex][1])/(entry[startIndex][0] - entry[endIndex][0]))
            return result

    for x in range(estimateYears):
        predictYear = endYear + (x+1)

        predictBirthRate = estimate(existingData, predictYear)

        estimateX = int(predictYear)
        estimateY = float(predictBirthRate)

        #Prints the estimate for every year between chosen start and end years
        print(estimateX, '{:.2f}'.format(round(estimateY, 2)))

        t.goto(estimateX, estimateY)
        t.stamp()
        t.up()
        
screen.exitonclick()