## Preamble not finished
import random as rng
import Parts.TableHelper as TableHelper
lineBreak = '\n'
blankSpace = ' '

def FighterTables(rolls):
    result = 'You are a fighter.' + lineBreak
    
    trainRoll = rng.randint(1,6)
    result += (ClassTraining(trainRoll) + lineBreak)
    
    ## HeraldicSigns
    result += ('Heraldic Sign:' + blankSpace)
    result += (HeraldicSigns(rolls[0]) + lineBreak)
    
    ## Instructor
    result += ('Instructor:' + blankSpace)
    result += (Instructor(rolls[1]) + lineBreak)
    
    ## SignatureStyles
    result += ('Signature Styles:' + blankSpace)
    result += (SignatureStyles(rolls[2]) + lineBreak)
    
    return result

def HeraldicSigns(roll):
    emb = []
    emb += ['A rampant golden dragon on a green field, representing valor and a quest for wealth.']
    emb += ['The fist of a storm giant clutching lightning before a storm cloud, symbolizing wrath and power.']
    emb += ['Crossed greatswords in front of a castle gate, signifying the defense of a city or kingdom.']
    emb += ['A skull with a dagger through it, representing the doom you bring to your enemies.']
    emb += ['A phoenix in a ring of fire, an expression of an indomitable spirit.']
    emb += ['Three drops of blood beneath a horizontal sword blade on a black background, symbolizing three foes you have sworn to kill.']
    
    return TableHelper.dSixTable(emb, roll)

def Instructor(roll):
    emb = []
    emb += ['Gladiator. Your instructor was a slave who fought for freedom in the arena, or one who willingly chose the gladiator\'s life to earn money and fame.']
    emb += ['Military. Your trainer served with a group of soldiers and knows much about working as a team.']
    emb += ['City Watch. Crowd control and peacekeeping are your instructor\'s specialties.']
    emb += ['Tribal Warrior. Your instructor grew up in a tribe, where fighting for one\'s life was practically an everyday occurrence.']
    emb += ['Street Fighter. Your trainer excels at urban combat, combining close-quarters work with silence and efficiency.']
    emb += ['Weapon Master. Your mentor helped you to become one with your chosen weapon, by imparting highly specialized knowledge of how to wield it most effectively.']
    
    return TableHelper.dSixTable(emb, roll)

def SignatureStyles(roll):
    emb = []
    emb += ['Elegant. You move with precise grace and total control, never using more energy than you need.']
    emb += ['Brutal. Your attacks rain down like hammer blows, meant to splinter bone or send blood flying.']
    emb += ['Cunning. You dart in to attack at just the right moment and use small-scale tactics to tilt the odds in your favour.']
    emb += ['Effortless. You rarely perspire or display anything other than a stoic expression in battle.']
    emb += ['Energetic. You sing and laugh during combat as your spirit soars. You are happiest when you have a foe in front of you and a weapon in hand.']
    emb += ['Sinister. You scowl and sneer while fighting, and you enjoy mocking your foes as you defeat them.']
    
    return TableHelper.dSixTable(emb, roll)

def ClassTraining(roll):
    emb = []
    emb += ['you wanted to hone your combat skills, and so you joined a war college.']
    emb += ['your squired for a knight who taught you how to fight, care for a steed, and conduct yourself with honor. You decided to take up that path for yourself.']
    emb += ['horrible monsters descended on your community, killing someone you loved. You took up arms to destroy those creatures and others of a similar nature.']
    emb += ['you joined the army and learned how to fight as part of a group.']
    emb += ['you grew up fighting, and you refined your talents by defending yourself against people who crossed you.']
    emb += ['you could always pick up just about any weapon and know how to use it effectively.']
    result = 'You became a fighter because ' + TableHelper.dSixTable(emb, roll) + lineBreak
    return result