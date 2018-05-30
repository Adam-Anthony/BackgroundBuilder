## Preamble not finished
import random as rng
import Parts.TableHelper as TableHelper
lineBreak = '\n'
blankSpace = ' '

def WarlockTables(rolls):
    result = 'You are a warlock.' + lineBreak

    trainRoll = rng.randint(1,6)
    result += (ClassTraining(trainRoll) + lineBreak)

    ## PatronAttitudes
    result += (PatronAttitudes(rolls[0]) + lineBreak)

    ## Special Terms
    result += 'The terms of the pact include special terms.' + blankSpace
    result += (SpecialTerms(rolls[1]) + lineBreak)

    ##Binding Mark
    result += (BindingMark(rolls[2]) + lineBreak)

    return result

def PatronAttitudes(roll):
    emb = []
    emb += ['You patron has guided and helped your family for generations and is kindly toward you.']
    emb += ['Each interaction with your capricious patron is a surprise, whether pleasant or painful.']
    emb += ['Your patron is the spirit of a long-dead hero who sees your pact as a way for it to continue to influence the world.']
    emb += ['Your patron is a strict disciplinarian but treats you with a measure of respect.']
    emb += ['Your patron tricked you into a pact and treats you as a slave.']
    emb += ['You are mostly left to your own devices with no interference from your patron. Sometimes you dread the demands it will make when it does appear.']

    return TableHelper.dSixTable(emb, roll)

def SpecialTerms(roll):
    emb = []
    emb += ['When directed, you must take immediate action against a specific enemy of your patron.']
    emb += ['Your pact tests your willpower; you are required to abstain from alcohol and other intoxicants.']
    emb += ['At least once a day, you must inscribe or carve your patron\'s name or symbol on the wall of a building.']
    emb += ['You must occasionally conduct bizarre rituals to maintain your pact.']
    emb += ['You can never wear the same outfit twice, since your patron finds such predictability to be boring.']
    emb += ['When you use an eldritch invocation, you must speak your patron\'s name aloud or risk incurring its displeasure.']
    
    return TableHelper.dSixTable(emb, roll)

def BindingMark(roll):
    emb = []
    emb += ['One of your eyes looks the same as one of your patron\'s eyes.']
    emb += ['Each time you wake up, the small blemish on your face appears in a different place.']
    emb += ['You display outward symptoms of a disease but suffer no ill effects from it.']
    emb += ['Your tongue is an unnatural colour.']
    emb += ['You have a vestigial tail']
    emb += ['Your nose glows in the dark.']

    return TableHelper.dSixTable(emb, roll)

def ClassTraining(roll):
    emb = []
    emb += ['while wandering around in a forbidden place, you encountered an otherworldly being that offered to enter into a pact with you.']
    emb += ['you were examining a strange tome you found in an abandoned library when the entity that would become your patron suddenly appeared before you.']
    emb += ['you stumbled into the clutches of your patron after you accidentally stepped through a magical doorway.']
    emb += ['when you were faced with a terrible crisis, you prayed to any being who would listen, and the creature that answered became your patron.']
    emb += ['your fututre patron visited you in your dreams and offered great power in exchange for your service.']
    emb += ['one of your ancestors had a pact with your patron, so that entity was determined to bind you to the same agreement.']

    result =  'You became a warlock because ' + TableHelper.dSixTable(emb, roll) + lineBreak
    return result