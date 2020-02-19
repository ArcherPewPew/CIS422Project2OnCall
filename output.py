'''
Author: Kiana Hosaka
Date of last modification: 2-19-2020
Description: This produces the functionality of the Shift Assignments module
References:
    TODO
'''

class Assignments:
    def __init__(self):
        # TODO
        return None
    
    def exportFile(self, fileName):
        '''
        string -> int
        Receives the name of the file to export to
        This function exports the saved shift assignments to a specified CSV file
        Returns a 0 if no errors occured or a 1 if an error occured
        '''
        # TODO
        return # 0 if no errors occured or a 1 if an error occured
    
    def updateSchedule(self, weekNum, secondary, index, newName):
        '''
        int, int, int, str -> int
        Receives an int indicating the week number, 
            a 0 if the RA is the primary for the shift or a 1 if they are secondary,
            an int indicating the field in the list that was changed,
            and a str of the new name for that field
        This function updates a field in the shiftAssignmnets dictionary
        Returns a 0 if no errors occured or a 1 if an error occured
        '''
        # TODO
        return # 0 if no errors occured or a 1 if an error occured
    
    def generateSchedule(self):
        '''
        None -> int
        This function calls the schedulers and saves their returned information into the raPreferences dictionary
        Returns a 0 if no errors occured or a 1 if an error occured
        '''
        # TODO
        return # 0 if no errors occured or a 1 if an error occured
    
