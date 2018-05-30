## Guild Artisan
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def GuildArtisanTables():
	result = 'Your background is a guild artisan.' + newLine
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
	emb += ['I was apprenticed to a master who taught me the guild\'s business.']
	emb += ['I helped a guild artisan keep a secret or complete a task, and in return I was taken on as an apprentice.']
	emb += ['one of my family members who belonged to the guild made a place for me.']
	emb += ['I was always good with my hands, so I took the opportunity to learn a trade.']
	emb += ['I wanted to get away from my home situation and start a new life.']
	emb += ['I learned the essentials of my craft from a mentor but had to join the guild to finish my training.']
	return ('I became a guild artisan because ' + TableHelper.dSixTable(emb, roll) + newLine)