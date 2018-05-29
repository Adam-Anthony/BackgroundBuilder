## Preamble not finished
import random as rng
import TableHelper
lineBreak = '\n'
blankSpace = ' '

def DruidTables(rolls):
    result = 'You are a druid.' + lineBreak
    
    trainRoll = rng.randint(1,6)
    result += (ClassTraining(trainRoll) + lineBreak)
    
    result += ('Treasured Item:' + blankSpace)
    result += (TreasuredItems(rolls[0]) + lineBreak)
    
    result += ('Guiding Aspect:' + blankSpace)
    result += (GuidingAspects(rolls[1]) + lineBreak)
    
    result += ('Mentor:' + blankSpace)
    result += (Mentor(rolls[2]) + lineBreak)
    
    return result

def TreasuredItems(roll):
    emb = []
    emb += ['A twig from the meeting tree that stands in the center of your village.']
    emb += ['A vial of water from the source of a sacred river.']
    emb += ['Special herbs tied together in a bundle.']
    emb += ['A small bronze bowl engraved with animal images.']
    emb += ['A rattle made from a dried gourd and holly berries.']
    emb += ['A miniature golden sickle handed down to you by your mentor.']
    
    return TableHelper.dSixTable(emb, roll)

def GuidingAspects(roll):
    emb = []
    emb += ['Yew trees remind you of renewing your mind and spirit, letting the old die and the new spring forth.']
    emb += ['Oak trees represent strength and vitality. Meditating under an oak fills your body and mind with resolve and fortitude.']
    emb += ['The river\'s endless flow reminds you of the great span of the world. You seek to act with the longterm interests of nature in mind.']
    emb += ['The sea is a constant, churning cauldron of power and chaos. It reminds you that accepting change is necessary to sustain yourself in the world.']
    emb += ['The birds in the sky are evidence that even the smallest creature can survive if they remain above the fray.']
    emb += ['As demonstrated by the actions of the wolf, an individual\'s strength is nothing compared to the power of the pack.']
    
    return TableHelper.dSixTable(emb, roll)

def Mentor(roll):
    emb = []
    emb += ['Your mentor was a wise treant who taught you to think in terms of years and decades rather than days or months.']
    emb += ['You were tutored by a dryad who watched over a slumbering portal to the Abyss. During your training, you were tasked with watching for hidden threats to the world.']
    emb += ['Your tutor always interacted with you in the form of a falcon. You never saw the tutor\'s humanoid form.']
    emb += ['You were one of several youngsters who were mentored by an old druid, until one of your fellow pupils betrayed your group and killed your master.']
    emb += ['Your mentor has appeared to you only in visions. You have yet to meet this person, and you are not sure such a person exists in mortal form.']
    emb += ['Your mentor was a werebear who taught you to treat all living things with equal regard.']
    
    return TableHelper.dSixTable(emb, roll)

def ClassTraining(roll):
    emb = []
    emb += ['you saw too much devastation in the wild places, too much of nature\'s splendor ruined by the despoilers. You joined a circle of druids to fight back against the enemies of nature.']
    emb += ['you found a place among a group of druids after you fled a catastrophe.']
    emb += ['you have always had an affinity for animals, so you explored your talent to see how you could best use it.']
    emb += ['you befriended a druid and was moved by druidic teachings. You decided to follow your friend\'s guidance and give something back to the world.']
    emb += ['while you were growing up, you saw spirits all around you-- entities no one else could perceive. You sought out the druids to help you understand the visions and communicate with these beings.']
    emb += ['you have always felt disgust for creatures of unnatural origin. For this reason, you immersed yourself in the study of the druidic mysteries and became a champion of the natural order.']
    result = 'You became a druid because ' + TableHelper.dSixTable(emb, roll) + lineBreak
    return result