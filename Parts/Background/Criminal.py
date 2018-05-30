## Criminal ##
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def CriminalTables():
	result = 'Your background is a criminal.' + newLine
	result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    return result

def Trait():
	emb = []
	return Personality.Traits(emb)

def Ideal():
	emb = []
	return Personality.Ideals(emb)

def Bond():
	emb = []
	return Personality.Bonds(emb)

def Flaw():
	emb = []
	return Personality.Flaws(emb)

def Decision():
	roll = rng.randint(1,6)
	emb = []
	emb += ['I resented authority in my younger days and saw a life of crime as the best way to fight against tyranny and oppression.']
	emb += ['necessity forced me to take up the life, since it was the only way I could survive.']
	emb += ['I fell in with a gang of reprobates and ne\'er-do-wells, and I learned my specialty from them.']
	emb += ['a parent or relative taught me my criminal specialty to prepare me for the family business.']
	emb += ['I left home and found a place in a thieves\' guild or some other criminal organization.']
	emb += ['I was always bored, so I turned to crime to pass the time and discovered I was quite good at it.']
	return ('I became a criminal because ' + TableHelper.dSixTable(emb, roll) + newLine)