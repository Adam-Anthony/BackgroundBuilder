## Folk Hero
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def FolkHeroTables():
	result = 'Your background is a folk hero.' + newLine
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
	emb += ['I learned what was right and wrong from my family.']
	emb += ['I was always enamored by tales of heroes and wished I could be something more than ordinary.']
	emb += ['I hated my mundane life, so when it was time for someone to step up and do the right thing, I took my chance.']
	emb += ['a parent or one of my relatives was an adventurer, and I was inspired by that person\'s courage.']
	emb += ['a mad old hermit spoke a prophecy when I was born, saying that I would accomplish great things.']
	emb += ['I have always stood up for those who are weaker than I am.']
	return ('I became a folk hero because ' + TableHelper.dSixTable(emb, roll) + newLine)