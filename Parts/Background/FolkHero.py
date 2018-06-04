## Folk Hero
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def GetResults():
    result = 'Your background is a folk hero.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    result += DefiningEvent()
    return result

def Trait():
    emb = []
    emb += ['I judge people by their actions, not their words.']
    emb += ['If someone is in trouble, I\'m always ready to lend help.']
    emb += ['When I set my mind to something, I follow through no matter what gets in my way.']
    emb += ['I have a strong sense of fair play and always try to find the most equitable solution to arguments.']
    emb += ['I\'m confident in my own abilities and do what I can to install confidence in others.']
    emb += ['Thinking is for other people. I prefer action.']
    emb += ['I misuse long words in an attempt to sound smarter.']
    emb += ['I get bored easily. When am I going to get on with my destiny?']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    align = []
    emb += ['Respect. People deserve to be treated with dignity and respect.']
    emb += ['Fairness. No one should get preferential treatment before the law, and no one is above the law.']
    emb += ['Freedom. Tyrants must not be allowed to oppres the people.']
    emb += ['Might. If I become strong, I can take what I want--what I deserve.']
    emb += ['Sincerity. There\'s no good in pretending to be something I\'m not.']
    emb += ['Destiny. Nothing and no one can steer me away from my higher calling.']
    #
    align += ['(Good)']
    align += ['(Lawful)']
    align += ['(Chaotic)']
    align += ['(Evil)']
    align += ['(Neutral)']
    align += ['(Any)']
    #
    return Personality.Ideals(emb, align)

def Bond():
    emb = []
    emb += ['I have a family, but I have no idea where they are. One day, I hope to see them again.']
    emb += ['I worked the land, I love the land, and I will protect the land.']
    emb += ['A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.']
    emb += ['My tools are symbols of my past life, and I carry them so that I will never forget my roots.']
    emb += ['I protect those who cannot protect themselves.']
    emb += ['I wish my childhood sweetheart had come with me to pursue my destiny.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['The tyrant who rules my land will stop at nothing to see me killed.']
    emb += ['I\'m convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.']
    emb += ['The people who knew me when I was young know my shameful secret, so I can never go home again.']
    emb += ['I have a weakness for the vices of the city, especially hard drink.']
    emb += ['Secretly, I believe that things would be better if I were a tyrant lording over the land.']
    emb += ['I have trouble trusting in my allies.']
    return Personality.Flaws(emb)

def DefiningEvent():
    roll = rng.randint(1,10)
    emb = []
    emb += ['I stood up to a tyrant\'s agents.']
    emb += ['I saved people during a natural disaster.']
    emb += ['I stood alone against a terrible monster.']
    emb += ['I stole from a corrupt merchant to help the poor.']
    emb += ['I led a militia to fight off an invading army.']
    emb += ['I broke into a tyrant\'s castle and stole weapons to arm the people.']
    emb += ['I trained the peasantry to use farm implements as weapons against a tyrant\'s soldiers.']
    emb += ['A lord rescinded an unpopular decree after I led a symbolic act of protect against it.']
    emb += ['A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.']
    emb += ['Recruited into a lord\'s army, I rose to leadership and was commended for my heroism.']
    return ('Defining Event:' + newLine + TableHelper.dTenTable(emb, roll) + newLine)

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