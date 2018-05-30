## Sailor
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def SailorTables():
	result = 'Your background is a sailor.' + newLine
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
	emb += ['I was press-ganged by pirates and forced to serve on their ship until I finally escaped.']
	emb += ['I wanted to see the world, so I signed on as a deckhand for a merchant ship.']
	emb += ['one of my relatives was a sailor who took me to sea.']
	emb += ['I needed to escape my community quickly, so I stowed away on a ship. When the crew found me, I was forced to work for my passage.']
	emb += ['Reavers attacked my community, so I found refuge on a ship until I could seek vengeance.']
	emb += ['I had few prospects where I was living, so I left to find my fortune elsewhere.']
	return ('I became a sailor because ' + TableHelper.dSixTable(emb, roll) + newLine)