## Noble
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def NobleTables():
	result = 'Your background is a noble.' + newLine
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
	emb += ['I come from an old and storied family, and it fell to me to preserve the family name.']
	emb += ['my family has been disgraced, and I intend to clear our name.']
	emb += ['my family recently came by its title, and that elevation thrust us into a new and strange world.']
	emb += ['my family has a title, but none of my ancestors have distinguished themselves since we gained it.']
	emb += ['my family is filled with remarkable people. I hope to live up to their example.']
	emb += ['I hope to increase my family\'s power and influence.']
	return ('I became a noble because ' + TableHelper.dSixTable(emb, roll) + newLine)