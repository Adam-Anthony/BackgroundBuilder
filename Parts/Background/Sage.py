## Sage
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def SageTables():
	result = 'Your background is a sage.' + newLine
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
	emb += ['I was naturally curious, so I packed up and went to a university to learn more about the world.']
	emb += ['my mentor\'s teachings opened my mind to new possibilities in that field of study.']
	emb += ['I was always an avid reader, and I learned much about my favorite topic on my own.']
	emb += ['I discovered an old library and pored over the texts I found there. That experience awakened a hunger for more knowledge.']
	emb += ['I impressed a wizard who told me I was squandering my talents and should seek out an education to take advantage of my gifts.']
	emb += ['One of my parents or a relative gave me a basic education that whetted my appetite, and I left home to build on what I had learned.']
	return ('I became a sage because ' + TableHelper.dSixTable(emb, roll) + newLine)