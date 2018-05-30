## Hermit
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def HermitTables():
	result = 'Your background is a hermit.' + newLine
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
	emb += ['my enemies ruined my reputation, and I fled to the wilds to avoid further disparagement.']
	emb += ['I am comfortable with being isolated, as I seek inner peace.']
	emb += ['I never liked the people I called my friends, so it was easy for me to strike out on my own.']
	emb += ['I felt compelled to forsake my past, but did so with great reluctance, and sometimes I regret making that decision.']
	emb += ['I lost everything--my home, my family, my friends. Going it alone was all I could do.']
	emb += ['Society\'s decadence disgusted me, so I decided to leave it behind.']
	return ('I became a hermit because ' + TableHelper.dSixTable(emb, roll) + newLine)