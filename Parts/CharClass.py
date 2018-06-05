import random as rng 
import Parts.Classes.Barbarian as Barbarian
import Parts.Classes.Bard as Bard
import Parts.Classes.Cleric as Cleric

import Parts.Classes.Druid as Druid
import Parts.Classes.Fighter as Fighter
import Parts.Classes.Monk as Monk

import Parts.Classes.Paladin as Paladin
import Parts.Classes.Ranger as Ranger
import Parts.Classes.Rogue as Rogue

import Parts.Classes.Sorcerer as Sorcerer
import Parts.Classes.Warlock as Warlock
import Parts.Classes.Wizard as Wizard

import Parts.TableHelper as TableHelper
lineBreak = '\n'
blankSpace = ' '

def RollClassNotWeighted():
    roll = rng.randint(1,12)
    characterClass = ''
    if roll == 1:
        characterClass = 'Barbarian'
    elif roll == 2:
        characterClass = 'Bard'
    elif roll == 3:
            characterClass = 'Cleric'
    elif roll == 4:
        characterClass == 'Druid'
    elif roll == 5:
        characterClass == 'Fighter'
    elif roll == 6:
        characterClass == 'Monk'
    elif roll == 7:
        characterClass == 'Paladin'
    elif roll == 8:
        characterClass == 'Ranger'
    elif roll == 9:
        characterClass == 'Rogue'
    elif roll == 10:
        characterClass == 'Sorcerer'
    elif roll == 11:
        characterClass == 'Warlock'
    elif roll == 12:
        characterClass == 'Wizard'
    
    CheckClass(characterClass)

def CheckClass(cc):
    rolls = [rng.randint(1,6), rng.randint(1,6), rng.randint(1,6)]
    result = ''
    if cc == 'Barbarian':
        result = Barbarian.BarbarianTables(rolls)
    elif cc == 'Bard':
        result = Bard.BardTables(rolls)
    elif cc == 'Cleric':
        result = Cleric.ClericTables(rolls)
    elif cc == 'Druid':
        result = Druid.DruidTables(rolls)
    elif cc == 'Fighter':
        result = Fighter.FighterTables(rolls)
    elif cc == 'Monk':
        result = Monk.MonkTables(rolls)
    elif cc == 'Paladin':
        result = Paladin.PaladinTables(rolls)
    elif cc == 'Ranger':
        result = Ranger.RangerTables(rolls)
    elif cc == 'Rogue':
        result = Rogue.RogueTables(rolls)
    elif cc == 'Sorcerer':
        result = Sorcerer.SorcererTables(rolls)
    elif cc == 'Warlock':
        result = Warlock.WarlockTables(rolls)
    elif cc == 'Wizard':
        result = Wizard.WizardTables(rolls)
    #
    return result
################################################################################