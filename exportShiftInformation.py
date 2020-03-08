import shiftAssignments as sa
import importlib

def exportShiftInfo(fileName):
	importlib.reload(sa)
	primaryInfo = {}
	secondaryInfo = {}
	cummulativeInfo = {}
	days = {0:"Sunday Day", 1:"Sunday Night", 2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday Day",8:"Saturday Night"}

	try:
		open(fileName, 'w')
	except:
		return 1

	for i in range(1,11):				#10 weeks
		primary = sa.shiftAssignments[i][0]
		secondary = sa.shiftAssignments[i][1]
		for ra in primary:
			if ra in primaryInfo.keys():
				primaryInfo[ra] += 1
			else:
				primaryInfo[ra] = 1		#number of primary shifts

		for ra in secondary:
			if ra in secondaryInfo.keys():
				secondaryInfo[ra] += 1
			else:
				secondaryInfo[ra] = 1		#number of secondary shifts

	for ra in primaryInfo.keys():
		cummulativeInfo[ra] = [primaryInfo[ra], secondaryInfo[ra]]

	for ra in cummulativeInfo:
		print(ra, ' ', cummulativeInfo[ra][0], ' ', cummulativeInfo[ra][1])

	print(cummulativeInfo)

	print(primaryInfo)
	print(secondaryInfo)

exportShiftInfo("test.txt")