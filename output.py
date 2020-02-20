'''
	Author: Kiana Hosaka
	Date of Last Modification: February 20, 2020
	Description: File produces the functionality of the Shift Assignments Module.
	References:
	- Prepending to a list: https://kite.com/python/answers/how-to-prepend-to-a-list-in-python

'''
#TODO: What kind of errors could occur?

import importlib
import shiftAssignments as sa
import test_week as week # For testing
import test_end as end # For testing


# Global dictionary that will get written to shiftAssignments.py

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
	
	# File containing shift assignment dictionary
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

	# Writing assignment dictionary to shiftAssignments.py
	f.write("shiftAssignments = %s\n" % (str(assignments)))
	f.close()

	return 0


def exportFile(fileName):
	'''
		(Name of file: str) -> int

		Receives the name of the file to export to. This function 
		exports the saved shift assignments to a specified CSV file. 
		Returns 0 if no errors occured or 1 if an error occured.
	'''

	importlib.reload(sa) # Reloading dictionary
	output_file = open(fileName, "w")
	output_file.write(",,,,---- RESIDENT ASSISTANT SHIFT ASSIGNMENTS -----\n\n")
	output_file.write(",,SUNDAY DAY, SUNDAY NIGHT, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, \
				FRIDAY, SATURDAY DAY, SATURDAY NIGHT\n")	

	for week in sa.shiftAssignments:
		# Write week number
		output_file.write("Week %d," % (week))

		# Write primary schedule
		output_file.write(", %s, %s, %s, %s, %s, %s, %s, %s, %s \n" % \
				(sa.shiftAssignments[week][0][0], \
				sa.shiftAssignments[week][0][1], sa.shiftAssignments[week][0][2], \
				sa.shiftAssignments[week][0][3], sa.shiftAssignments[week][0][4], \
				sa.shiftAssignments[week][0][5], sa.shiftAssignments[week][0][6], \
				sa.shiftAssignments[week][0][7], sa.shiftAssignments[week][0][8]))

		# Write secondary schedule		
		output_file.write(",, %s, %s, %s, %s, %s, %s, %s, %s, %s \n" % \
				(sa.shiftAssignments[week][1][0], \
				sa.shiftAssignments[week][1][1], sa.shiftAssignments[week][1][2], \
				sa.shiftAssignments[week][1][3], sa.shiftAssignments[week][1][4], \
				sa.shiftAssignments[week][1][5], sa.shiftAssignments[week][1][6], \
				sa.shiftAssignments[week][1][7], sa.shiftAssignments[week][1][8]))

		output_file.write("\n")
			
	output_file.close()
	return 0

 
def updateSchedule(weekNum, secondary, index, newName):
	'''
		(Term week: int, Secondary?: int, Index of old name: int, New RA: str) -> int

		Receives an int indicating the week number, 0 if the RA is the primary 
		for the shift or 1 if they are secondary, an int indicating the field 
		in the list that was changed, and a str of the new name for that field.
		This function updates a field in the shiftAssignmnets dictionary.
		Returns 0 if no errors occured or 1 if an error occured.
	'''
	# Copy of the assignments
	importlib.reload(sa) # Reloading dictionary
	new_assignments = sa.shiftAssignments
	new_assignments[weekNum][secondary][index] = newName
	f = open("shiftAssignments.py", "w")
	f.write("shiftAssignments = %s\n" % (str(new_assignments)))
	f.close()

	return 0

# Call methods
# generateSchedule()
# exportFile("file_output.csv")
# updateSchedule(2, 0, 1, "KIANA")

