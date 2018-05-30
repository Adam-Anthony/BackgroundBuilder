## Charlatan
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '
def CharlatanTables():
    result = 'Your background is a charlatan.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    result += Schemes()
    return result

def Trait():
    emb = []
    emb += ['I fall in and out of love easily, and am always pursuing someone.']
    emb += ['I have a joke for every occasion, especially occasions where humor is inappropriate.']
    emb += ['Flattery is my preferred trick for getting what I want.']
    emb += ['I\'m a born gambler who can\'t resist taking a risk for a potential payoff.']
    emb += ['I lie about almost everything, even when there\'s no good reason to.']
    emb += ['Sarcasm and insults are my weapons of choice.']
    emb += ['I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.']
    emb += ['I pocket anything I see that might have some value.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    align = []
    emb += ['Independence. I am a free spirit -- no one tells me what to do.']
    emb += ['Fairness. I never target people who can\'t afford to lose a few coins.']
    emb += ['Charity. I distribute the money I acquire to the people who really need it.']
    emb += ['Creativity. I never run the same con twice.']
    emb += ['Friendship. Material goods come and go. Bonds of friendship last forever.']
    emb += ['Aspiration. I\'m determined to make something of myself.']
    #
    align += ['(Chaotic)']
    align += ['(Lawful)']
    align += ['(Good)']
    align += ['(Chaotic)']
    align += ['(Good)']
    align += ['(Any)']
    #
    return Personality.Ideals(emb, align)

def Bond():
    emb = []
    emb += ['I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.']
    emb += ['I owe everything to my mentor -- a horrible person who\'s probably rotting in jail somewhere.']
    emb += ['Somewhere out there, I have a child who doesn\'t know me. I\'m making the world better for him and her.']
    emb += ['I come from a noble family, and one day I\'ll reclaim my lands and title from those who stole them from me.']
    emb += ['A powerful person killed someone I love. Some day soon, I\'ll have my revenge.']
    emb += ['I swindled and ruined a person who didn\'t deserve it. I seek to atone for my misdeeds but might never be able to forgive myself.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['I can\'t resist a pretty face.']
    emb += ['I\'m always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in..']
    emb += ['I\'m convinced that no one could ever fool me the way I fool others.']
    emb += ['I\'m too greedy for my own good. I can\'t resist taking a risk if there\'s money involved.']
    emb += ['I can\'t resist swindling people who are more powerful than me.']
    emb += ['I hate to admit it and will hate myself for it, but I\'ll run and preserve my own hide if the going gets tough.']
    return Personality.Flaws(emb)

def Schemes():
	roll = rng.randint(1,6)
	emb = []
	emb += ['I cheat at games of chance.']
	emb += ['I shave coins or forget documents.']
	emb += ['I insinuate myself into people\'s lives to prey on their weakness and secure their fortunes.']
	emb += ['I put on new identities like clothes.']
	emb += ['I run sleight-of-hand cons on street corners.']
	emb += ['I convince people that worthless junk is worth their hard-earned money.']
	return ('Favorite Scheme:' + newLine + TableHelper.dSixTable(emb, roll) + newLine)

def Decision():
	roll = rng.randint(1,6)
	emb = []
	emb += ['I was left to my own devices, and my knack for manipulating others helped me survive.']
	emb += ['I learned early on that people are gullible and easy to exploit.']
	emb += ['I often got in trouble, but I managed to talk my way out of it every time.']
	emb += ['I took up with a confidence artist, from whom I learned my craft.']
	emb += ['after a charlatan fleeced my family, I decided to learn the trade so I would never be fooled by such deception again.']
	emb += ['I was poor or I fear becoming poor, so I learned the tricks I needed to keep myself out of poverty.']
	return ('I became a charlatan because ' + TableHelper.dSixTable(emb, roll) + newLine)