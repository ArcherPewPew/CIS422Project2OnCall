'''
    Author: Lily Jim
    Date of last modification: 2-19-2020
    Description: This creates the graphical user interface
    References:
        On Deck Development Team's Project 1 interface.py file
        Tkinter ComboBox: https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-combobox/
        Tkinter Grid: https://www.tutorialspoint.com/python/tk_grid.htm
        List methods: https://www.geeksforgeeks.org/python-list/ and https://www.programiz.com/python-programming/methods/list/index
        Dictionary methods: https://www.geeksforgeeks.org/iterate-over-a-dictionary-in-python/ and https://www.geeksforgeeks.org/get-method-dictionaries-python/
        TODO
'''

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import importlib

import input
import output
import raPreferences as raPrefs
import shiftAssignments as sa

class OnCallViewer:
    def __init__(self):
        '''
            None -> None
            This initializes an instance of OnCallViewer
        '''
        # Windows:
        self.root = tk.Tk()
        self.preferences = None
        self.schedule = None
        self.settings = None
        
        # RA Deletion Event Tracking:
        self.raIDs = None
        self.raNames = None
        self.delRaDropdown = None
        self.raSelectedToDelete = None
        
        # Preference Settings Tracker:
        self.settingsIDs = None
        self.settingsNames = None
        self.tiebreakerOptions = ['Random', 'Alphabetical Order by Last Name', 'Numerical Order by ID Number']
        self.settingsSaved = False
        # Dropdown menus
        self.goldStarDropdown = None
        self.tiebreakerDropdown = None
        self.pairingDropdown1 = None
        self.pairingDropdown2 = None
        self.pairingDropdown3 = None
        self.pairingDropdown4 = None
        # Selected in dropdowns
        self.goldStarChoice = None
        self.tiebreakerChoice = None
        self.pairingChoice1 = None
        self.pairingChoice2 = None
        self.pairingChoice3 = None
        self.pairingChoice4 = None
        return None
    
    
    ''' The following function is for the home window and runs the whole application '''
    def home(self):
        '''
            None -> None
            This acts as the main function for the user interface
            This creates the home screen
        '''
        # Setup home window:
        root = self.root
        root.title('On Call - Home')
        root.geometry('400x400+200+100') # width x height + x_offset + y_offset
        root.minsize(400, 400)
        
        # Create buttons:
        prefButton = tk.Button(root, text='RA Preferences', command=self.preferencesView)
        prefButton.pack(padx=50, side=tk.LEFT)
        
        scheduleButton = tk.Button(root, text='Schedule', command=self.scheduleView)
        scheduleButton.pack(padx=50, side=tk.LEFT)
        
        # Start screen:
        root.mainloop()
        return None
    
    
    ''' The following functions are for the preferences window '''
    def preferencesView(self):
        '''
            None -> None
            This creates the RA Preferences screen
        '''
        # Setup preferences window:
        self.preferences = tk.Toplevel()
        pref = self.preferences
        pref.title('On Call - RA Preferences')
        pref.geometry('800x400+250+150') # width x height + x_offset + y_offset
        pref.minsize(400, 400)
        
        # TODO display current RAs in the system
        
        # TODO provide way to update a preference
        
        # Create import button:
        importPrefs = tk.Button(pref, text='Import Preferences', command=self.importPreferences)
        importPrefs.grid(column=1, row=0, padx=50, pady=50)
        
        # Create RA deletion section:
        # Get RA names
        importlib.reload(raPrefs)
        self.raIDs = []
        self.raNames = []
        for ra in raPrefs.raPreferences:
            if(ra != 1 and ra != 2 and ra != 3):
                self.raIDs.append(ra)
                self.raNames.append(raPrefs.raPreferences.get(ra)[0])
        names = self.raNames
        # Create Delete RA label
        delRaLabel = tk.Label(pref, text='Delete RA:')
        delRaLabel.grid(column=0, row=1, padx=10, pady=10)
        # Create dropdown menu
        self.delRaDropdown = tk.ttk.Combobox(pref, values=names, state='readonly')
        self.delRaDropdown.grid(column=1, row=1, padx=10, pady=10)
        self.delRaDropdown.bind('<<ComboboxSelected>>', self.selectedForDeletion)
        # Create deletion save button:
        saveDeletion = tk.Button(pref, text='Save', command=self.deleteRA)
        saveDeletion.grid(column=2, row=1, padx=10, pady=10)
        
        # Start screen:
        pref.protocol('WM_DELETE_WINDOW', self.closePreferences)
        pref.update() # use update, not mainloop so other functions can still run
        return None
    
    def importPreferences(self):
        '''
            None -> None
            Asks user for csv file name
            Calls input.py's importFile function
        '''
        # TODO notify user what this will do
        files = [('CSV Files', '*.csv')]
        fileName = tk.filedialog.askopenfilename(filetypes = files)
        if(fileName != ''):
            error = input.Preferences.importFile(fileName)
            # TODO if error indicator returned, send message to user
        self.closePreferences()
        return None
    
    def selectedForDeletion(self, event):
        '''
            This updates the selected RA to delete when the choice changes in the dropdown menu
        '''
        self.raSelectedToDelete = self.delRaDropdown.get()
        return None
    
    def deleteRA(self):
        '''
            None -> None
            This calls input.py's function to delete the selected RA
        '''
        if(self.raSelectedToDelete != None):
            # TODO send warning to user
            #print(self.raSelectedToDelete)
            pos = self.raNames.index(self.raSelectedToDelete)
            #print(pos)
            studentID = self.raIDs[pos]
            #print(studentID)
            input.Preferences.deletePreferences(studentID)
            self.closePreferences() # terminates preferences window forcing the user to reopen it, refreshing the information
        else:
            # TODO send message to user to select RA
            print('No RA selected to delete')
        return None
    
    def closePreferences(self):
        '''
            None -> None
            This closes the preferences window
            It resets the RA Deletion Event Tracking variables
        '''
        self.preferences.destroy()
        self.preferences = None
        self.raIDs = None
        self.raNames = None
        self.delRaDropdown = None
        self.raSelectedToDelete = None
        return None
    
    
    ''' The following functions are for the schedule window '''
    def scheduleView(self):
        '''
            None -> None
            This creates the schedule screen
        '''
        # Setup schedule window:
        self.schedule = tk.Toplevel()
        sched = self.schedule
        sched.title('On Call - Schedule')
        sched.geometry('800x400+250+150') # width x height + x_offset + y_offset
        sched.minsize(400, 400)
        
        # TODO display current schedule in the system
        
        # TODO provide way to update a shift
        
        # Create Generate button:
        generateSched = tk.Button(sched, text='Generate New Schedule', command=self.generateNewSchedule)
        generateSched.grid(column=0, row=0, padx=50, pady=50)
        
        # Create export button:
        exportSched = tk.Button(sched, text='Export Schedule', command=self.exportSchedule)
        exportSched.grid(column=1, row=0, padx=50, pady=50)
        
        # Start screen:
        sched.update() # use update, not mainloop so other functions can still run
        return None
    
    def generateNewSchedule(self):
        '''
            None -> None
            This opens the preference's settings screen
            This calls output.py's generateSchedule function
        '''
        # TODO check if schedule already exists
        # TODO if schedule already exists, warn user of overwriting
        # TODO if schedule doesn't exist, tell user what will happen
        # TODO run settings screen
        # TODO check that settings are saved, if not do not run generate (both from the user clicking 'x' on the settings window or ignoring the settings window)
        self.settingsView()
        error = output.generateSchedule()
        # TODO handle error
        #self.settingsSaved = False # ready the system for the next generate schedule button press
        # TODO close schedule window to force a refresh
        return None
    
    def exportSchedule(self):
        '''
            None -> None
            Asks user for csv file name
            Calls output.py's exportFile function
        '''
        importlib.reload(sa)
        if(len(sa.shiftAssignments) != 0):
            files = [('CSV Files', '*.csv')]
            fileName = tk.filedialog.asksaveasfilename(filetypes = files)
            if(fileName != ''):
                error = output.exportFile(fileName)
                # TODO if error indicator returned, send message to user ---- exportFile currently never returns 1 under any circumstances
        else:
            tk.messagebox.showerror(message='No schedule to export. Please generate a schedule first.')
        return None
    
    
    ''' The following functions are for the generate schedule settings window '''
    def settingsView(self):
        '''
            None -> None
            This creates the preference's settings screen
        '''
        # Setup settings window:
        self.settings = tk.Toplevel()
        settings = self.settings
        settings.title('On Call - Settings')
        settings.geometry('900x300+300+200') # width x height + x_offset + y_offset
        settings.minsize(900, 300)
        
        # Get RA info for dropdown menus:
        importlib.reload(raPrefs)
        self.settingsIDs = []
        self.settingsNames = []
        for ra in raPrefs.raPreferences:
            if(ra != 1 and ra != 2 and ra != 3):
                self.settingsIDs.append(ra)
                self.settingsNames.append(raPrefs.raPreferences.get(ra)[0])
        names = self.settingsNames
        
        # Create Gold Star label:
        goldStarLabel = tk.Label(settings, text='Gold Star RA:')
        goldStarLabel.grid(column=0, row=0, padx=10, pady=10)
        # Create Gold Star dropdown menu:
        self.goldStarDropdown = tk.ttk.Combobox(settings, values=names, state='readonly')
        self.goldStarDropdown.grid(column=1, row=0, padx=10, pady=10)
        self.goldStarDropdown.current(0)
        self.goldStarChoice = self.goldStarDropdown.get()
        self.goldStarDropdown.bind('<<ComboboxSelected>>', self.updateGoldStarChoice)
        
        # Create tiebreaker label:
        tiebreakerLabel = tk.Label(settings, text='Preference Tiebreaker:')
        tiebreakerLabel.grid(column=0, row=1, padx=10, pady=10)
        # Create tiebreaker dropdown menu:
        self.tiebreakerDropdown = tk.ttk.Combobox(settings, values=self.tiebreakerOptions, state='readonly')
        self.tiebreakerDropdown.grid(column=1, row=1, padx=10, pady=10)
        self.tiebreakerDropdown.current(0)
        self.tiebreakerChoice = self.tiebreakerDropdown.get()
        self.tiebreakerDropdown.bind('<<ComboboxSelected>>', self.updateTiebreakerChoice)
        
        # Create first dis-allowed pairing label:
        pairingLabel1 = tk.Label(settings, text='RAs who cannot share a shift:')
        pairingLabel1.grid(column=0, row=2, padx=10, pady=10)
        # Create first dis-allowed pairing first RA dropdown menu:
        self.pairingDropdown1 = tk.ttk.Combobox(settings, values=names, state='readonly')
        self.pairingDropdown1.grid(column=1, row=2, padx=10, pady=10)
        self.pairingDropdown1.bind('<<ComboboxSelected>>', self.updatePairingOne)
        # Create first dis-allowed pairing label:
        pairingLabel2 = tk.Label(settings, text='and')
        pairingLabel2.grid(column=2, row=2, padx=10, pady=10)
        # Create first dis-allowed pairing first RA dropdown menu:
        self.pairingDropdown2 = tk.ttk.Combobox(settings, values=names, state='readonly')
        self.pairingDropdown2.grid(column=3, row=2, padx=10, pady=10)
        self.pairingDropdown2.bind('<<ComboboxSelected>>', self.updatePairingTwo)
        
        # Create second dis-allowed pairing label:
        pairingLabel1 = tk.Label(settings, text='Second pair of RAs who cannot share a shift:')
        pairingLabel1.grid(column=0, row=3, padx=10, pady=10)
        # Create first dis-allowed pairing first RA dropdown menu:
        self.pairingDropdown3 = tk.ttk.Combobox(settings, values=names, state='readonly')
        self.pairingDropdown3.grid(column=1, row=3, padx=10, pady=10)
        self.pairingDropdown3.bind('<<ComboboxSelected>>', self.updatePairingThree)
        # Create second dis-allowed pairing label:
        pairingLabel2 = tk.Label(settings, text='and')
        pairingLabel2.grid(column=2, row=3, padx=10, pady=10)
        # Create first dis-allowed pairing first RA dropdown menu:
        self.pairingDropdown4 = tk.ttk.Combobox(settings, values=names, state='readonly')
        self.pairingDropdown4.grid(column=3, row=3, padx=10, pady=10)
        self.pairingDropdown4.bind('<<ComboboxSelected>>', self.updatePairingFour)
        
        # Create save button:
        saveSettings = tk.Button(settings, text='Save', command=self.saveSettingsChoices)
        saveSettings.grid(column=1, row=4, padx=10, pady=10)
        
        # Start screen:
        settings.update()
        return None
    
    def saveSettingsChoices(self):
        '''
            None -> None
            This calls input.py's function to save the settings
            This also closes the settings window
        '''
        # TODO call input's function(s)
        # TODO include error checking for the pairing choices
            # an RA cannot be paired with theirself
            # an RA cannot be paired with 'no one'
        print(self.goldStarChoice)
        print(self.tiebreakerChoice)
        print(self.pairingChoice1)
        print(self.pairingChoice2)
        print(self.pairingChoice3)
        print(self.pairingChoice4)
        #self.settingsSaved = True # TODO
        self.closeSettings()
        return None
    
    def closeSettings(self):
        '''
            None -> None
            This closes the settings window
            It resets the Preference Settings Tracker variables
        '''
        self.settings.destroy()
        self.settings = None
        self.settingsIDs = None
        self.settingsNames = None
        # Dropdown menus
        self.goldStarDropdown = None
        self.tiebreakerDropdown = None
        self.pairingDropdown1 = None
        self.pairingDropdown2 = None
        self.pairingDropdown3 = None
        self.pairingDropdown4 = None
        # Selected in dropdowns
        self.goldStarChoice = None
        self.tiebreakerChoice = None
        self.pairingChoice1 = None
        self.pairingChoice2 = None
        self.pairingChoice3 = None
        self.pairingChoice4 = None
        return None
    
    def updateGoldStarChoice(self, event):
        '''
            This updates the selected RA in the gold star dropdown menu
        '''
        self.goldStarChoice = self.goldStarDropdown.get()
        return None
    
    def updateTiebreakerChoice(self, event):
        '''
            This updates the selected tiebreaker choice in the dropdown menu
        '''
        self.tiebreakerChoice = self.tiebreakerDropdown.get()
        return None
    
    def updatePairingOne(self, event):
        '''
            This updates the selected RA in the first dropdown menu for the first dis-allowed pair
        '''
        self.pairingChoice1 = self.pairingDropdown1.get()
        return None
    
    def updatePairingTwo(self, event):
        '''
            This updates the selected RA in the second dropdown menu for the first dis-allowed pair
        '''
        self.pairingChoice2 = self.pairingDropdown2.get()
        return None
    
    def updatePairingThree(self, event):
        '''
            This updates the selected RA in the first dropdown menu for the second dis-allowed pair
        '''
        self.pairingChoice3 = self.pairingDropdown3.get()
        return None
    
    def updatePairingFour(self, event):
        '''
            This updates the selected RA in the second dropdown menu for the second dis-allowed pair
        '''
        self.pairingChoice4 = self.pairingDropdown4.get()
        return None
    
    
    ''' The following function is for testing '''
    def testButton(self):
        '''
            None -> None
            This function is used to test the pressing of buttons
        '''
        print('Button Pressed') # Prints to terminal
        return None
    
if __name__ == "__main__":
    screen = OnCallViewer()
    screen.home()