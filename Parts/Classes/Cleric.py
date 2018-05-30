## Preamble is finished
import random as rng
import Parts.TableHelper as TableHelper
lineBreak = '\n'
blankSpace = ' '
def ClericTables(rolls):
    result = 'You are a cleric.' + lineBreak

    trainRoll = rng.randint(1,6)
    result += (ClassTraining(trainRoll) + lineBreak)

    result += (Temple(rolls[0]) + lineBreak)

    result += 'You have a keepsake, meant to symbolize their faith.' + blankSpace
    result += (Keepsake(rolls[1]) + lineBreak)

    result += 'Every cleric must grapple with a dark secret, you are no different.' + blankSpace
    result += (Secret(rolls[2]) + lineBreak)
    
    return result

def Temple(roll):
    emb = []
    emb += ['Your temple is said to be the oldest surviving structure built to honor your god.']
    emb += ['Acolytes of several like-minded deities all received instruction together in your temple.']
    emb += ['You come from a temple famed for the brewery it operates. Some say you smell like one of its ales.']
    emb += ['Your temple is a fortress and a proving ground that trains warrior-priests.']
    emb += ['Your temple is a peaceful, humble place, filled with vegetable gardens and simple priests.']
    emb += ['You served in a temple in the Outer Planes.']
    return TableHelper.dSixTable(emb, roll)

def Keepsake(roll):
    emb = []
    emb += ['The finger bone of a saint.']
    emb += ['A metal-bound book that tells how to hunt and destroy infernal creatures.']
    emb += ['A pig\'s whistle that reminds you of your humble and beloved mentor.']
    emb += ['A braid of hair woven from the tail of a unicorn.']
    emb += ['A scroll that describes how best to rid the world of necromancers.']
    emb += ['A runestone said to be blessed by your god.']
    return TableHelper.dSixTable(emb, roll)

def Secret(roll):
    emb = []
    emb += ['An imp offers you counsel. You try to ignore the creature, but sometimes its advice is helpful.']
    emb += ['You believe that, in the final analysis, the gods are nothing more than ultrapoweful mortal creatures.']
    emb += ['You acknowledge the power of the gods, but you think that most events are dictated by pure chance.']
    emb += ['Even though you can work divine magic, you have never truly felt the presence of a divine essence within yourself.']
    emb += ['You are plagued by nightmares that you believe are sent by your god as punishment for some unknown transgression.']
    emb += ['In times of despair, you feel that you are but a plaything of the gods, and you resent their remoteness.']
    return TableHelper.dSixTable(emb, roll)

def ClassTraining(roll):
    emb = []
    emb += ['a suppernatural being in service to the gods called you to become a divine agent in the world.']
    emb += ['you saw the injustice and horror in the world and felt moved to take a stand against them.']
    emb += ['your god gave you an unmistakable sign. You dropped everything to serve the divine.']
    emb += ['although you were always devout, it wasn\'t until you completed a pilgrimage that you knew your true calling.']
    emb += ['you used to serve in your religion\'s bureaucracy but found you needed to work in the world, to bring the message of your faith to the darkest corners of the land.']
    emb += ['you realize that your god works through you, and you do as commanded, even though you don\'t know why you were chosen to serve.']
    result =  'You became a cleric because ' + TableHelper.dSixTable(emb, roll) + lineBreak
    return result