## Outlander
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def OutlanderTables():
	result = 'Your background is an outlander.' + newLine
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
	emb += ['I spent a lot of time in the wilderness as a youngster, and I came to love that way of life.']
	emb += ['from a young age, I couldn\'t abidethe stink of the cities and preferred to spend my time in nature.']
	emb += ['I came to understand the darkness that lurks in the wilds, and I vowed to combat it.']
	emb += ['my people lived on the edges of civilization, and I learned the methods of survival from my family.']
	emb += ['after a tragedy I retreated to the wilderness, leaving my old life behind.']
	emb += ['my family moved away from civilization, and I learned to adapt to my new environment.']
	return ('I became an outlander because ' + TableHelper.dSixTable(emb, roll) + newLine)