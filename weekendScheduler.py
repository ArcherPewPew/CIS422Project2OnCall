'''
Author: Alex Archer
Date of last modification: 3-2-2020
Description: This determines the on call schedule for weekend shifts
References:
    https://stackoverflow.com/questions/13520876/how-can-i-make-multiple-empty-lists-in-python
'''

import random
import importlib
import raPreferences as raPrefs

def weekendShifts():
    '''
    None ->  [[], []] -- list of two-lists
    Reads the dictionary in raPreferences.py.
    This function acts like a main function specific to scheduling weekends and is called by output.py
    Returns a list of two-lists of the weekend shift schedule.
    '''
    importlib.reload(raPrefs)
    raPreferences =  raPrefs.raPreferences

    ra1 = raPreferences.get('3')[0][0] #ra 1 of bad pair 1
    ra2 = raPreferences.get('3')[0][1] 
    badPair1 = [ra1,ra2] 

    ra3 = raPreferences.get('3')[1][1] #ra 1 of bad pair 2
    ra4 = raPreferences.get('3')[1][1]
    badPair2 = [ra3,ra4]

    '''
    This loop strips the settings from the raPreferences dictonary, makes a copy in raDict
    and appends it with a new integer variable to count the number of shifts. 
    '''
    raDict = {}
    for key,val in raPreferences.items(): 
        if key not in ['1','2','3']:
            raDict[key] = val
            raDict[key].append(0) #add var to counts number of shifts

    dictLen = len(list(raDict))
    avg = (78 / dictLen) #there are 78 slots to fill / #RAs. Used for number of shifts enforcement.
  
    '''
    Each Primary/Secondary is a List that corresponds to a weekend with 4 shifts.
    Each weekend is filled by a Primary and a Secondary RA  per shift.
    Week one is unique as there is no Sunday shift. 
    '''
    primary_1 = ["P1 Friday", "P1 Saturday Day", "P1 Saturday Night", "X"]
    secondary_1 = ["S1 Friday", "S1 Saturday Day", "S1 Saturday Night", "X"]

    #The remaining 9 weeks are assigned as empty lists of size 4. 
    primary_2, secondary_2, primary_3, secondary_3, primary_4, secondary_4, primary_5, secondary_5, primary_6,\
        secondary_6, primary_7, secondary_7, primary_8, secondary_8, primary_9, secondary_9, primary_10,\
        secondary_10 = ([None]*4 for i in range(18)) 
    
    #Final output schedule data structure is therefor a list of two-lists.
    schedule = [[primary_1, secondary_1], [primary_2, secondary_2], [primary_3, secondary_3], \
		[primary_4, secondary_4], [primary_5, secondary_5], [primary_6, secondary_6], \
		[primary_7, secondary_7], [primary_8, secondary_8], [primary_9, secondary_9], \
		[primary_10, secondary_10]]

    weekcount = 1

    ''' This loop assigns RAs to the first week's primary and secondary shifts. There is no sunday shift''' 
    for day in range(3): #friday, saturday day, saturday night
        firstRa = random.choice(list(raDict)) #pick primary worker
        #make sure they don't have the week off
        while weekcount == raDict.get(firstRa)[4] or weekcount == raDict.get(firstRa)[5] or \
              weekcount == raDict.get(firstRa)[6]:
            firstRa = random.choice(list(raDict)) 
        raDict[firstRa][7] += 1 #increase shift counter
        secondRa = random.choice(list(raDict)) #pick secondary worker
        #make sure they don't have the week off, aren't a disallowed pair, the same person or have > avg shifts.
        while [firstRa,secondRa] == badPair1 or [secondRa,firstRa] == badPair1 or [firstRa,secondRa] == badPair2 or \
              [secondRa,firstRa] == badPair2 or firstRa == secondRa or weekcount == raDict.get(secondRa)[4] or \
              weekcount == raDict.get(secondRa)[5] or weekcount == raDict.get(secondRa)[6]: 
            secondRa = random.choice(list(raDict)) 
        raDict[secondRa][7] += 1 #increase shift counter
        #add each RA to the primary/secondary list for week one.
        primary_1[day] = raDict[firstRa][0]
        secondary_1[day] = raDict[secondRa][0]  
    weekcount += 1

    ''' This loop assigns RAs to Primary and Secondary shifts for weeks 2 through 10'''
    for week in range(1,10): #weeks 2-10 
        for day in range(4): #friday, saturday day, saturday night, sunday day
            firstRa = random.choice(list(raDict)) #pick primary worker
            #make sure they dont have the week off or have more shifts than average.
            while weekcount == raDict.get(firstRa)[4] or weekcount == raDict.get(firstRa)[5] or \
                  weekcount == raDict.get(firstRa)[6] or raDict.get(firstRa)[7] > avg:
                firstRa = random.choice(list(raDict)) 
            raDict[firstRa][7] += 1 #increase shift counter
            secondRa = random.choice(list(raDict)) #pick secondary worker
            #make sure they don't have the week off, aren't a disallowed pair, or the same person, and have no more shifts than average
            while [firstRa,secondRa] == badPair1 or [secondRa,firstRa] == badPair1 or [firstRa,secondRa] == badPair2 or \
                  [secondRa,firstRa] == badPair2 or firstRa == secondRa or weekcount == raDict.get(secondRa)[4] or \
                  weekcount == raDict.get(secondRa)[5] or weekcount == raDict.get(secondRa)[6] or raDict.get(secondRa)[7] > avg+1: 
                secondRa = random.choice(list(raDict))
            raDict[secondRa][7] += 1 #increase shift counter
            #add each RA to the primary/secondary list for the particular week
            schedule[week][0][day] = raDict[firstRa][0]
            schedule[week][1][day] = raDict[secondRa][0]    
        weekcount += 1

    return(schedule)    

''' These functions are for testing '''
def clearshifts(): #clears shift count, useful for resetting.
    for key in raDict.keys():
        raDict[key][7] = 0

def shiftcount(): #counts shifts, useful for testing
    numshifts = 0
    for key in raDict.keys():
        numshifts += raDict[key][7]
        print(raDict[key][0], ' has ', raDict[key][7], " shifts.") 
    print("numshifts: ", numshifts)
    
''' alternate code

import raPreferences  #directly instead of importlib + update works too

'''
