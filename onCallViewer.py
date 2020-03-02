'''
    Author: Lily Jim
    Date of last modification: 2-28-2020
    Description: This creates the graphical user interface
    References:
        On Deck Development Team's Project 1 interface.py file
        Tkinter ComboBox: https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-combobox/
        Tkinter Grid: https://www.tutorialspoint.com/python/tk_grid.htm
        Tkinter Button: https://www.tutorialspoint.com/python/tk_button.htm
        Tkinter Button Config Options: https://effbot.org/tkinterbook/button.htm
        Tkinter Button Text Config: https://pythonexamples.org/python-tkinter-button-change-font/
        Tkinter variable: https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/
        Tkinter wait_variable: http://www.scoberlin.de/content/media/http/informatik/tkinter/x8996-event-processing.htm and https://stackoverflow.com/questions/44790449/making-tkinter-wait-untill-button-is-pressed
        Tkinter Scrollbar: https://stackoverflow.com/questions/43731784/tkinter-canvas-scrollbar-with-grid
        List methods: https://www.geeksforgeeks.org/python-list/ and https://www.programiz.com/python-programming/methods/list/index
        Dictionary methods: https://www.geeksforgeeks.org/iterate-over-a-dictionary-in-python/ and https://www.geeksforgeeks.org/get-method-dictionaries-python/
        Button with args: https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
'''

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font

import importlib
from functools import partial

import input
import output
import raPreferences as raPrefs
import shiftAssignments as sa

