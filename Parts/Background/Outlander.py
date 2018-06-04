## Outlander
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '
indentSpace = '    '

def GetResults():
    result = 'Your background is an outlander.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    result += Origin()
    return result

def Trait():
    emb = []
    emb += ['I\'m driven by a wanderlust that led me away from home.']
    emb += ['I watch over my friends as if they were a litter of newborn pups.']
    emb += ['I once ran twenty-five miles without stopping to warn to my clan of an approaching orc horde. I\'d do it again if I had to.']
    emb += ['I have a lesson for every situation, drawn from observing nature.']
    emb += ['I place no stock in wealthy or well-mannered folk. Money and manners won\'t save you from a hungry owlbear.']
    emb += ['I\'m always picking things up, absently fiddling with them, and sometimes accidentally breaking them.']
    emb += ['I feel far more comfortable around animals than people.']
    emb += ['I was, in fact, raised by wolves.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    ideal = []
    emb += ['Change. Life is like the seasons, in constant change, and we must change with it.']
    emb += ['Greater Good. It is each person\'s responsibility to make the most happiness for the whole tribe.']
    emb += ['Honor. It is each person\'s responsibility to make the most happiness for the whole tribe.']
    emb += ['Might. The strongest are meant to rule. (Evil)']
    emb += ['Nature. The natural world is more important than all the constructs of civilization.']
    emb += ['Glory. I must earn glory in battle, for myself and my clan.']
    #
    ideal += ['(Chaotic)']
    ideal += ['(Good)']
    ideal += ['(Lawful)']
    ideal += ['(Evil)']
    ideal += ['(Neutral)']
    ideal += ['(Any)']
    #
    return Personality.Ideals(emb, ideal)

def Bond():
    emb = []
    emb += ['My family, clan, or tribe is the most important in my life, even when they are far from me.']
    emb += ['An injury to the unspoiled wilderness of my home is an injury to me.']
    emb += ['I will bring terrible wrath down on the evildoers who destroyed my homeland.']
    emb += ['I am the last of my tribe, and it is up to me to ensure their names enter legend.']
    emb += ['I suffer awful visions of a coming disaster and will do anything to prevent it.']
    emb += ['It is my duty to provide children to sustain my tribe.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['I am too enamored of ale, wine, and other intoxicants.']
    emb += ['There\'s no room for caution in a life lived to the fullest.']
    emb += ['I remember every insult I\'ve received and nurse a silent resentment toward anyone who\'s ever wronged me.']
    emb += ['I am slow to trust members of other races, tribes, and societies.']
    emb += ['Violence is my answer to almost any challenge.']
    emb += ['Don\'t expect me to save those who can\'t save themselves. It is nature\'s way that the strong thrive and the weak perish.']
    return Personality.Flaws(emb)

def Origin():
    roll = rng.randint(1,10)
    emb = []
    emb += ['Forester']
    emb += ['Trapper']
    emb += ['Homesteader']
    emb += ['Guide']
    emb += ['Exile or outcast']
    emb += ['Bounty hunter']
    emb += ['Pilgrim']
    emb += ['Tribal Nomad']
    emb += ['Hunter-gatherer']
    emb += ['Tribal marauder']
    return ('Origin:' + newLine + indentSpace + TableHelper.dTenTable(emb,roll) + newLine)

def Decision():
    roll = rng.randint(1,6)
    emb = []
    emb += ['I spent a lot of time in the wilderness as a youngster, and I came to love that way of life.']
    emb += ['from a young age, I couldn\'t abidethe stink of the cities and preferred to spend my time in nature.']
    emb += ['I came to understand the darkness that lurks in the wilds, and I vowed to combat it.']
    emb += ['my people lived on the edges of civilization, and I learned the methods of survival from my family.']
    emb += ['after a tragedy I retreated to the wilderness, leaving my old life behind.']
    emb += ['my family moved away from civilization, and I learned to adapt to my new environment.']
    return ('I became an outlander because ' + TableHelper.dSixTable(emb, roll) + newLine)