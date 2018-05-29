## Preamble not finished
import random as rng
import TableHelper
lineBreak = '\n'
blankSpace = ' '

def RangerTables(rolls):
    result = 'You are a ranger.' + lineBreak
    #
    trainRoll = rng.randint(1,6)
    result += (ClassTraining(trainRoll) + lineBreak)
    #
    ## ViewsOfTheWorld
    result += ('View of the World:' + blankSpace)
    result += (ViewsOfTheWorld(rolls[0]) + lineBreak)
    #
    ## Homelands
    result += ('Homeland:' + blankSpace)
    result += (Homelands(rolls[1]) + lineBreak)
    #
    ## SwornEnemys
    result += ('Sworn Enemy:' + blankSpace)
    result += (SwornEnemies(rolls[2]) + lineBreak)
    #
    return result

def ViewsOfTheWorld(roll):
    emb = []
    emb += ['Towns and cities are the best places for those who can\'t survive on their own.']
    emb += ['The advancement of civilization is the best way to thwart chaos, but its reach must be monitored.']
    emb += ['Towns and cities are a necessary evil, but once the wilderness is purged of supernatural threats, we will need them no more.']
    emb += ['Walls are for cowards, who huddle behind them while others do the work of making the world safe.']
    emb += ['Visiting a town is not unpleasant, but after a few days I feel the irresistible call to return to the wild.']
    emb += ['Cities breed weakness by isolating folk from the harsh lessons of the wild.']
    #
    return TableHelper.dSixTable(emb, roll)

def Homelands(roll):
    emb = []
    emb += ['You patrolled an ancient forest, darkened and corrupted by several crossings to the Shadowfell.']
    emb += ['As part of a group of nomads, you acquired the skills for surviving in the desert.']
    emb += ['Your early life in the Underdark prepared you for the challenges of combating its denizens.']
    emb += ['You dwelled on the edge of a swamp, in an area imperiled by land creatures as well as aquatic ones.']
    emb += ['Because you grew up among the peaks, finding the best path through the mountains is second nature to you.']
    emb += ['You wandered the far north, learning how to protect yourself and prosper in a realm overrun by ice.']
    #
    return TableHelper.dSixTable(emb, roll)

def SwornEnemies(roll):
    emb = []
    emb += ['You seek revenge on nature\'s behalf for the great transgressions your foe has committed.']
    emb += ['Your forebears or predecessors fought these creatures, and so shall you.']
    emb += ['You bear no enmity toward your foe. You stalk such creatures as a hunter tracks down a wild animal.']
    emb += ['You find your foe fascinating, and you collect books of tales and history concerning it.']
    emb += ['You collect tokens of your fallen enemies to remind you of each kill.']
    emb += ['You respect your chosen enemy, and you see your battles as a test of respective skills.']
    #
    return TableHelper.dSixTable(emb, roll)

def ClassTraining(roll):
    emb = []
    emb += ['you found purpose while you honed your hunting skills by bringing down dangerous animals at the edge of civilization.']
    emb += ['you always had a way with animals, able to calm them with a soothing word and a touch.']
    emb += ['you suffer from terrible wanderlust, so being a ranger gave you a reason not to remain in one place for too long.']
    emb += ['you have seen what happens when the monsters come out from the dark. You took it upon yourself to become the first line of defense against the evils that lie beyond civilization\'s borders.']
    emb += ['you met a grizzled ranger who taught you woodcraft and the secrets of the wild lands.']
    emb += ['you served in an army, learning the precepts of your profession while blazing trails and scouting enemy encampments.']
    result = 'You became a ranger because ' + TableHelper.dSixTable(emb, roll) + lineBreak
    return result