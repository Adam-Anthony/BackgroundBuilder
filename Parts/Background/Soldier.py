## Soldier
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '
indentSpace = '    '

def GetResults():
    result = 'Your background is a soldier.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    result += Specialty()
    return result

def Trait():
    emb = []
    emb += ['I\'m always polite and respectful.']
    emb += ['I\'m haunted by memories of war. I can\'t get the images of violence out of my mind.']
    emb += ['I\'ve lost too many friends, and I\'m slow to make new ones.']
    emb += ['I\'m full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.']
    emb += ['I can stare down a hell hound without flinching.']
    emb += ['I enjoy being strong and like breaking things.']
    emb += ['I have a crude sense of humor.']
    emb += ['I face problems head-on. A simple, direct solution is the best path to success.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    align = []
    emb += ['Greater Good. Our lot is to lay down our lives in defense of others.']
    emb += ['Responsibility. I do what I must and obey just authority.']
    emb += ['Independence. When people follow orders blindly, they embrace a kind of tyranny.']
    emb += ['Might. In life as in war, the stronger force wins.']
    emb += ['Live and Let Live. Ideals are\'t worth killing over or going to war for.']
    emb += ['Nation. My city, nation, or people are all that matter.']
    #
    align += ['(Good)']
    align += ['(Lawful)']
    align += ['(Chaotic)']
    align += ['(Evil)']
    align += ['(Neutral)']
    align += ['(Any)']
    return Personality.Ideals(emb, align)

def Bond():
    emb = []
    emb += ['I would still lay down my life for the people I served with.']
    emb += ['Someone saved my life on the battlefield. To this day, I will never leave a friend behind.']
    emb += ['My honor is my life.']
    emb += ['I\'ll never forget the crushing defeat my company suffered or the enemies who dealt it.']
    emb += ['Those who fight beside me are those worth dying for.']
    emb += ['I fight for those who cannot fight for themselves.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['The monstrous enemy we faced in battle still leaves me quivering with fear.']
    emb += ['I have little respect for anyone who is not a proven warrior.']
    emb += ['I made a terrible mistake in battle cost many lives--and I would do anything to keep that mistake secret.']
    emb += ['My hatred of my enemies is blind and unreasoning.']
    emb += ['I obey the law, even if the law causes misery.']
    emb += ['I\'d rather eat my armor than admit when I\'m wrong.']
    return Personality.Flaws(emb)

def Specialty():
    roll = rng.randint(1,8)
    emb = []
    emb += ['Officer']
    emb += ['Scout']
    emb += ['Infantry']
    emb += ['Cavalry']
    emb += ['Healer']
    emb += ['Quartermaster']
    emb += ['Standard bearer']
    emb += ['Support staff (cook, blacksmith, or the like)']
    return ('Specialty:' + newLine + indentSpace + TableHelper.dEightTable(emb, roll) + newLine)
    
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