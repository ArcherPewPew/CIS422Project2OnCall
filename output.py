'''
	Author: Kiana Hosaka
	Date of Last Modification: February 20, 2020
	Description: File produces the functionality of the Shift Assignments Module.
	References:
	- Prepending to a list: https://kite.com/python/answers/how-to-prepend-to-a-list-in-python

'''
#TODO: Add error checking

import importlib
import shiftAssignments as sa
import test_week as week # For testing
# import test_end as end # For testing
# import weekdayScheduler as week
import weekendScheduler as end # Alex's weekend scheduler

outputUpdates = [] # list of lists
# outputUpdates - [[weeknum, sec, index, old], ...]

def generateSchedule():
	'''
		(None) -> int

		Calls the schedulers and saves their returned information into the shiftAssignments dictionary. 
		Returns 0 if no errors occured or 1 if an error occured.
	'''

	# For now, I am not "calling" the schedulers but I have created test files
	# week_schedule = week.weekdayShifts()
	end_schedule = end.weekendShifts()

	# Dictionary that will get written to shiftAssignments.py
	assignments = {}
	
	# File containing shift assignment dictionary
	f = open("shiftAssignments.py", "w")	

	# Adding the WEEKDAYS to the dictionary
	for i in range(10): # 10 weeks in a term
		assignments.update({i+1: [week.schedule[i][0], week.schedule[i][1]]})

	# Adding the WEEKENDS to the dictionary
	for i in range(10): # 10 weeks in a term

		# Prepend Sunday Day
		# assignments[i+1][0].insert(0, end.schedule[i][0][3]) # Test
		# assignments[i+1][1].insert(0, end.schedule[i][1][3]) # Test
		assignments[i+1][0].insert(0, end_schedule[i][0][3]) # Prepending Primary Sunday Day
		assignments[i+1][1].insert(0, end_schedule[i][1][3]) # Prepending Secondary Sunday Day

		# Appending rest of weekend
		for j in range(3): # Friday, Saturday Day, Sunday Night
			# assignments[i+1][0].append(end.schedule[i][0][j]) # Test
			# assignments[i+1][1].append(end.schedule[i][1][j]) # Test
			assignments[i+1][0].append(end_schedule[i][0][j]) # Primary
			assignments[i+1][1].append(end_schedule[i][1][j]) # Secondary

	# Writing assignment dictionary to shiftAssignments.py
	f.write("shiftAssignments = %s\n" % (str(assignments)))

	f.close()
	return 0


def exportFile(fileName):
	'''
		(Name of file: str) -> int

		Receives the name of the file to export to.
		Exports the saved shift assignments to a specified CSV file. 
		Returns 0 if no errors occured or 1 if an error occured.
	'''
	
	importlib.reload(sa) # Reloading dictionary

	# Creating user inputted output file and headers
	output_file = open(fileName, "w")
	output_file.write(",,SUNDAY DAY,SUNDAY NIGHT,MONDAY,TUESDAY,WEDNESDAY,THURSDAY,"
				"FRIDAY,SATURDAY DAY,SATURDAY NIGHT\n")	

	# Go through the weeks of shiftAssignments dictionary and save into output file
	for week in sa.shiftAssignments:
		# Write week i's number
		output_file.write("Week %d," % (week))

		# Write week i's primary schedule
		output_file.write(", %s, %s, %s, %s, %s, %s, %s, %s, %s \n" % \
				(sa.shiftAssignments[week][0][0], \
				sa.shiftAssignments[week][0][1], sa.shiftAssignments[week][0][2], \
				sa.shiftAssignments[week][0][3], sa.shiftAssignments[week][0][4], \
				sa.shiftAssignments[week][0][5], sa.shiftAssignments[week][0][6], \
				sa.shiftAssignments[week][0][7], sa.shiftAssignments[week][0][8]))

		# Write week i's secondary schedule		
		output_file.write(",, %s, %s, %s, %s, %s, %s, %s, %s, %s \n" % \
				(sa.shiftAssignments[week][1][0], \
				sa.shiftAssignments[week][1][1], sa.shiftAssignments[week][1][2], \
				sa.shiftAssignments[week][1][3], sa.shiftAssignments[week][1][4], \
				sa.shiftAssignments[week][1][5], sa.shiftAssignments[week][1][6], \
				sa.shiftAssignments[week][1][7], sa.shiftAssignments[week][1][8]))

		output_file.write("\n")
			
	output_file.close()
	return 0

 
def rewriteSchedule(assignments):
	'''
		(Updated assignments: dict) -> None
		
		Recieves an updated assignments dictionary and rewrites the sa.shiftAssignments file.
		Called by updateScehdule(...) and undo().
		Returns 0.
	'''

	f = open("shiftAssignments.py", "w")
	f.write("shiftAssignments = %s\n" % (str(assignments)))
	f.close()

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
	#TODO: Does update schedule need to generate a new output file?

	# SAVE HERE(weekNum, secondary, index)	
	save(weekNum, secondary, index)

	# Copy of current shift assignments	
	importlib.reload(sa) # Reloading dictionary
	new_assignments = sa.shiftAssignments

	# Update new assignment 
	new_assignments[weekNum][secondary][index] = newName
	
	# Update shiftAssignments dictionary
	rewriteSchedule(new_assignments)
	'''
	f = open("shiftAssignments.py", "w")
	f.write("shiftAssignments = %s\n" % (str(new_assignments)))
	f.close()
	'''

	return 0


		
def save(weekNum, secondary, index):
	'''
		(Term week: int, Secondary?: int, Index of old name: int) -> int

		Receives an int indicating the week number, 0 if the RA is the primary
		for the shift or 1 if they are secondary, and an int indicating the field
		in the list that was changed.
		Saves the old values from shiftAssignments
	'''
	# Copy of shift assignments
	old_assignments = sa.shiftAssignments

	# Append to outputUpdates
	outputUpdates.append([weekNum, secondary, index, old_assignments])
	#print(outputUpdates)
	#print("save\n")

	return 0

def undo():
	'''
		() -> None
		
		Rewrites the sa.shiftAssignments with the previous state.
	'''
	# Getting the last state and removing from outputUpdates
	last_state = outputUpdates.pop()

	# Copy of current shift assignments
	importlib.reload(sa) # Reloading dictionary
	new_assignments = sa.shiftAssignments

	# Assigning all fields	
	weekNum = last_state[0]	
	secondary = last_state[1]
	index = last_state[2]
	old_assignments = last_state[3]

	# print("old assignments are:",  old_assignments)
	# Update shiftAssignments dictionary
	rewriteSchedule(old_assignments)
	'''
	f = open("shiftAssignments.py", "w")
	f.write("shiftAssignments = %s\n" % (str(old_assignments)))
	f.close()
	'''

	return 0

'''
	Calling methods to test program functionality.
'''
# generateSchedule()
# updateSchedule(2, 0, 1, "ALOOOHHHHAAAAAAAA")
# updateSchedule(10, 0, 0, "HOSAKA")
# print("main\n")
# print(sa.shiftAssignments)
# undo()
# print(sa.shiftAssignments)
