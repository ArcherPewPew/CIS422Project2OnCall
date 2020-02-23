'''
Author: Alyssa Huque
Date of last modification: 2-22-2020
Description: This produces the functionality of the RA Preferences module
References:
    TODO
'''

from datetime import datetime
import ast

class Input:
	# all of these are Alyssa's functions
	def __init__(self):
		pass

	def input_preferences(filename):
		'''file -> dictionary
		parses the file of RA preferences and adds to raPreferences dictionary
		'''
		with open(filename, "r") as file:
			contents = file.readlines()
			for i in range(len(contents)):
				contents[i] = contents[i].strip('\n')
				contents[i] = contents[i].split(',')
				# contents[i] = contents[i].split(',')
			for j in range(len(contents)): # error checking
				if contents[j][0][:3] != "951": # first field is not a student ID
					return 1
				raPreferences = {j[0]: j[1:8] for j in contents}
		file.close()
		return raPreferences

	def reading_dict_py(filename):
		'''file -> dictionary
		parses file with raPreferences dictionary
		'''
		with open(filename, "r") as file: # opens file
			contents = file.readlines() # reads lines
		for i in contents:
			raPreferences = i.strip("raPreferences = ") # stores only the dictionary and nothing more in roster_dict
		file.close()
		raPreferences = ast.literal_eval(raPreferences) # converts from string to dictionary
		return raPreferences

class Preferences:
	def __init__(self):
		# TODO
		pass

	def importFile(filename):
		'''string -> int
		Receives the name of the file to import
		This function imports RA preference information.
		The file may contain one or several RAs. This function also accounts for an empty file.
		The file may contain RAs who are already in the system. These RAs have their preferences updated.
		Returns a 0 if no errors occured or a 1 if an error occured
		'''
		updated_dict = Input.input_preferences(filename) #now i have a dictionary with the new information, I need to compare
		if(updated_dict == 1):
			return 1 # returns 1 for GUI warning
		original_dict = Input.reading_dict_py("raPreferences.py")

		dictionary = original_dict.copy()

		# adding new RAs
		added_RAs = list(updated_dict.keys() - original_dict.keys())
		for i in range(len(added_RAs)):
			dictionary[added_RAs[i]] = updated_dict.get(added_RAs[i])

		# updating RA information
		for key in original_dict.keys() & updated_dict.keys():
			dictionary[key][1:7] = updated_dict[key][1:7]

		file = open("raPreferences.py", "w+") # writes file for Queue
		file.write("raPreferences = %s\n" % (str(dictionary)))
		file.close()
		return 0 # 0 if no errors occured or a 1 if an error occured

	def deletePreferences(student_id):
		'''string -> int
		Receives the id number of the RA that needs to be deleted from
			the dictionary.
		This function removes the key/value pair of the given RA and
		rewrites the raPreferences dictionary.
		Returns a 0 if no errors occured or a 1 if an error occured
		'''
		current_dictionary = Input.reading_dict_py("raPreferences.py")
		del current_dictionary[student_id]

		file = open("raPreferences.py", "w+")
		file.write("raPreferences = %s\n" % (str(current_dictionary)))
		file.close()
		return 0 # 0 if no errors occured or a 1 if an error occured

	def saveSettings(self): # TODO determine how the preferences will be sent, perhaps separate functions
		'''
		'''
		# TODO
		return None

if __name__ == '__main__':
	Preferences.importFile("example.csv")
	# Preferences.importFile("example5.csv")
	# Preferences.importFile("updatedexample.csv")
	# Preferences.deletePreferences('951545641')
