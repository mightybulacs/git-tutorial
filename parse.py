with open("input.csv", "r") as handler:
	patients = []
	for line in handler:
		tokens = line.rstrip().split(",")
		patient = {}
		patient['name'] 	= tokens[0]
		patient['sequence'] = tokens[1]
		patient['age'] 		= int(tokens[2])
		patients.append(patient)
	print(patients)
		