import random
raPreferences = {951111111:	["Alex Archer",	"Tuesday",	"Thursday",	"Sunday", 3, 5, 8], 951111112: ["Kiana Hosaka", "Sunday", "Thursday", "Monday", 2, 6, 4], 951111113: ["Alyssa Huque", "Wednesday", "Monday", "Sunday", 0, 0, 0], 951111114: ["Lily Jim", "Thursday", "Sunday", "Tuesday", 5, 3, 9], 951111115: ["Max Terry", "Monday", "Sunday", "Thursday", 10, 5, 1], 951111116: ["Lucas Hyatt", "Wednesday", "Tuesday", "Monday", 5, 7, 2], 951111117: ["James Kang", "Tuesday", "Monday", "Sunday", 4, 8, 3], 951111118: ["Claire Kolln", "Thursday", "Wednesday", "Tuesday", 6, 9, 0], 951111119: ["Leonie Way", "Sunday", "Tuesday", "Thursday", 3, 2, 8], 951111121: ["Stefan Fields", "Wednesday", "Monday", "Sunday", 10, 1, 5], 951111122: ["Justin Becker", "Thursday", "Wednesday", "Monday", 5, 0, 9], 951111123: ["Cory Ingram", "Monday", "Sunday", "Tuesday", 10, 4, 3], 951111124: ["Samuel Lundquist", "Thursday", "Monday", "Wednesday", 3, 7, 10], 951111125: ["Olivia Pannell", "Monday", "Wednesday", "Thursday", 2, 4, 9], 951111126: ["Bethany Van Meter", "Sunday", "Thursday", "Tuesday", 9, 3, 8], 951111127: ["Ryan Gurnick", "Thursday", "Monday", "Wednesday", 0, 7, 10], 1: 951111116, 2: 2, 3: [[951111114, 951111127], [0, 0]]}

