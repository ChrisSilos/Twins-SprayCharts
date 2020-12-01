# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:00:22 2020

@author: StevensUser
"""

# -*- coding: utf-8 -*-
"""


@author: Christian Silos
I pledge my honor I have abided by the Stevens Honor System
"""
#import necessary libraries

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math as m

# create lists that will be used in final bargaphs
Categories = ['Flyball%','Linedrive%','Groundball%', 'Hard-hit% (>92mph)','Med-hit% (>72mph)','Soft-hit% (<72mph)','Pull%','Straightaway%','Oppo%']
Twins2018 = [] 
Twins2019 = []
Kepler2018 = []
Kepler2019 = []


def WinningPercentage(): #function that generates a comparison between Actual Winning Percentage and predicted winning percentage
    
    GeneralData = [] #initiate list to hold data from the csv
    
    #append data from the csv into the list
    file = open("2019MLBGeneralData.csv",'r')
    for line in file:
        parts = line.strip().split(',')
        GeneralData.append(parts) 
        
    TeamNames = [] #initiate list for team names
    Wins = [] #initiate list for wins
    Losses = [] #initiate list for losses
    RunsScored = [] #initiate list for runs scored
    RunsAllowed = [] #initiate list for runs allowed
    WinningPercentages=[] #initiate list for winning percentages
    PythagoreanWinningPercentages = [] #initiate list for pythagorean winning percentages
    Differences = [] #initiate list for differences. This will be used when cacluating the average difference between the two sets
    
    #fill each list with appropriate values 
    for i in range(len(GeneralData)):
        if i == 0:
            continue
        else:
            TeamNames.append(GeneralData[i][0])
            Wins.append(int(GeneralData[i][1]))
            Losses.append(int(GeneralData[i][2]))
            RunsScored.append(int(GeneralData[i][11]))
            RunsAllowed.append(int(GeneralData[i][12]))
            
    #calculate the actual and pythagorean winning percentages for each team
    for i in range(len(Wins)):
        winningPercentage = "{:.1f}".format(Wins[i]/(Wins[i]+Losses[i])*100) #{:.1f}.format() rounds the value to the nearest tenth
        WinningPercentages.append(float(winningPercentage)) #the value must be converted back into a float after the previous line
        
        PythagoreanWinningPercentage = "{:.1f}".format(m.pow(RunsScored[i],1.83)/(m.pow(RunsScored[i],1.83)+m.pow(RunsAllowed[i],1.83))*100)
        PythagoreanWinningPercentages.append(float(PythagoreanWinningPercentage))
        
    #calculate the differences between actual winning percentage an pythagorean winning percentage for each team   
    for i in range (len(TeamNames)):
        difference = abs(WinningPercentages[i]-PythagoreanWinningPercentages[i])
        Differences.append(difference)
    
    avgdifference = "{:.2f}".format((sum(Differences))/30) #calculate the average difference among all 30 teams
    
    #begin creating the bar graph
    ind = np.arange(len(TeamNames))  # the x locations for the groups
    width = 0.25  # the width of the bars
    fig, ax = plt.subplots(figsize=(20,4)) #size of the graph
    ax.bar(ind, WinningPercentages, width,label='Actual Winning %') #bars for actual winning percentage
    ax.bar(ind + width, PythagoreanWinningPercentages, width,label='Pythagorean Winning %') #bars for predicted winning percentage
    ax.set_ylabel('Winning %')    
    ax.set_title('Actual Winning % vs Predicted Winning % in the 2019 MLB Season')
    ax.set_xticks(ind)
    ax.set_xticklabels(TeamNames)
    plt.xticks(rotation=70)
    ax.legend()
    fig.tight_layout()
    plt.ylim(25,70)
    plt.show()
    
    print("Average Difference:",avgdifference+"%")


def SprayChart(filename): #function that produces a spray chart
    
    file = open(filename,'r') #opens the file
    data=[] #initiate list to hold the data
    
    
    #converts csv data into a matrix    
    for line in file:
        parts = line.strip().split(',')
        data.append(parts) 
        
    xcoordinates = [] #initiate list to hold x coordinates
    ycoordinates = [] #initiate list to hold y coordinates
    distance = [] #initiate list to hold distance values
    hand = [] #initiate list to determine right or left handed batter
    outcomes = [] #initiate list to hold outcomes
    pulled = [] #initate list to hold pulled balls
    battedballtype = [] #initiate list to hold type of batted ball
    exitvelo = [] #initiate list to hold exit velocities
    
    #append the appropiate element from the data into each list
    for i in range(len(data)):
        xcoordinates.append(data[i][37])
        ycoordinates.append(data[i][38])
        distance.append(data[i][52])
        hand.append(data[i][17])
        outcomes.append(data[i][8])
        battedballtype.append(data[i][23])
        exitvelo.append(data[i][53])
    
    #remove extra quotation marks from each element in each list
    xcoordinates = [i.replace('"', '') for i in xcoordinates]
    ycoordinates = [i.replace('"', '') for i in ycoordinates]
    distance = [i.replace('"', '') for i in distance]
    hand = [i.replace('"','') for i in hand]
    outcomes = [i.replace ('"','') for i in outcomes]
    battedballtype = [i.replace ('"','') for i in battedballtype]
    exitvelo = [i.replace ('"','') for i in exitvelo]
    
    #initate variables that will be used to calculate flyball, groundball,popup, and linedrive percentages
    flyballs = 0
    groundballs = 0
    popups = 0
    linedrives = 0
    
    # loops through the data and finds the amount of flyballs, groundballs, popups, and linedrives in the data
    for i in range(len(battedballtype)):
        if battedballtype[i] == 'ground_ball':
            groundballs+=1
        elif battedballtype[i] == 'line_drive':
            linedrives+=1
        elif battedballtype[i] == 'popup':
            popups+=1
        elif battedballtype[i] == 'fly_ball':
            flyballs+=1
        else:
            continue
    
    # calculate line drive, flyball, and groundball percentages
    LDpercent = "{:.1f}".format(linedrives/(linedrives+flyballs+groundballs+popups)*100)
    FBpercent = "{:.1f}".format(flyballs/(linedrives+flyballs+groundballs+popups)*100)
    GBpercent = "{:.1f}".format(groundballs/(linedrives+flyballs+groundballs+popups)*100)
    
    #initate variables that will be used to calculate hard, medium, and soft hit percentages
    hard = 0
    med = 0
    soft = 0
    
    del(exitvelo[0]) #removes the first element in the exit velocity list because it is the title of the column 'launch speed'
    
    #loops through the data and find the number of balls hit over 92mph, between 72 and 92 mph, and below 72 mph
    for i in range(len(exitvelo)):
        if exitvelo[i].isalpha() == True: #this line is necessary for skipping over any values that are listed as 'null'
            continue
        elif float(exitvelo[i]) >= 92:
            hard +=1
        elif float(exitvelo[i]) >= 72:
            med +=1
        else:
            soft +=1
    
    #calculates hard hit percentage, medium hit percentage, and soft hit percentage
    hardpercentage = "{:.1f}".format(hard/(hard+med+soft)*100)
    medpercentage = "{:.1f}".format(med/(hard+med+soft)*100)
    softpercentage = "{:.1f}".format(soft/(hard+med+soft)*100)
     
    
    # removes the first element in each of these lists because they are the titles of the columns
    del xcoordinates[0]
    del ycoordinates[0]
    del distance[0]
    del hand[0]
    del outcomes[0]
    del exitvelo[0]
    
    #initiate lists that will hold values needed to produce the spray chart
    cleanedxcoordinates = [] 
    cleanedycoordinates=[]
    cleaneddistance = []
    hrhand = [] 
    totalinstances = 0
    
  
    # initiate list to calculate overall batted-ball metrics. These lists are different that the lists above because the lists above will only account for the event that the user inputs when prompted. These lists keep track of every instance throughout the whole dataset whether the user asks for it or not
    TotalcleanedX = []
    TotalcleanedY = []
    TotalcleanedDistance = []
    Totalhand = []
    RelLocation = []
    
    #initate variables that will be used to calculate pull percentage, opposite field percentage, and straightaway percentage of the ENTIRE dataset (differenct from the vairables used only for the instance that the user inputs)
    pull = 0
    oppo = 0
    straight = 0
    
    #loops through the list and finds necessary values for producing a spray chart
    for i in range(len(xcoordinates)):    
        if (xcoordinates[i].isalpha() == True) or (ycoordinates[i].isalpha() == True) or (distance[i].isalpha() == True): #in the dataset, sometimes one of these values will be 'null'. Since there needs to be an equal number of x/y coordinates and distances (will be used to plot in polar), if any of these values are 'null', then the whole line is ignored
            continue
        else: 
            #if the values are not alphabetic, then they are appended to the new lists as floats
            TotalcleanedX.append(float(xcoordinates[i]))
            TotalcleanedY.append(float(ycoordinates[i]))
            TotalcleanedDistance.append(float(distance[i]))
            Totalhand.append(hand[i])
            
    Totalsprayangles = [] #initiate list to hold spray angles of the ENTIRE dataset. NOTE* When reading the report, spray angles are NOT the same and launch angles in baseball. Spray angle refers to the horizontal angle at which the ball is hit, while launch angle refers to the vertical angle at which the ball is hit.
    for i in range(len(TotalcleanedX)):
        Totalsprayangles.append(-np.arctan((TotalcleanedX[i]-130)/(213-TotalcleanedY[i])) + 3.14/2) #this is the necessary math to convert the x/y location data into an angle for polar coordinates. If you try to plot the x/y coordinates directly onto a graph, they DO NOT show the true location of where the ball was hit
        
    #loops through the data and determines whether the ball was pulled, hit to the opposite field, or hit straightaway. These terms are explained in the report. 
    for i in range (len(TotalcleanedDistance)):
        #NOTE* The way I designed my spray chart, the right field line is located at theta=0, and the left field line is located at theta=pi.
        # The handed-ness of the batter must be considered, since right-handed and left-handed players have reversed pull and opposite field sides
        if Totalhand[i] == 'R' and Totalsprayangles[i] >= 1.832: #this value is 7pi/12. Based on my spray chart, this represents left-center field
            RelLocation.append(1)
            pull+=1
        elif Totalhand[i] == 'L' and Totalsprayangles[i] <= 1.309:#this value is 5pi/12. Based on my spray chart, this represents right-center field
            RelLocation.append(1)
            pull+=1
        elif (Totalsprayangles[i] < 1.832) and (Totalsprayangles[i] > 1.309): #this range represents center field
            RelLocation.append(2)
            straight+=1
        else: 
            RelLocation.append(0)    
            oppo+=1
                     
    #calculates pull percentage, opposite field percentage, and straightaway percentage
    pullpercent = "{:.1f}".format(pull/(pull+oppo+straight)*100)
    oppopercent = "{:.1f}".format(oppo/(pull+oppo+straight)*100)
    straightpercent = "{:.1f}".format(straight/(pull+oppo+straight)*100)
    
    
    output = "" #initates output variable
    
    #prompt the user for the type of event they would like to see in the spray chart
    while True:
        instance = input("What event would you like to view on the spray chart? (Enter 'HELP' for options):")
        if (instance == 'home_run') or (instance == 'single') or (instance == 'double') or (instance == 'triple') or (instance == 'field_out') or (instance == 'grounded_into_double_play'):
            output = instance
            break
        elif (instance == 'HELP'): #provide user with a list of options and proper syntax
            print("\nHere is a list of options with proper syntax: \n")
            print('To view singles, enter: "single"')
            print('To view doubles, enter: "double"')
            print('To view triples, enter: "triple"')
            print('To view home runs, enter: "home_run"')
            print('To view field outs, enter: "field_out"')
            print('To view double plays, enter: "grounded_into_double_play"')
            continue
        else:
            print()
            print("Sorry, that is not an option. Please try again.(for a list of options, enter: HELP)") #reprompt the user if they do not enter and appropriate event
            continue
    
    #similar to loop featured previously. HOWEVER, this loop only pertains to the instance that the user inputs, NOT the entire dataset
    for i in range(len(xcoordinates)):    
        if (xcoordinates[i].isalpha() == True) or (ycoordinates[i].isalpha() == True) or (distance[i].isalpha() == True):
            continue
        else: 
            if outcomes[i] == output:
                cleanedxcoordinates.append(float(xcoordinates[i]))
                cleanedycoordinates.append(float(ycoordinates[i]))
                cleaneddistance.append(float(distance[i]))
                hrhand.append(hand[i])
                totalinstances+=1
                
    sprayangles = [] #initiate list to hold spray angle values ONLY for the event indicated by the user. This is necessary when converting the x,y coordinates to polar coordinates
    for i in range(len(cleanedxcoordinates)):
        sprayangles.append(-np.arctan((cleanedxcoordinates[i]-130)/(213-cleanedycoordinates[i])) + 3.14/2) #This is the conversion necessary to get the coordinates into a usable form and orientation
    
    #Again, this is the SAME loop as used previously. HOWEVER, it only pertains to the events indicated by the user input
    for i in range (len(cleaneddistance)):
        if hrhand[i] == 'R' and sprayangles[i] >= 1.832:
            pulled.append(1)
        elif hrhand[i] == 'L' and sprayangles[i] <= 1.309:
            pulled.append(1)
        elif (sprayangles[i] < 1.832) and (sprayangles[i] > 1.309):
            pulled.append(2)
        else: 
            pulled.append(0)
    
    colors = [] #initiate list to hold the colors that will be used in the spray chart
    for i in pulled:
        if i == 1:
            colors.append('red') #pulled balls are red
        elif i == 2:
            colors.append('green') #straightaway balls are green
        else:
            colors.append('blue') #opposite field balls are blue
    
    wall = [] #initate list to hold theta values that will be used to create an outfield wall on the spray chart
    walldistance = []#initiate list to hold r values that will be used to create an outfield wall on the spray chart
    infield = [] #initiate list to hold r values that will be used to create the edge of the infield on the spray chart
    
    angle = 0 #create variable to start outfield wall on the right field line (remember, theta=0 is the right field line)
    for i in range(314): #in order to create a wall, I decided to plot 314 individual points that look like an arc when plotted. I chose 314 because the angle from one side of the chart to the other is pi
        walldistance.append(350) #r value for the wall in the polar plot. 350 represents 350 feet from home plate, a reasonable distance for an outfield wall. In reality, center field tends to be deeper than right and left field, producing a more elliptical wall.
        infield.append(140) #r value for the infield in the polar plot. 140 feet is a reasonable distance for the edge of the infield
        wall.append(angle) #
        angle = angle + .01 #theta value for both the wall and the infield. Needs to increase by .01 in order to simulate an arc
    
    #defines r and theta values used in plotting each hit
    #r = cleaneddistance 
    #theta = sprayangles          
    #print(sprayangles)
    
    fig = plt.figure(figsize=(10,10)) #size of the plot
    ax = fig.add_subplot(111, projection='polar') #polar plot
    c = ax.scatter(sprayangles, cleaneddistance,c=colors, cmap='hsv', alpha=0.5) #coordinates for each batted-ball
    c = ax.scatter(wall, walldistance, c='black', cmap='hsv', alpha=0.75) #coordinates for the wall
    c = ax.scatter(wall, infield, cmap='hsv',c='green', alpha=1) #coordinates for the edge of the infield
    c = ax.scatter(1, 90, cmap='hsv',c='black',s=100, alpha=1) #coordinates for first base
    c = ax.scatter(1.5707, 120, cmap='hsv',c='black',s=100 ,alpha=1) #coordinates for second base 
    c = ax.scatter(2.14, 90, cmap='hsv',c='black',s=100, alpha=1) #coordinates for third base
    
    #prints the appropriate name above each spray chart
    if filename == "MKepler2018.csv":
        plt.title("Max Kepler 2018: "+output+"s",fontdict={'fontsize':20})
    elif filename == "MKepler2019.csv":
        plt.title("Max Kepler 2019: "+output+"s",fontdict={'fontsize':20})
    elif filename == "2018TwinsData.csv":
        plt.title("Twins 2018: "+output+"s",fontdict={'fontsize':20})
    elif filename == "2019TwinsData.csv":
        plt.title("Twins 2019: "+output+"s",fontdict={'fontsize':20})
    
    ax.set_thetamin(45) #set theta bounds for quarter circle
    ax.set_thetamax(135)
    ax.set_yticklabels([]) #remove y labels
    ax.set_xticklabels([]) #remove x labels
    plt.ylim(0,440) #set maximum r value at r=440 to prevent auto-scaling. 440 is an extremely far distance for a hit, so I don't believe many hits (if at all), were too far to be plotted. Any hit between this value and the outfield wall was most likely a home run (not perfect since in reality different baseball stadiums have different outfield dimensions)
    ax.grid(False) #remove gridlines
    plt.show() #show plot
    
    # initiate vairables to keep track of the amount of INPUT INSTANCES were pulled, hit straightaway, and hit to the opposite field. Again this is different then the variables used to track the ENTIRE dataset
    finalpull = 0
    finalstraight = 0
    finaloppo = 0
    
    #tally the amount of each instance
    print("Total",output+'s',':',totalinstances)
    for i in pulled:
        if i == 1:
            finalpull+=1
        elif i == 2:
            finalstraight+=1
        else:
            finaloppo+=1
    
    #calculate pull, straightaway, and opposite field percentages for the input instances 
    if (finalpull+finaloppo+finalstraight == 0): #necessary to avoid division by 0 in the case that there are no instances in the dataset (ex. Max Kepler did not hit any triples in 2019)
        finalpullpercent = 0
        finaloppopercent = 0
        finalstraightpercent = 0
    else:
        finalpullpercent = "{:.1f}".format(finalpull/(finalpull+finaloppo+finalstraight)*100)
        finaloppopercent = "{:.1f}".format(finaloppo/(finalpull+finaloppo+finalstraight)*100)
        finalstraightpercent = "{:.1f}".format(finalstraight/(finalpull+finaloppo+finalstraight)*100)      
    
    #print results
    print(output, "pull percentage:",finalpullpercent)
    print(output, "straightaway percentage:",finalstraightpercent)
    print(output, "opposite field percentage:",finaloppopercent)
     
    #append appropriate values to the lists defined at the beginning of the script based on filename
    if filename == "MKepler2018.csv":
        Kepler2018.append(float(FBpercent))
        Kepler2018.append(float(LDpercent))
        Kepler2018.append(float(GBpercent))
        Kepler2018.append(float(hardpercentage))
        Kepler2018.append(float(medpercentage))
        Kepler2018.append(float(softpercentage))
        Kepler2018.append(float(pullpercent))
        Kepler2018.append(float(straightpercent))
        Kepler2018.append(float(oppopercent))
    elif filename == "MKepler2019.csv":
        Kepler2019.append(float(FBpercent))
        Kepler2019.append(float(LDpercent))
        Kepler2019.append(float(GBpercent))
        Kepler2019.append(float(hardpercentage))
        Kepler2019.append(float(medpercentage))
        Kepler2019.append(float(softpercentage))
        Kepler2019.append(float(pullpercent))
        Kepler2019.append(float(straightpercent))
        Kepler2019.append(float(oppopercent))
    elif filename == "2018TwinsData.csv":
        Twins2018.append(float(FBpercent))
        Twins2018.append(float(LDpercent))
        Twins2018.append(float(GBpercent))
        Twins2018.append(float(hardpercentage))
        Twins2018.append(float(medpercentage))
        Twins2018.append(float(softpercentage))
        Twins2018.append(float(pullpercent))
        Twins2018.append(float(straightpercent))
        Twins2018.append(float(oppopercent))
    elif filename == "2019TwinsData.csv":
        Twins2019.append(float(FBpercent))
        Twins2019.append(float(LDpercent))
        Twins2019.append(float(GBpercent))
        Twins2019.append(float(hardpercentage))
        Twins2019.append(float(medpercentage))
        Twins2019.append(float(softpercentage))
        Twins2019.append(float(pullpercent))
        Twins2019.append(float(straightpercent))
        Twins2019.append(float(oppopercent))  
        


WinningPercentage() #print winning percentage graph

#produce spray charts for each dataset
SprayChart("2018TwinsData.csv") 
SprayChart("2019TwinsData.csv")
SprayChart("MKepler2018.csv")
SprayChart("MKepler2019.csv")


#create dual bar graph comparing batted-ball data for MAX KEPLER across 2018 and 2019
ind = np.arange(len(Kepler2018))  # the x locations for the groups
width = 0.35  # the width of the bars
fig, ax = plt.subplots(figsize=(10,5))
rects1 = ax.bar(ind - width/2, Kepler2018, width,label='2018')
rects2 = ax.bar(ind + width/2, Kepler2019, width,label='2019')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percent')
ax.set_title('Max Kepler 2018 vs 2019')
ax.set_xticks(ind)
ax.set_xticklabels(Categories)
plt.xticks(rotation=70)
ax.legend()
fig.tight_layout()
plt.show()

#create dual bar graph comparing batted-ball data for MINNESOTA TWINS across 2018 and 2019
ind = np.arange(len(Twins2018))  # the x locations for the groups
width = 0.35  # the width of the bars
fig, ax = plt.subplots(figsize=(10,5))
rects1 = ax.bar(ind - width/2, Twins2018, width,label='2018')
rects2 = ax.bar(ind + width/2, Twins2019, width,label='2019')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percent')
ax.set_title('Twins Offense 2018 vs 2019')
ax.set_xticks(ind)
ax.set_xticklabels(Categories)
plt.xticks(rotation=70)
ax.legend()
fig.tight_layout()
plt.show()

