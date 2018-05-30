def dSixTable(values, roll):
	return values[roll-1]

def dEightTable(values, roll):
	return values[roll-1]

def XdSixTable(values, rolls):
	q = []
	for x in range(0,len(rolls)):
		q += [values[rolls[x]]]
	return q

def XdEightTable(values, rolls):
	q = []
	for x in range(0,len(rolls)):
		q += [values[rolls[x]]]
	return q