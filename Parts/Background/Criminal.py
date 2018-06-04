## Criminal ##
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '
indentSpace = '    '

def GetResults():
    result = 'Your background is a criminal.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    result += Specialty()
    return result

def Trait():
    emb = []
    emb += ['I always have a plan for what to do when things go wrong.']
    emb += ['I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.']
    emb += ['The first thing I do in a new place is note the locations of everything valuable--or where such things could be hidden.']
    emb += ['I would rather make a new friend than a new enemy.']
    emb += ['I am incredibly slow to trust. Those who seem the fairest often have the most to hide.']
    emb += ['I don\'t pay attention to the risks in a situation. Never tell me the odds.']
    emb += ['The best way to get me to do something is to tell me I can\'t do it.']
    emb += ['I blow up at the slightest insult.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    align = []
    emb += ['Honor. I don\'t steal from others in the trade.']
    emb += ['Freedom. Chains are meant to be broken, as are those who would forge them.']
    emb += ['Charity. I steal from the wealthy so that I can help people in need.']
    emb += ['Greed. I will do whatever it takes to become wealthy.']
    emb += ['People. I\'m loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care.']
    emb += ['Redemption. There\'s a spark of good in everyone.']
    #
    align += ['(Lawful)']
    align += ['(Chaotic)']
    align += ['(Good)']
    align += ['(Evil)']
    align += ['(Neutral)']
    align += ['(Good)']

    return Personality.Ideals(emb, align)

def Bond():
    emb = []
    emb += ['I\'m trying to pay off an old debt I owe to a generous benefactor.']
    emb += ['My ill-gotten gains go to support my family.']
    emb += ['Something important was taken from me, and I aim to steal it back.']
    emb += ['I will become the greatest thief that ever lived.']
    emb += ['I\'m guilty of a terrible crime. I hope I can redeem myself for it.']
    emb += ['Someone I loved died because of a mistake I made. That will never happen again.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['When I see something valuable, I can\'t think about anything but how to steal it.']
    emb += ['When faced with a choice between money and my friends, I usually choose the money.']
    emb += ['If there\'s a plan, I\'ll forget it. If I don\'t forget it, I\'ll ignore it.']
    emb += ['I have a \"tell\" that reveals when I\'m lying.']
    emb += ['I turn tail and run when things look bad.']
    emb += ['An innocent person is in prison for a crime that I committed. I\'m okay with that.']
    return Personality.Flaws(emb)

def Specialty():
    emb = []
    roll = rng.randint(1,8)
    emb += ['Blackmailer']
    emb += ['Burglar']
    emb += ['Enforcer']
    emb += ['Fence']
    emb += ['Highway robber']
    emb += ['Hired killer']
    emb += ['Pickpocket']
    emb += ['Smuggler']
    return ('Criminal Specialty:' + newLine + indentSpace +TableHelper.dEightTable(emb, roll) + newLine)

def Decision():
    roll = rng.randint(1,6)
    emb = []
    emb += ['I resented authority in my younger days and saw a life of crime as the best way to fight against tyranny and oppression.']
    emb += ['necessity forced me to take up the life, since it was the only way I could survive.']
    emb += ['I fell in with a gang of reprobates and ne\'er-do-wells, and I learned my specialty from them.']
    emb += ['a parent or relative taught me my criminal specialty to prepare me for the family business.']
    emb += ['I left home and found a place in a thieves\' guild or some other criminal organization.']
    emb += ['I was always bored, so I turned to crime to pass the time and discovered I was quite good at it.']
    return ('I became a criminal because ' + TableHelper.dSixTable(emb, roll) + newLine)