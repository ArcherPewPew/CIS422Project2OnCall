'''
Author: Alyssa Huque
Date of last modification: 2-19-2020
Description: This produces the functionality of the RA Preferences module
References:
    TODO
'''

class Preferences:
    def __init__(self):
        # TODO
        return None
    
    def importFile(self, fileName):
        '''
        string -> int
        Receives the name of the file to import
        This function imports RA preference information. 
        The file may contain one or several RAs. This function also accounts for an empty file.
        The file may contain RAs who are already in the system. These RAs have their preferences updated.
        Returns a 0 if no errors occured or a 1 if an error occured
        '''
        # TODO
        return # 0 if no errors occured or a 1 if an error occured
    
    def updatePreferences(self, idNum, index, newPref):
        '''
        int, int, str -> int
        Receives the id number of the RA with the changed preference,
            the field of the preference changed, what the new preference is
        This function updates a field in the raPreferences dictionary
        Returns a 0 if no errors occured or a 1 if an error occured
        '''
        # TODO
        return # 0 if no errors occured or a 1 if an error occured
    
    def saveSettings(self): # TODO determine how the preferences will be sent, perhaps separate functions
        '''
        
        '''
        # TODO
        return 