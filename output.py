'''
	Author: Kiana Hosaka
	Date of Last Modification: February 19, 2020
	Description: File produces the functionality of the Shift Assignments Module.
	References:
	- Prepending to a list: https://kite.com/python/answers/how-to-prepend-to-a-list-in-python
'''
import shiftAssignments as sa
import test_week as week
import test_end as end


def generateSchedule():
	'''
		(None) -> int

		This function calls the schedulers and saves their returned information 
		into the raPreferences dictionary. Returns 0 if no errors occured or 1 if 
		an error occured.
	'''
	# For now, I am not "calling" the schedulers but I have created test files
	# for how the return of the schedulers would be

	assignments = {}
	f = open("shiftAssignments.py", "w")	

	# Adding the WEEKDAYS to the dictionary
	for i in range(11): # 11 weeks in a term
		assignments.update({i+1: [week.schedule[i][0], week.schedule[i][1]]})

	# Adding the WEEKENDS to the dictionary
	for i in range(11): # 11 weeks in a term
		assignments[i+1][0].insert(0, end.schedule[i][0][3]) # Prepending Primary Sunday Day
		assignments[i+1][1].insert(0, end.schedule[i][1][3]) # Prepending Secondary Sunday Day

		# Appending rest of weekend
		for j in range(3):
			assignments[i+1][0].append(end.schedule[i][0][j]) # Primary
			assignments[i+1][1].append(end.schedule[i][1][j]) # Secondary

	f.write("shiftAssignments = %s\n" % (str(assignments)))
	f.close()

	#TODO: What kind of errors could occur?
	return 0 # 0 if no errors occured or a 1 if an error occured


def exportFile(fileName):
	'''
		(Name of file: str) -> int

		Receives the name of the file to export to. This function 
		exports the saved shift assignments to a specified CSV file. 
		Returns 0 if no errors occured or 1 if an error occured.
	'''
	return # 0 if no errors occured or a 1 if an error occured

 
def updateSchedule(weekNum, secondary, index, newName):
	'''
		(Term week: int, Secondary?: int, Index of old name: int, New RA: str) -> int

		Receives an int indicating the week number, 0 if the RA is the primary 
		for the shift or 1 if they are secondary, an int indicating the field 
		in the list that was changed, and a str of the new name for that field.
		This function updates a field in the shiftAssignmnets dictionary.
		Returns 0 if no errors occured or 1 if an error occured.
	'''
	return # 0 if no errors occured or a 1 if an error occured

generateSchedule()
