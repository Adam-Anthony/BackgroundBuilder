## Urchin
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def GetResults():
    result = 'Your background is an urchin.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    return result

def Trait():
    emb = []
    emb += ['I hide scraps of food and trinkets away in my pockets.']
    emb += ['I ask a lot of questions.']
    emb += ['I like to squeeze into small places where no one else can get to me.']
    emb += ['I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms.']
    emb += ['I eat like a pig and have bad manners.']
    emb += ['I think anyone who\'s nice to me is hiding evil intent.']
    emb += ['I don\'t like to bathe.']
    emb += ['I bluntly say what other people are hinting at or hiding.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    ideal = []
    #
    emb += ['Respect. All people, rich or poor, deserve respect.']
    emb += ['Community. We have to take care of each other, because no one else is going to do it.']
    emb += ['Change. The low are lifted up, and the high and mighty are brought down. Change is the nature of things.']
    emb += ['Retribution. The rich need to be shown what life and death are like in the gutters.']
    emb += ['People. I help the people who help me--that\'s what keeps us alive.']
    emb += ['Aspiration. I\'m going to prove that I\'m worthy of a better life.']
    #
    ideal += ['(Good)']
    ideal += ['(Lawful)']
    ideal += ['(Chaotic)']
    ideal += ['(Evil)']
    ideal += ['(Neutral)']
    ideal += ['(Any)']
    return Personality.Ideals(emb, ideal)

def Bond():
    emb = []
    emb += ['My town or city is my home, and I\'ll fight to defend it.']
    emb += ['I sponsor an orphanage to keep others from enduring what I was forced to endure.']
    emb += ['I owe my survival to another urchin who taught me to live on the streets.']
    emb += ['I owe a debt I can never repay to the person who took pity on me.']
    emb += ['I escaped my life of poverty by robbing an important person, and I\'m wanted for it.']
    emb += ['No one else should have to endure the hardships I\'ve been through.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['If I\'m outnumbered, I will run away from a fight.']
    emb += ['Gold seems like a lot of money to me, and I\'ll do just about anything for more of it.']
    emb += ['I will never fully trust anyone other than myself.']
    emb += ['I\'d rather kill someone in their sleep then fight fair.']
    emb += ['It\'s not stealing if I need it more than someone else.']
    emb += ['People who can\'t take of themselves get what they deserve.']
    return Personality.Flaws(emb)

def Decision():
    roll = rng.randint(1,6)
    emb = []
    emb += ['wanderlust caused me to leave my family to se the world. I look after myself.']
    emb += ['I ran away from a bad situation at home and made my own way in the world.']
    emb += ['monsters wiped out my village, and I was the sole survivor. I had to find a way to survive.']
    emb += ['a notorious thief looked after me and other orphans, and we spied and stole to earn our keep.']
    emb += ['one day I woke up on the streets, alone and hungry, with no memory of my early childhood.']
    emb += ['my parents died, leaving no one to look after me. I raised myself.']
    return ('I became an urchin because ' + TableHelper.dSixTable(emb, roll) + newLine)