'''
Author: Max Terry
Date of last modification: 2-25-2020
Description: This determines the on call schedule for weekday shifts
References:
    TODO
'''

import ast
import random

class WeekdayShifts:
    def __init__(self):
        self.raPreferences = self.getRaInformation()
        return None

    def getRaInformation(self):
        '''
        None -> (dictionary)
        Reads the dictionary in raPreferences.py.
        Returns a dictionary containing the preference information.
        '''
        fileContents = ''
        tempRaPreferences = {}
        with open("raPreferences.py", "r") as prefFile:
            fileContents = prefFile.readlines()[0]
            tempRaPreferences = ast.literal_eval(fileContents.strip("raPreferences = "))

        for raId in tempRaPreferences:
            tempRaPreferences[raId] = tempRaPreferences[raId][0:4]       #gets rid of weekend information
            tempRaPreferences[raId].append(0)           #to keep track of shift counter

        return tempRaPreferences

    def weekdayShifts(self):
        '''
        None -> (list)
        This function acts like a main function specific to scheduling weekdays and is called by output.py
        Returns a dictionary of the weekday shifts
        '''
        # IDEA: get list of all people that want to work on each work day, then randomly select from that list to fill all spots.
        #weekdays = {'Sunday':[], 'Monday':[], 'Tuesday':[], 'Wednesday':[], 'Thursday':[]}

       # for ra in self.raPreferences:

       #for testing
        weekdays = {'Sunday':['951111111', '951111112', '951111113', '951111114'], 'Monday':['951111115', '951111116', '951111117'],
                    'Tuesday': ['951111118', '951111119', '951111121'], 'Wednesday':['951111122', '951111123', '951111124'],
                    'Thursday': ['951111125', '951111126', '951111127']}

        schedule = self.scheduleShifts(weekdays)
        return schedule

    def scheduleShifts(self, initialWeekdays):
        '''
        dictionary -> list
        '''
        weekdays = initialWeekdays.copy()       #to avoid aliasing
        finalShiftList = []

        for i in range(10):     #ten weeks
            weekList = []
            primaryList = []
            secondaryList = []
            for day in weekdays:  #5 shifts per week
                needShiftRas = []           #will save who has the fewest shifts
                minShifts = 1000            #start at a high number so the first RA will be lower
                
                for ra in weekdays[day]:     #go through the ras to see who needs more shifts 
                    numberShifts = self.raPreferences[ra][4]
                    if numberShifts < minShifts:
                        minShifts = numberShifts
                        needShiftRas = [ra]      #save the name in the list of fewest shifts
                    elif numberShifts == minShifts:
                        needShiftRas.append(ra)

                if(len(needShiftRas) < 2):          #if there is only one person with the minimum number of shifts
                    haveShiftRas = weekdays[day].copy()
                    haveShiftRas.remove(needShiftRas[0])    #have to get rid of this to avoid duplicates
                    needShiftRas.append(random.choice(haveShiftRas))

                
                primaryRa = random.choice(needShiftRas)
                needShiftRas.remove(primaryRa)              #so there isnt a repeat here
                self.raPreferences[primaryRa][4] += 1       #increment the shift counter

                secondaryRa = random.choice(needShiftRas)   #don't need to remove this one as the availableRa list resets anyways
                self.raPreferences[secondaryRa][4] += 1

                primaryList.append(self.raPreferences[primaryRa][0])            #want all primary/secondary ras for a week in separate lists
                secondaryList.append(self.raPreferences[secondaryRa][0])

            weekList.append(primaryList)
            weekList.append(secondaryList)
            finalShiftList.append(weekList)

        return finalShiftList


    def assignDays(self):
        #schedule  this many per day at first, then fill in the last few later
        raPerDay = len(self.raPreferences) // 5
        leftOver = len(self.raPreferences) - (raPerDay * 5)
        weekdays = {"Sunday": [], "Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": []}


shifts = WeekdayShifts()
#shifts.assignDays()
shifts.weekdayShifts()

