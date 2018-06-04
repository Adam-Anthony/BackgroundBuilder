## Acolyte
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def GetResults():
    result = 'Your background is an acolyte.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    return result

def Trait():
    emb = []
    emb += ['I idolize a particular hero of my faith, and constantly refer to that person\'s deeds and example.']
    emb += ['I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.']
    emb += ['I see omens in every event and action. The gods try to speak to us, we just need to listen.']
    emb += ['Nothing can shake my optimistic attitude.']
    emb += ['I quote (or misquote) sacred texts and proverbsin almost every situation.']
    emb += ['I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.']
    emb += ['I\'ve enjoyed fine food, drink, and high society among my temple\'s elite. Rough living grates on me.']
    emb += ['I\'ve spent so long in the temple that I have little practical experience dealing with people in the outside world.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    align = []
    emb += ['Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld.']
    emb += ['Charity. I always try to help those in need, no matter what the personal cost.']
    emb += ['Change. We must help bring about the changes the gods are constantly working in the world.']
    emb += ['Power. I hope to one day rise to the top of my faith\'s religious hierarchy.']
    emb += ['Faith. I trust that my deity will guide my actions. I have faith that if I work hard, things will go well.']
    emb += ['Aspiration. I seek to prove myself worthy of my god\'s favor by matching my actions against his or her teachings.']
    #
    align += ['(Lawful)']
    align += ['(Good)']
    align += ['(Chaotic)']
    align += ['(Lawful)']
    align += ['(Lawful)']
    align += ['(Any)']
    #
    return Personality.Ideals(emb, align)

def Bond():
    emb = []
    emb += ['I would die to recover an ancient relic of my faith that was lost long ago.']
    emb += ['I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.']
    emb += ['I owe my life to the priest who took me in when my parents died.']
    emb += ['Everything I do is for the common people.']
    emb += ['I will do anything to protect the temple where I served.']
    emb += ['I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['I judge others harshly, and myself even more severely.']
    emb += ['I put too much trust in those who wield power within my temple\'s hierarchy.']
    emb += ['My piety sometimes leads me to blindly trust those that profess faith in my god.']
    emb += ['I am inflexible in my thinking.']
    emb += ['I am suspicious of strangers and expect the worst of them.']
    emb += ['Once I pick a goal, I become obssessed with it to the detriment of everything else in my life.']
    return Personality.Flaws(emb)

def Decision():
    roll = rng.randint(1,6)
    emb = []
    emb += ['I ran away from home at an early age and found refuge in a temple.']
    emb += ['my family gave me to a temple, since they were unable or unwilling to care for me.']
    emb += ['I grew up in a household with strong religious convictions. Entering the service of one or more gods seemed natural.']
    emb += ['an impassioned sermon struck a chord deep in my soul and moved me to serve the faith.']
    emb += ['I followed a childhood friend, a respected acquaintance, or someone I loved into religious service.']
    emb += ['after encountering a true servant of the gods, I was so inspired that I immediately entered the service of a religious group.']
    return ('I became an acolyte because ' + TableHelper.dSixTable(emb, roll) + newLine)