## Entertainer
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def EntertainerTables():
	result = 'Your background is an entertainer.' + newLine
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
	emb += ['members of my family made ends meet by performing, so it was fitting for me to follow their example.']
	emb += ['I always had a keen insight into other people, enough so that I could make them laugh or cry with my stories or songs.']
	emb += ['I ran away from home to follow a minstrel troupe.']
	emb += ['I saw a bard perform once, and I knew from that moment on what I was born to do.']
	emb += ['I earned coin by performing on street corners and eventually made a name for myself.']
	emb += ['A traveling entertainer took me in and taught me the trade.']
	return ('I became an entertainer because ' + TableHelper.dSixTable(emb, roll) + newLine)