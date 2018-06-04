## Noble
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def GetResults():
    result = 'Your background is a noble.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    return result

def Trait():
    emb = []
    emb += ['My eloquent flattery makes everyone I talk to feel like the most wonderful and important person n the world.']
    emb += ['The common folk love me for my kindness and generosity.']
    emb += ['No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses.']
    emb += ['I take great pains to always look my best and follow the latest fashions.']
    emb += ['I don\'t like to get my hands dirty, and I won\'t be caught dead in unsuitable accomodations.']
    emb += ['Despite my noble birth, I do not place myself above other folk. We all have the same blood.']
    emb += ['My favor, once lost, is lost forever.']
    emb += ['If you do me an injury, I will crush you, ruin your name, and salt your fields.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    ideal = []
    emb += ['Respect. Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity.']
    emb += ['Responsibility. It is my duty to respect the authority of those above me, just as those below me must respect mine.']
    emb += ['Independence. I must prove that I can handle myself without the coddling of my family.']
    emb += ['Power. If I can attain more power, no one will tell me what to do.']
    emb += ['Family. Blood runs thicker than water.']
    emb += ['Noble Obligation. It is my duty to protect and care for the people beneath me.']
    #
    ideal += ['(Good)']
    ideal += ['(Lawful)']
    ideal += ['(Chaotic)']
    ideal += ['(Evil)']
    ideal += ['(Any)']
    ideal += ['(Good)']
    #
    return Personality.Ideals(emb, ideal)

def Bond():
    emb = []
    emb += ['I will face any challenge to win the approval of my family.']
    emb += ['My house\'s alliance with anohter noble family must be sustained at all costs']
    emb += ['Nothing is more important than the other members of my family.']
    emb += ['I am in love with the heir of a family that my family despises.']
    emb += ['My loyalty to my sovereign is unwavering.']
    emb += ['The common folk must see me as a hero of the people.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['I secretly believe that everyone is beneath me.']
    emb += ['I hide a truly scandalous secret that could ruin my family forever.']
    emb += ['I too often hear veiled insults and threats in every word addressed to me, and I\'m quick to anger.']
    emb += ['I have an insatiable desire for carnal pleasures.']
    emb += ['In fact, the world does revolve around me.']
    emb += ['By my words and action, I often bring shame to my family.']
    return Personality.Flaws(emb)

def Decision():
    roll = rng.randint(1,6)
    emb = []
    emb += ['I come from an old and storied family, and it fell to me to preserve the family name.']
    emb += ['my family has been disgraced, and I intend to clear our name.']
    emb += ['my family recently came by its title, and that elevation thrust us into a new and strange world.']
    emb += ['my family has a title, but none of my ancestors have distinguished themselves since we gained it.']
    emb += ['my family is filled with remarkable people. I hope to live up to their example.']
    emb += ['I hope to increase my family\'s power and influence.']
    return ('I became a noble because ' + TableHelper.dSixTable(emb, roll) + newLine)