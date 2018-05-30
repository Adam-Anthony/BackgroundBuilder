## Urchin
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def UrchinTables():
	result = 'Your background is an urchin.' + newLine
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
	emb += ['wanderlust caused me to leave my family to se the world. I look after myself.']
	emb += ['I ran away from a bad situation at home and made my own way in the world.']
	emb += ['monsters wiped out my village, and I was the sole survivor. I had to find a way to survive.']
	emb += ['a notorious thief looked after me and other orphans, and we spied and stole to earn our keep.']
	emb += ['one day I woke up on the streets, alone and hungry, with no memory of my early childhood.']
	emb += ['my parents died, leaving no one to look after me. I raised myself.']
	return ('I became an urchin because ' + TableHelper.dSixTable(emb, roll) + newLine)