# TODO call weekendsOffCheck
# TODO don't let duplicate windows open
# TODO dropdown lists of RAs should have 'none' as an option
# TODO require 10 RAs to generate schedule
# TODO limit max RAs
# TODO "header" labels to RA preferences
# TODO set column/row sizes
# TODO add delete all RAs button
# TODO add clear/delete schedule button
# TODO add warnings/messages when clicking buttons

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
        self.prefEdit = None
        self.schedEdit = None
        
        # RA Preferences Tracker:
        self.raIDs = None
        self.raNames = None
        self.delRaDropdown = None
        self.raSelectedToDelete = None
        
        # RA Preference Edit Tracker:
        self.weekdayOptions = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
        self.weekdayDropdown = None
        self.weekdayChoice = None
        self.weekendOptions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.weekendDropdown = None
        self.weekendChoice = None
        
        # Schedule Edit Tracker:
        self.scheduleNames = None
        self.changeRaDropdown = None
        self.changeRaChoice = None
        
        # Preference Settings Tracker:
        self.settingsSaved = False
        self.settingsClosed = tk.BooleanVar(self.root, True)
        self.settingsIDs = None
        self.settingsNames = None
        self.tiebreakerOptions = ['Random', 'Alphabetical Order by Last Name', 'Numerical Order by ID Number']
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
        root.geometry('400x200+200+100') # width x height + x_offset + y_offset
        root.minsize(400, 200)
        
        # Create buttons:
        prefButton = tk.Button(root, text='RA Preferences', command=self.preferencesView)
        prefButton.pack(padx=50, side=tk.LEFT)
        
        scheduleButton = tk.Button(root, text='Schedule', command=self.scheduleView)
        scheduleButton.pack(padx=50, side=tk.LEFT)
        
        # Start screen:
        root.mainloop()
        return None
    
    
    
    
    
    ''' The following functions are for the RA Preferences window '''
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
        pref.minsize(400, 600)
        
        importlib.reload(raPrefs)
        numRAs = len(raPrefs.raPreferences)
        
        # Create undo button
        if(numRAs != 0):
            undoButton = tk.Button(pref, text='Undo', command=self.undoPreferences)
            undoButton.grid(column=0, row=0)
            if(len(input.inputUpdates) == 0):
                undoButton.configure(state='disabled')
        
            # Display current RAs in the system
            index = 0
            self.raIDs = []
            self.raNames = []
            for ra in raPrefs.raPreferences:
                if(ra != '1' and ra != '2' and ra != '3'):
                    self.raIDs.append(ra)
                    self.raNames.append(raPrefs.raPreferences.get(ra)[0])

                    # Show RA name
                    nameLabel = tk.Label(pref, text=raPrefs.raPreferences.get(ra)[0])
                    nameLabel.grid(column=0, row=index+1)

                    # Show weekday preferences
                    pref1 = tk.Button(pref, text=raPrefs.raPreferences.get(ra)[1], command=partial(self.editRA, index, 1))
                    pref1.grid(column=1, row=index+1)
                    pref2 = tk.Button(pref, text=raPrefs.raPreferences.get(ra)[2], command=partial(self.editRA, index, 2))
                    pref2.grid(column=2, row=index+1)
                    pref3 = tk.Button(pref, text=raPrefs.raPreferences.get(ra)[3], command=partial(self.editRA, index, 3))
                    pref3.grid(column=3, row=index+1)

                    # Show weekend off requests
                    pref4 = tk.Button(pref, text=raPrefs.raPreferences.get(ra)[4], command=partial(self.editRA, index, 4))
                    pref4.grid(column=4, row=index+1)
                    pref5 = tk.Button(pref, text=raPrefs.raPreferences.get(ra)[5], command=partial(self.editRA, index, 5))
                    pref5.grid(column=5, row=index+1)
                    pref6 = tk.Button(pref, text=raPrefs.raPreferences.get(ra)[6], command=partial(self.editRA, index, 6))
                    pref6.grid(column=6, row=index+1)

                    # Increase counter for widget placement
                    index += 1
        
        # Create import button:
        importPrefs = tk.Button(pref, text='Import Preferences', command=self.importPreferences)
        importPrefs.grid(column=1, row=numRAs+1, padx=50, pady=50)
        
        # Create RA deletion section:
        # Create Delete RA label
        delRaLabel = tk.Label(pref, text='Delete RA:')
        delRaLabel.grid(column=0, row=numRAs+2, padx=10, pady=10)
        # Create dropdown menu
        self.delRaDropdown = tk.ttk.Combobox(pref, values=self.raNames, state='readonly')
        self.delRaDropdown.grid(column=1, row=numRAs+2, padx=10, pady=10)
        self.delRaDropdown.bind('<<ComboboxSelected>>', self.selectedForDeletion)
        # Create deletion save button:
        saveDeletion = tk.Button(pref, text='Save', command=self.deleteRA)
        saveDeletion.grid(column=2, row=numRAs+2, padx=10, pady=10)
        
        # Start screen:
        pref.protocol('WM_DELETE_WINDOW', self.closePreferences)
        pref.update() # use update, not mainloop so other functions can still run
        return None
    
    def undoPreferences(self):
        '''
            None -> None
            Calls input.py's undo function
        '''
        input.Preferences.undo()
        self.closePreferences()
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
            pos = self.raNames.index(self.raSelectedToDelete)
            studentID = self.raIDs[pos]
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
            It resets the RA Preferences Tracker variables
        '''
        if self.prefEdit != None:
            self.prefEdit.destroy()
            self.prefEdit = None
            self.weekdayDropdown = None
            self.weekdayChoice = None
            self.weekendDropdown = None
            self.weekendChoice = None
        self.preferences.destroy()
        self.preferences = None
        self.raIDs = None
        self.raNames = None
        self.delRaDropdown = None
        self.raSelectedToDelete = None
        return None
    
    
    
    
    
    ''' The following functions are for the Edit RA Preference window '''
    # TODO prevent this window from opening if one is already open
    def editRA(self, ra, field):
        '''
            int, int, int -> None
            This opens a new window and allows the user to input a new preference for an RA
        '''
        # Setup RA edit window:
        self.prefEdit = tk.Toplevel()
        prefEdit = self.prefEdit
        prefEdit.title('On Call - Edit RA Preference')
        prefEdit.geometry('500x100+400+300') # width x height + x_offset + y_offset
        prefEdit.minsize(500, 100)
        
        # Create label with RA's name:
        nameLabel = tk.Label(prefEdit, text=self.raNames[ra])
        nameLabel.grid(column=0, row=0, padx=10, pady=10)
        
        # Create label and dropdown menu for new preference:
        if(field <= 3):
            prefLabel = tk.Label(prefEdit, text=('Weekday Preference #%d:' % (field)))
            prefLabel.grid(column=1, row=0, padx=10, pady=10)
            self.weekdayDropdown = tk.ttk.Combobox(prefEdit, values=self.weekdayOptions, state='readonly')
            self.weekdayDropdown.grid(column=2, row=0, padx=10, pady=10)
            self.weekdayDropdown.bind('<<ComboboxSelected>>', self.updateWeekdayChoice)
        else:
            prefLabel = tk.Label(prefEdit, text=('Weekend Off Preference #%d:' % (field - 3)))
            prefLabel.grid(column=1, row=0, padx=10, pady=10)
            self.weekendDropdown = tk.ttk.Combobox(prefEdit, values=self.weekendOptions, state='readonly')
            self.weekendDropdown.grid(column=2, row=0, padx=10, pady=10)
            self.weekendDropdown.bind('<<ComboboxSelected>>', self.updateWeekendChoice)
        
        # Create save button:
        savePref = tk.Button(prefEdit, text='Save', command=partial(self.updateRA, ra, field))
        savePref.grid(column=1, row=1, padx=10, pady=10)
        
        prefEdit.protocol('WM_DELETE_WINDOW', self.closeEditRA)
        prefEdit.update()
        
        return None
    
    def updateRA(self, ra, field):
        '''
            int, int -> None
            This updates an RA's preference to the selected choice in the dropdown menu
            When the user clicks save when updating an RA's preference field, this function will get called
            This calls input's updatePreferences function
        '''
        if(field <= 3):
            input.Preferences.updatePreferences(self.raIDs[ra], field, self.weekdayChoice)
        else:
            input.Preferences.updatePreferences(self.raIDs[ra], field, self.weekendChoice)
        self.closeEditRA()
        self.closePreferences()
        return None
    
    def closeEditRA(self):
        '''
            None -> None
            This closes the Edit RA Preferences window
            It resets the RA Preference Edit Tracker variables
        '''
        self.prefEdit.destroy()
        self.prefEdit = None
        self.weekdayDropdown = None
        self.weekdayChoice = None
        self.weekendDropdown = None
        self.weekendChoice = None
        return None
    
    
    
    
    
    ''' The following functions are for the Schedule window '''
    def scheduleView(self):
        '''
            None -> None
            This creates the schedule screen
        '''
        # Setup schedule window:
        self.schedule = tk.Toplevel()
        sched = self.schedule
        sched.title('On Call - Schedule')
        sched.geometry('1500x800+0+0') # width x height + x_offset + y_offset
        sched.minsize(400, 400)
        
        importlib.reload(sa)
        # Only show schedule if there is a schedule
        if(len(sa.shiftAssignments) != 0):
            # Create undo button
            undoButton = tk.Button(sched, text='Undo', command=self.undoShiftChange)
            undoButton.grid(column=0, row=0)
            if(len(output.outputUpdates) == 0):
                undoButton.configure(state='disabled')
            
            # Display 'headers' for the schedule
            sundayDay = tk.Label(sched, text='Sunday Day')
            sundayDay.grid(column=1, row=1)
            sundayNight = tk.Label(sched, text='Sunday Night')
            sundayNight.grid(column=2, row=1)
            monday = tk.Label(sched, text='Monday')
            monday.grid(column=3, row=1)
            tuesday = tk.Label(sched, text='Tuesday')
            tuesday.grid(column=4, row=1)
            wednesday = tk.Label(sched, text='Wednesday')
            wednesday.grid(column=5, row=1)
            thursday = tk.Label(sched, text='Thursday')
            thursday.grid(column=6, row=1)
            friday = tk.Label(sched, text='Friday')
            friday.grid(column=7, row=1)
            saturdayDay = tk.Label(sched, text='Saturday Day')
            saturdayDay.grid(column=8, row=1)
            saturdayNight = tk.Label(sched, text='Saturday Day')
            saturdayNight.grid(column=9, row=1)
            
            # Display current schedule in the system
            for week in sa.shiftAssignments:
                # Primary RA row
                weekNum = tk.Label(sched, text=('Week %d Primary' % (week)))
                weekNum.grid(column=0, row=(week*2))
                slot1 = tk.Button(sched, text=sa.shiftAssignments[week][0][0], command=partial(self.editSchedule, week, 0, 0))
                slot1.grid(column=1, row=(week*2))
                slot2 = tk.Button(sched, text=sa.shiftAssignments[week][0][1], command=partial(self.editSchedule, week, 0, 1))
                slot2.grid(column=2, row=(week*2))
                slot3 = tk.Button(sched, text=sa.shiftAssignments[week][0][2], command=partial(self.editSchedule, week, 0, 2))
                slot3.grid(column=3, row=(week*2))
                slot4 = tk.Button(sched, text=sa.shiftAssignments[week][0][3], command=partial(self.editSchedule, week, 0, 3))
                slot4.grid(column=4, row=(week*2))
                slot5 = tk.Button(sched, text=sa.shiftAssignments[week][0][4], command=partial(self.editSchedule, week, 0, 4))
                slot5.grid(column=5, row=(week*2))
                slot6 = tk.Button(sched, text=sa.shiftAssignments[week][0][5], command=partial(self.editSchedule, week, 0, 5))
                slot6.grid(column=6, row=(week*2))
                slot7 = tk.Button(sched, text=sa.shiftAssignments[week][0][6], command=partial(self.editSchedule, week, 0, 6))
                slot7.grid(column=7, row=(week*2))
                slot8 = tk.Button(sched, text=sa.shiftAssignments[week][0][7], command=partial(self.editSchedule, week, 0, 7))
                slot8.grid(column=8, row=(week*2))
                slot9 = tk.Button(sched, text=sa.shiftAssignments[week][0][8], command=partial(self.editSchedule, week, 0, 8))
                slot9.grid(column=9, row=(week*2))
                # Secondary RA row
                weekNum = tk.Label(sched, text=('Week %d Secondary' % (week)))
                weekNum.grid(column=0, row=(week*2)+1)
                slot11 = tk.Button(sched, text=sa.shiftAssignments[week][1][0], command=partial(self.editSchedule, week, 1, 0))
                slot11.grid(column=1, row=(week*2)+1)
                slot12 = tk.Button(sched, text=sa.shiftAssignments[week][1][1], command=partial(self.editSchedule, week, 1, 1))
                slot12.grid(column=2, row=(week*2)+1)
                slot13 = tk.Button(sched, text=sa.shiftAssignments[week][1][2], command=partial(self.editSchedule, week, 1, 2))
                slot13.grid(column=3, row=(week*2)+1)
                slot14 = tk.Button(sched, text=sa.shiftAssignments[week][1][3], command=partial(self.editSchedule, week, 1, 3))
                slot14.grid(column=4, row=(week*2)+1)
                slot15 = tk.Button(sched, text=sa.shiftAssignments[week][1][4], command=partial(self.editSchedule, week, 1, 4))
                slot15.grid(column=5, row=(week*2)+1)
                slot16 = tk.Button(sched, text=sa.shiftAssignments[week][1][5], command=partial(self.editSchedule, week, 1, 5))
                slot16.grid(column=6, row=(week*2)+1)
                slot17 = tk.Button(sched, text=sa.shiftAssignments[week][1][6], command=partial(self.editSchedule, week, 1, 6))
                slot17.grid(column=7, row=(week*2)+1)
                slot18 = tk.Button(sched, text=sa.shiftAssignments[week][1][7], command=partial(self.editSchedule, week, 1, 7))
                slot18.grid(column=8, row=(week*2)+1)
                slot19 = tk.Button(sched, text=sa.shiftAssignments[week][1][8], command=partial(self.editSchedule, week, 1, 8))
                slot19.grid(column=9, row=(week*2)+1)
        else:
            # Show message that there is not a schedule in the system
            noSchedLabel = tk.Label(sched, text='No Existing Schedule\nPlease Generate New Schedule')
            noSchedLabel.grid(column=0, row=0)
        
        # Create Generate button:
        generateSched = tk.Button(sched, text='Generate New Schedule', command=self.generateNewSchedule)
        generateSched.grid(column=0, row=22, pady=50)
        
        # Create export button:
        exportSched = tk.Button(sched, text='Export Schedule', command=self.exportSchedule)
        exportSched.grid(column=0, row=23)
        
        # Start screen:
        sched.update() # use update, not mainloop so other functions can still run
        return None
    
    def undoShiftChange(self):
        '''
            None -> None
            This calls output.py's undo function
        '''
        output.undo()
        self.closeSchedule()
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
        inputGood = input.Preferences.weekendsOffCheck()
        if(inputGood == 0):
            self.settingsSaved = False
            self.settingsClosed.set(False)
            self.settingsView()
            self.root.wait_variable(self.settingsClosed)
            if(self.settingsSaved):
                error = output.generateSchedule()
                # TODO handle error
        elif(inputGood == 1):
            tk.messagebox.showerror(message='A schedule cannot be generated:\nA minimum of 10 RAs are needed.')
        elif(inputGood == 2):
            tk.messagebox.showerror(message='A schedule cannot be generated:\nMore than half the RA team has requested the same weekend off.')
            
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
    
    def closeSchedule(self):
        '''
            None -> None
            This closes the schedule window
        '''
        self.schedule.destroy()
        self.schedule = None
        return None
    
    
    
    
    
    ''' The following functions are for the Edit Schedule window '''
    # TODO prevent this window from opening if one is already open
    def editSchedule(self, weekNum, secondary, index):
        '''
            int, int, int -> None
            This creates the screen to update a shift in the schedule
        '''
        # Setup schedule edit window:
        self.schedEdit = tk.Toplevel()
        schedEdit = self.schedEdit
        schedEdit.title('On Call - Edit Schedule')
        schedEdit.geometry('400x200+400+300') # width x height + x_offset + y_offset
        schedEdit.minsize(400, 200)
        
        # Get RA info for dropdown menu:
        importlib.reload(raPrefs)
        self.scheduleNames = []
        for ra in raPrefs.raPreferences:
            if(ra != '1' and ra != '2' and ra != '3'):
                self.scheduleNames.append(raPrefs.raPreferences.get(ra)[0])
        
        # Create label with shift getting changed:
        shifts = ['Sunday Day', 'Sunday Night', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday Day', 'Saturday Night']
        primaryLabel = 'Primary'
        if(secondary):
            primaryLabel = 'Secondary'
        changeShiftLabel = tk.Label(schedEdit, text=('Change %s Week %d %s Shift:' % (shifts[index], weekNum, primaryLabel)))
        changeShiftLabel.grid(column=0, row=0, padx=10, pady=10)
        
        # Create dropdown menu for new shift assignment:
        self.changeRaDropdown = tk.ttk.Combobox(schedEdit, values=self.scheduleNames, state='readonly')
        self.changeRaDropdown.grid(column=0, row=1, padx=10, pady=10)
        self.changeRaDropdown.bind('<<ComboboxSelected>>', self.updateChangeRaChoice)
        
        # Create save button:
        saveChange = tk.Button(schedEdit, text='Save', command=partial(self.updateShift, weekNum, secondary, index))
        saveChange.grid(column=0, row=2, padx=10, pady=10)
        
        schedEdit.protocol('WM_DELETE_WINDOW', self.closeEditSchedule)
        schedEdit.update()
        return None
    
    def updateShift(self, weekNum, secondary, index):
        '''
            int, int, int -> None
            This updates the chosen field in the schedule
            This calls output's function
        '''
        output.updateSchedule(weekNum, secondary, index, self.changeRaChoice)
        self.closeEditSchedule()
        self.closeSchedule()
        return None
    
    def closeEditSchedule(self):
        '''
            None -> None
            This closes the Edit Schedule window
            It resets the Schedule Edit Tracker variables
        '''
        self.schedEdit.destroy()
        self.schedEdit = None
        self.scheduleNames = None
        self.changeRaDropdown = None
        self.changeRaChoice = None
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
            if(ra != '1' and ra != '2' and ra != '3'):
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
        settings.protocol('WM_DELETE_WINDOW', self.closeSettings)
        settings.update()
        return None
    
    def saveSettingsChoices(self):
        '''
            None -> None
            This calls input.py's function to save the settings
            This also closes the settings window
        '''
        # TODO include error checking for the pairing choices
            # an RA cannot be paired with theirself
            # an RA cannot be paired with 'no one'
        # TODO remove print statements
        
        # Handle gold star choice
        nameIndex = self.settingsNames.index(self.goldStarChoice)
        input.Preferences.setGoldStar(self.settingsIDs[nameIndex])
        #print(self.goldStarChoice, self.settingsIDs[nameIndex])
        
        # Handle tiebreaker choice
        tiebreakerIndex = self.tiebreakerOptions.index(self.tiebreakerChoice)
        input.Preferences.setTiebreaker(tiebreakerIndex)
        #print(self.tiebreakerChoice, self.tiebreakerOptions.index(self.tiebreakerChoice))
        
        # Handle bad pairing choices
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        if(self.pairingChoice1 != None and self.pairingChoice2 != None):
            pairingIndex1 = self.settingsNames.index(self.pairingChoice1)
            pairingIndex2 = self.settingsNames.index(self.pairingChoice2)
            p1 = self.settingsIDs[pairingIndex1]
            p2 = self.settingsIDs[pairingIndex2]
        if(self.pairingChoice3 != None and self.pairingChoice4 != None):
            pairingIndex3 = self.settingsNames.index(self.pairingChoice3)
            pairingIndex4 = self.settingsNames.index(self.pairingChoice4)
            p3 = self.settingsIDs[pairingIndex3]
            p4 = self.settingsIDs[pairingIndex4]
        input.Preferences.setBadPairings(p1, p2, p3, p4)
        #print(self.pairingChoice1, p1)
        #print(self.pairingChoice2, p2)
        #print(self.pairingChoice3, p3)
        #print(self.pairingChoice4, p4)
        
        # Close window
        self.settingsSaved = True
        self.closeSettings()
        self.closeSchedule() # close schedule window to force a refresh
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
        self.settingsClosed.set(True)
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
    
    
    
    
    
    ''' The following functions are for testing '''
    def testButton(self):
        '''
            None -> None
            This function is used to test the pressing of buttons
        '''
        print('Button Pressed') # Prints to terminal
        return None
    
    def testRaEdit(self, ra, field):
        '''
            int -> None
            This function was created to test how the edit RA preferences button works
        '''
        print(ra, field)
        return None
    
    def testSchedEdit(self, week, secondary, index):
        '''
            int, int, int -> None
            This function was created to test how the edit schedule button works
        '''
        print(week, secondary, index)
        return None
    
    
    
    
    
    ''' The following functions are for tracking dropdown menus '''
    def updateWeekdayChoice(self, event):
        '''
            This updates the selected weekday choice in the dropdown menu
            Dropdown menu is in Edit RA Preference window
        '''
        self.weekdayChoice = self.weekdayDropdown.get()
        return None
    
    def updateWeekendChoice(self, event):
        '''
            This updates the selected weekend choice in the dropdown menu
            Dropdown menu is in Edit RA Preference window
        '''
        self.weekendChoice = self.weekendDropdown.get()
        return None
    
    def updateChangeRaChoice(self, event):
        '''
            This updates the selected RA in the dropdown menu
            Dropdown menu is in Edit Schedule window
        '''
        self.changeRaChoice = self.changeRaDropdown.get()
        return None
    
    def updateGoldStarChoice(self, event):
        '''
            This updates the selected RA in the gold star dropdown menu
            Dropdown menu is in Settings window
        '''
        self.goldStarChoice = self.goldStarDropdown.get()
        return None
    
    def updateTiebreakerChoice(self, event):
        '''
            This updates the selected tiebreaker choice in the dropdown menu
            Dropdown menu is in Settings window
        '''
        self.tiebreakerChoice = self.tiebreakerDropdown.get()
        return None
    
    def updatePairingOne(self, event):
        '''
            This updates the selected RA in the first dropdown menu for the first dis-allowed pair
            Dropdown menu is in Settings window
        '''
        self.pairingChoice1 = self.pairingDropdown1.get()
        return None
    
    def updatePairingTwo(self, event):
        '''
            This updates the selected RA in the second dropdown menu for the first dis-allowed pair
            Dropdown menu is in Settings window
        '''
        self.pairingChoice2 = self.pairingDropdown2.get()
        return None
    
    def updatePairingThree(self, event):
        '''
            This updates the selected RA in the first dropdown menu for the second dis-allowed pair
            Dropdown menu is in Settings window
        '''
        self.pairingChoice3 = self.pairingDropdown3.get()
        return None
    
    def updatePairingFour(self, event):
        '''
            This updates the selected RA in the second dropdown menu for the second dis-allowed pair
            Dropdown menu is in Settings window
        '''
        self.pairingChoice4 = self.pairingDropdown4.get()
        return None



if __name__ == "__main__":
    screen = OnCallViewer()
    screen.home()
    
    
'''Alternate Code

