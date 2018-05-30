## Soldier
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def SoldierTables():
	result = 'Your background is a soldier.' + newLine
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
	emb += ['I joined the militia to help protect my community from monsters.']
	emb += ['a relative of mine was a soldier, and I wanted to carry on the family tradition.']
	emb += ['The local lord forced me to enlist in the army.']
	emb += ['War ravaged my homeland while I was growing up. Fighting was the only life I ever knew.']
	emb += ['I wanted fame and fortune, so I joined a mercenary company, selling my sword to the highest bidder.']
	emb += ['Invaders attacked my homeland. It was my duty to take up arms in defense of my people.']
	return ('I became a soldier because ' + TableHelper.dSixTable(emb, roll) + newLine)