def foo():

    if raPreferences.get(3): #setting key
        p1ra1 = raPreferences.get(3)[0][0] #student 1 of bad pair 1
        p1ra2 = raPreferences.get(3)[0][1] #student 2 of bad pair 1
        bad1 = [p1ra1,p1ra2] #bad pair 1
        
        p2ra1 = raPreferences.get(3)[1][1]
        p2ra2 = raPreferences.get(3)[1][1]
        bad2 = [p2ra1,p2ra2]
        
        badpairs = [bad1,bad2]

    radict = {}

    for key,val in raPreferences.items(): ##copy dictonary w/o preferences
        if key not in [1,2,3]:
            radict[key] = val
            radict[key].append(0) #add var to counts number of shifts

    
    primary_1 = ["P1 Friday", "P1 Saturday Day", "P1 Saturday Night", "X"]
    secondary_1 = ["S1 Friday", "S1 Saturday Day", "S1 Saturday Night", "X"]
    primary_2 = ["P2 Friday", "P2 Saturday Day", "P2 Saturday Night", "P2 Sunday Day"]
    secondary_2 = ["S2 Friday", "S2 Saturday Day", "S2 Saturday Night", "S2 Sunday Day"]
    primary_3 = ["P3 Friday", "P3 Saturday Day", "P3 Saturday Night", "P3 Sunday Day"]
    secondary_3 = ["S3 Friday", "S3 Saturday Day", "S3 Saturday Night", "S3 Sunday Day"]
    primary_4 = ["P4 Friday", "P4 Saturday Day", "P4 Saturday Night", "P4 Sunday Day"]
    secondary_4 = ["S4 Friday", "S4 Saturday Day", "S4 Saturday Night", "S4 Sunday Day"]
    primary_5 = ["P5 Friday", "P5 Saturday Day", "P5 Saturday Night", "P5 Sunday Day"]
    secondary_5 = ["S5 Friday", "S5 Saturday Day", "S5 Saturday Night", "S5 Sunday Day"]
    primary_6 = ["P6 Friday", "P6 Saturday Day", "P6 Saturday Night", "P6 Sunday Day"]
    secondary_6 = ["S6 Friday", "S6 Saturday Day", "S6 Saturday Night", "S6 Sunday Day"]
    primary_7 = ["P7 Friday", "P7 Saturday Day", "P7 Saturday Night", "P7 Sunday Day"]
    secondary_7 = ["S7 Friday", "S7 Saturday Day", "S7 Saturday Night", "S7 Sunday Day"]
    primary_8 = ["P8 Friday", "P8 Saturday Day", "P8 Saturday Night", "P8 Sunday Day"]
    secondary_8 = ["S8 Friday", "S8 Saturday Day", "S8 Saturday Night", "S8 Sunday Day"]
    primary_9 = ["P9 Friday", "P9 Saturday Day", "P9 Saturday Night", "P9 Sunday Day"]
    secondary_9 = ["S9 Friday", "S9 Saturday Day", "S9 Saturday Night", "S9 Sunday Day"]
    primary_10 = ["P10 Friday", "P10 Saturday Day", "P10 Saturday Night", "P10 Sunday Day"]
    secondary_10 = ["S10 Friday", "S10 Saturday Day", "S10 Saturday Night", "S10 Sunday Day"]

    schedule = [[primary_1, secondary_1], [primary_2, secondary_2], [primary_3, secondary_3], \
		[primary_4, secondary_4], [primary_5, secondary_5], [primary_6, secondary_6], \
		[primary_7, secondary_7], [primary_8, secondary_8], [primary_9, secondary_9], \
		[primary_10, secondary_10]]

    weekcount = 1
    for i in range(3): #friday, saturday day, saturday night of week 1
        tmp = random.choice(list(radict)) #pick primary worker
        while weekcount == radict.get(tmp)[4] or weekcount == radict.get(tmp)[5] or weekcount == radict.get(tmp)[6]:
            tmp = random.choice(list(radict)) #make sure they dont have the week off
        radict[tmp][7] += 1 #increase shift counter
        tmp2 = random.choice(list(radict)) #pick secondary worker
        while [tmp,tmp2] == bad1 or [tmp2,tmp] == bad1 or [tmp,tmp2] == bad2 or [tmp2,tmp] == bad2 or tmp == tmp2 or weekcount == radict.get(tmp2)[4] or weekcount == radict.get(tmp2)[5]or weekcount == radict.get(tmp2)[6]: 
            tmp2 = random.choice(list(radict)) #make sure they arent the same person, a bad pair or have the week off.
        radict[tmp2][7] += 1 #increase shift counter
        primary_1[i] = radict[tmp][0]
        secondary_1[i] = radict[tmp2][0]    #update the week lists...
    weekcount += 1

    for x in range(1,10): #weeks 2-10
        for i in range(4): #friday, saturday day, saturday night, sunday day
            tmp = random.choice(list(radict)) #pick primary worker
            while weekcount == radict.get(tmp)[4] or weekcount == radict.get(tmp)[5] or weekcount == radict.get(tmp)[6]:
                tmp = random.choice(list(radict)) #make sure they dont have the week off
            radict[tmp][7] += 1 #increase shift counter
            tmp2 = random.choice(list(radict)) #pick secondary worker
            while [tmp,tmp2] == bad1 or [tmp2,tmp] == bad1 or [tmp,tmp2] == bad2 or [tmp2,tmp] == bad2 or tmp == tmp2 or weekcount == radict.get(tmp2)[4] or weekcount == radict.get(tmp2)[5]or weekcount == radict.get(tmp2)[6]: 
                tmp2 = random.choice(list(radict)) #make sure they arent the same person, a bad pair or have the week off.
            radict[tmp2][7] += 1 #increase shift counter
            schedule[x][0][i] = radict[tmp][0]
            schedule[x][1][i] = radict[tmp2][0]    #update the week lists..
        weekcount += 1

    ##picking other people means making sure they dont already have a shift ideally... going back to make shift counter
        ##TODO: account for the shifts now... 
    for key in radict.keys():
        print(radict[key][0], ' has ', radict[key][7], " shifts.") #prints 
    return(schedule)


        
