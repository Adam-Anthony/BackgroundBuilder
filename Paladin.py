## Preamble not finished
import random as rng
import TableHelper
lineBreak = '\n'
blankSpace = ' '

def PaladinTables(rolls):
    result = 'You are a fighter.' + lineBreak
    #
    trainRoll = rng.randint(1,6)
    result += (ClassTraining(trainRoll) + lineBreak)
    #
    ## HeraldicSigns
    result += ('Personal Goal:' + blankSpace)
    result += (PersonalGoals(rolls[0]) + lineBreak)
    #
    ## Instructor
    result += ('Symbol:' + blankSpace)
    result += (Symbols(rolls[1]) + lineBreak)
    #
    ## SignatureStyles
    result += ('Nemesis:' + blankSpace)
    result += (Nemesis(rolls[2]) + lineBreak)
    #
    ## Temptation
    temptRoll = rng.randint(1,6)
    result += ('Temptation:' + blankSpace)
    result += (Temptations(temptRoll) + lineBreak)
    #
    return result

def PersonalGoals(roll):
    emb = []
    emb += ['Peace. You fight so that future generations will not have to.']
    emb += ['Revenge. Your oath is the vehicle through which you will right an ancient wrong.']
    emb += ['Duty. You will live up to what you have sworn to do, or die trying.']
    emb += ['Leadership. You will win a great battle that bards will sing about, and in so doing, you will become an example to inspire others.']
    emb += ['Faith. You know your path is righteous, or else the gods would not have set you upon it. ']
    emb += ['Glory. You will lead the world into a grand new era, one that will be branded with your name.']
    #
    return TableHelper.dSixTable(emb, roll)

def Symbols(roll):
    emb = []
    emb += ['A dragon, emblematic of your nobility in peace and your ferocity in combat.']
    emb += ['A clenched fist, because you are always ready to fight for your beliefs.']
    emb += ['An upraised open hand, indicating your preference for diplomacy over combat.']
    emb += ['A red heart, showing the world your commitment to justice.']
    emb += ['A black heart, signifying that emotions such as pity do not sway your dedication to your oath.']
    emb += ['An unblinking eye, meaning that you are ever alert to all threats against your cause.']
    #
    return TableHelper.dSixTable(emb, roll)

def Nemesis(roll):
    emb = []
    emb += ['A mighty orc war chief who threatens to overrun and destroy everything you hold sacred.']
    emb += ['A fiend or a celestial, the agent of a power of the Outer Planes, who has been charged with corrupting or redeeming you, as appropriate.']
    emb += ['A dragon whose servants dog your steps.']
    emb += ['A high priest who sees you as a misguided fool and wants you to abandon your religion.']
    emb += ['A rival paladin who trained with you but became an oath-breaker and holds you responsible.']
    emb += ['A vampire who has sworn revenge against all paladins after being defeated by one.']
    #
    return TableHelper.dSixTable(emb, roll)

def Temptations(roll):
    emb = []
    emb += ['Fury. When your anger is roused, you have trouble thinking straight, and you fear you might do something you\'ll regret.']
    emb += ['Pride. Your deeds are noteworthy, and no one takes note of them more often than you.']
    emb += ['Lust. You can\'t resist an attractive face and a pleasant smile.']
    emb += ['Envy. You are mindful of what some famous folk have accomplished, and you feel inadequate when your deeds don\'t compare to theirs.']
    emb += ['Despair. You consider the great strength of the enemies you must defeat, and at times you see no way to achieve final victory.']
    emb += ['Greed. Regardless of how much glory and treasure you amass, it\'s never enough for you.']
    #
    return TableHelper.dSixTable(emb, roll)    

def ClassTraining(roll):
    emb = []
    emb += ['a fantastical being appeared before you and called on you to undertake a holy quest.']
    emb += ['one of your ancestors left a holy quest unfulfilled, so you intend to finish that work.']
    emb += ['the world is a dark and terrible place. You decided to serve as a beacon of light shining out against the gathering shadows.']
    emb += ['you served as a paladin\'s squire, learning all you needed to swear your own sacred oath.']
    emb += ['evil must be opposed on all fronts. You feel compelled to seek out wickedness and purge it from the world.']
    emb += ['becoming a paladin was a natural consequence of your unwavering faith. In taking your vows, you became the holy sword of your religion.']
    result = 'You became a paladin because ' + TableHelper.dSixTable(emb, roll) + lineBreak
    return result