def preferencesView(self):
        # Setup preferences window:
        self.preferences = tk.Toplevel()
        pref = self.preferences
        pref.title('On Call - RA Preferences')
        pref.geometry('700x400+250+150') # width x height + x_offset + y_offset
        pref.minsize(700, 400)
        pref.maxsize(700, 400)
        
        # Set up main frame
        prefMain = tk.Frame(pref)
        prefMain.grid(sticky='news') # Frame extends to north, east, west, and south of the window
        prefMain.grid_rowconfigure(0, weight=1) # TODO find out if this line is necessary
        prefMain.grid_columnconfigure(0, weight=1) # TODO find out if this line is necessary
        prefMain.grid_propagate(False)
        prefMain.config(width=700, height=400)
        # Create Canvas with scrollbar
        canvas = tk.Canvas(prefMain)
        canvas.grid(column=0, row=0, sticky='news')
        scroll = tk.Scrollbar(prefMain, orient="vertical", command=canvas.yview)
        scroll.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=scroll.set)
        prefWidgets = tk.Frame(canvas)
        canvas.create_window((0, 0), window=prefWidgets, anchor='nw')
        
        importlib.reload(raPrefs)
        numRAs = len(raPrefs.raPreferences)
        
        if(numRAs != 0):
            # Create undo button
            undoButton = tk.Button(prefWidgets, text='Undo', command=self.undoPreferences)
            undoButton.grid(column=0, row=0)
            if(len(input.inputUpdates) == 0):
                undoButton.configure(state='disabled')
            
            # TODO add 'header' labels to prefMain
            # labels in row 1
            
            # Create RA list frame
            #prefList = tk.Frame(prefMain)
            #prefList.grid(row=2, column=1, sticky='nw')
            #prefList.grid_rowconfigure(0, weight=1) # TODO find out if this line is necessary
            #prefList.grid_columnconfigure(0, weight=1) # TODO find out if this line is necessary
            #prefList.grid_propagate(False)
            #prefList.config(width=800, height=300)
            
            # Create canvas for the list frame
            #canvas = tk.Canvas(prefList)
            #canvas.grid(row=0, column=0, sticky="news")
            
            # Link a scrollbar to the canvas
            #scroll = tk.Scrollbar(prefList, orient="vertical", command=canvas.yview)
            #scroll.grid(row=0, column=1, sticky='ns')
            #canvas.configure(yscrollcommand=scroll.set)
            
            # Create a frame to contain the buttons
            #frameButtons = tk.Frame(canvas)
            #canvas.create_window((0, 0), window=frameButtons, anchor='nw')
            
            # Display current RAs in the system
            index = 0
            self.raIDs = []
            self.raNames = []
            for ra in raPrefs.raPreferences:
                if(ra != '1' and ra != '2' and ra != '3'):
                    self.raIDs.append(ra)
                    self.raNames.append(raPrefs.raPreferences.get(ra)[0])
                    # TODO set column/row sizes

                    # Show RA name
                    nameLabel = tk.Label(prefWidgets, text=raPrefs.raPreferences.get(ra)[0])
                    nameLabel.grid(column=0, row=index+1, sticky='news')

                    # Show weekday preferences
                    pref1 = tk.Button(prefWidgets, text=raPrefs.raPreferences.get(ra)[1], command=partial(self.editRA, index, 1))
                    pref1.grid(column=1, row=index+1, sticky='news')
                    pref2 = tk.Button(prefWidgets, text=raPrefs.raPreferences.get(ra)[2], command=partial(self.editRA, index, 2))
                    pref2.grid(column=2, row=index+1, sticky='news')
                    pref3 = tk.Button(prefWidgets, text=raPrefs.raPreferences.get(ra)[3], command=partial(self.editRA, index, 3))
                    pref3.grid(column=3, row=index+1, sticky='news')

                    # Show weekend off requests
                    pref4 = tk.Button(prefWidgets, text=raPrefs.raPreferences.get(ra)[4], command=partial(self.editRA, index, 4))
                    pref4.grid(column=4, row=index+1, sticky='news')
                    pref5 = tk.Button(prefWidgets, text=raPrefs.raPreferences.get(ra)[5], command=partial(self.editRA, index, 5))
                    pref5.grid(column=5, row=index+1, sticky='news')
                    pref6 = tk.Button(prefWidgets, text=raPrefs.raPreferences.get(ra)[6], command=partial(self.editRA, index, 6))
                    pref6.grid(column=6, row=index+1, sticky='news')

                    # Increase counter for widget placement
                    index += 1
            
            # Update buttons frames idle tasks to let tkinter calculate buttons sizes
            #frameButtons.update_idletasks()
            
            # Set the canvas scrolling region
            #canvas.config(scrollregion=canvas.bbox("all"))
        
        # TODO add scrollbar
        
        # Create import button:
        importPrefs = tk.Button(prefWidgets, text='Import Preferences', command=self.importPreferences)
        importPrefs.grid(column=1, row=numRAs+2, padx=50, pady=50)
        
        # Create RA deletion section:
        # Create Delete RA label
        delRaLabel = tk.Label(prefWidgets, text='Delete RA:')
        delRaLabel.grid(column=0, row=numRAs+3, padx=10, pady=10)
        # Create dropdown menu
        self.delRaDropdown = tk.ttk.Combobox(prefWidgets, values=self.raNames, state='readonly')
        self.delRaDropdown.grid(column=1, row=numRAs+3, padx=10, pady=10)
        self.delRaDropdown.bind('<<ComboboxSelected>>', self.selectedForDeletion)
        # Create deletion save button:
        saveDeletion = tk.Button(prefWidgets, text='Save', command=self.deleteRA)
        saveDeletion.grid(column=2, row=numRAs+3, padx=10, pady=10)
        
        # TODO add delete all RAs button?
        
        # Start screen:
        prefWidgets.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        pref.protocol('WM_DELETE_WINDOW', self.closePreferences)
        pref.update() # use update, not mainloop so other functions can still run
        return None
'''