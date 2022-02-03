import os 

dir = "Aula-"
numAula = 1

for i in range(0, 31):

	if numAula < 10:
		numAulaString = "0" + str(numAula)
	else:
		numAulaString = str(numAula)
	
	numAula += 1
	dirName = dir + numAulaString
	os.makedirs(dirName)