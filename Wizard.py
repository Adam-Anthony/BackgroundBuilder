# Preamble is not finished.
import random as rng
import TableHelper
lineBreak = '\n'
blankSpace = ' '

def WizardTables(rolls):
    result = 'You are a wizard.' + lineBreak

    trainRoll = rng.randint(1,6)
    result += (ClassTraining(trainRoll) + lineBreak)
    
    ## Spellbook
    result += 'Spellbook:' + blankSpace
    result += (Spellbooks(rolls[0]) + lineBreak)

    ## Ambition
    result += 'Ambition:' + blankSpace
    result += (Ambition(rolls[1]) + lineBreak)

    ## Eccentricity
    result += 'Eccentricity:' + blankSpace
    result += (Eccentricity(rolls[2]) + lineBreak)
    
    return result

def Spellbooks(roll):
    emb = []
    emb += ['A tome with pages that are thin sheets of metal, spells etched into them with acid.']
    emb += ['Long straps of leather on which spells are written, wrapped around a staff for ease of transport.']
    emb += ['A battered tome filled with pictographs that only you can understand.']
    emb += ['Small stones inscribed with spells and kept in a cloth bag.']
    emb += ['A scorched book, ravaged by dragon fire, with the script of your spells barely visible on its pages.']
    emb += ['A tome full of black pages whose writing is visible only in dim light or darkness.']
    return TableHelper.dSixTable(emb, roll)

def Ambition(roll):
    emb = []
    emb += ['You will prove that the gods aren\'t as powerful as folk believe.']
    emb += ['Immortality is the end goal of your studies.']
    emb += ['If you can fully understand magic, you can unlock its use for all and usher in an era of equality.']
    emb += ['Magic is a dangerous tool. You use it to protect what you treasure.']
    emb += ['Arcane power must be taken away from those who would abuse it.']
    emb += ['You will become the greatest wizard the world has seen in generations.']
    return TableHelper.dSixTable(emb, roll)

def Eccentricity(roll):
    emb = []
    emb += ['You have the habit of tapping your foot incessantly, which often annoys those around you.']
    emb += ['Your memory is quite good, but you have no trouble pretending to be absentminded when it suits your purposes.']
    emb += ['You never enter a room without looking to see what\'s hanging from the ceiling.']
    emb += ['Your most prized possession is a dead worm that you keep inside a potion vial.']
    emb += ['When you want people to leave you alone, you start talking to yourself. That usually does the trick.']
    emb += ['Your fashion sense and grooming, or more accurately lack thereof, sometimes cause others to assume you are a begger.']
    return TableHelper.dSixTable(emb, roll)

def ClassTraining(roll):
    emb = []
    emb += ['an old wizard chose you from among several candidates to serve an apprenticeship.']
    emb += ['when you became lost in a forest, a hedge wizard found you, took you in, and taught you the rudiments of magic.']
    emb += ['you grew up listening to tales of great wizards and knew you wanted to follow their path. You strove to be accepted at an academy of magic and succeeded.']
    emb += ['one of your relatives was an accomplished wizard who decided you were smart enough to learn the craft.']
    emb += ['while exploring an old tomb, library, or temple, you found a spellbook. You were immediately driven to learn all you could about becoming a wizard.']
    emb += ['you were a prodigy who demonstrated mastery of the arcane arts at an early age. When you became old enough to set out on your own, you did so to learn more magic and expand your power.']

    result =  'You became a wizard because ' + TableHelper.dSixTable(emb, roll) + lineBreak
    return result