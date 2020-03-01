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
        raInfo = self.getRaInformation()
        self.raPreferences = raInfo[0]
        self.settings = raInfo[1]
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

        finalReference = {}
        settings = {}
        for raId in tempRaPreferences:
            if raId not in ['1','2','3']:       #to save just the RA information
                finalReference[raId] = tempRaPreferences[raId][0:4]       #gets rid of weekend information
                finalReference[raId].append(0)           #to keep track of shift counter
            else:
                settings[raId] = tempRaPreferences[raId]

        return finalReference,settings

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

        #self.assignDays()
        schedule = self.scheduleShifts(weekdays)
        return schedule

    def assignDays(self):
        #schedule  this many per day at first, then fill in the last few later
        raPerDay = len(self.raPreferences) // 5
        leftOver = len(self.raPreferences) - (raPerDay * 5)
        weekdays = {"Sunday": [], "Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": []}
        raList = list(self.raPreferences.keys())
        
        #Gold star RA gets their first preference
        goldStarRa = self.settings['1']
        goldStarInfo = self.raPreferences[goldStarRa]
        goldStarDay = goldStarInfo[1]
        weekdays[goldStarDay].append(goldStarRa)
        raList.remove(goldStarRa)

        rasToRemove = []
        random.shuffle(raList)          #so every ra has an equal chance of being scheduled first/last
        #first choice loop
        for ra in raList:
            firstPreference = self.raPreferences[ra][1]
            if(len(weekdays[firstPreference]) < raPerDay):
                weekdays[firstPreference].append(ra)
                rasToRemove.append(ra)
        raList = [ra for ra in raList if ra not in rasToRemove]     #removes the scheduled RAs so they are not considered later

        #second choice loop
        rasToRemove = []
        random.shuffle(raList)
        for ra in raList:
            secondPreference = self.raPreferences[ra][2]
            if(len(weekdays[secondPreference]) < raPerDay):
                weekdays[secondPreference].append(ra)
                rasToRemove.append(ra)
        raList = [ra for ra in raList if ra not in rasToRemove]

        #third choice loop
        rasToRemove = []
        random.shuffle(raList)
        for ra in raList:
            thirdPreference = self.raPreferences[ra][3]
            if(len(weekdays[thirdPreference]) < raPerDay):
                weekdays[thirdPreference].append(ra)
                rasToRemove.append(ra)
        raList = [ra for ra in raList if ra not in rasToRemove]

        #make sure everyday has three people on it before assigning extra days
        #for day in weekdays:
          #  while(len(weekdays[day] != raPerDay):

        #for leftover people
        rasToRemove = []
        random.shuffle(raList)
        for ra in raList:
            raPreferences = self.raPreferences[ra][1:4]
            for i in range(3):
                day = raPreferences[i]
                if(len(weekdays[day]) < raPerDay + 1 and ra not in rasToRemove):
                    weekdays[day].append(ra)
                    rasToRemove.append(ra)
        raList = [ra for ra in raList if ra not in rasToRemove]


        print(weekdays)

        #for i in range(3):      #to loop through each choice



        #four/five different loops: one for first choice, one for second, one for third, and then tiebreakers and then leftovers if needed


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



shifts = WeekdayShifts()
shifts.assignDays()
shifts.weekdayShifts()

