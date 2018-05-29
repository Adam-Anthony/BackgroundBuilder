import random as rng 
import Barbarian
import Bard
import Cleric

import Druid
import Fighter
import Monk

import Paladin
import Ranger
import Rogue

import Sorcerer
import Warlock
import Wizard

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
        print(result)
    elif cc == 'Bard':
        result = Bard.BardTables(rolls)
        print(result)
    elif cc == 'Cleric':
        result = Cleric.ClericTables(rolls)
        print(result)
    elif cc == 'Druid':
        result = Druid.DruidTables(rolls)
        print(result)
    elif cc == 'Fighter':
        result = Fighter.FighterTables(rolls)
        print(result)
    elif cc == 'Monk':
        result = Monk.MonkTables(rolls)
        print(result)
    elif cc == 'Paladin':
        result = Paladin.PaladinTables(rolls)
        print(result)
    elif cc == 'Ranger':
        result = Ranger.RangerTables(rolls)
        print(result)
    elif cc == 'Rogue':
        result = Rogue.RogueTables(rolls)
        print(result)
    elif cc == 'Sorcerer':
        result = Sorcerer.SorcererTables(rolls)
        print(result)
    elif cc == 'Warlock':
        result = Warlock.WarlockTables(rolls)
        print(result)
    elif cc == 'Wizard':
        result = Wizard.WizardTables(rolls)
        print(result)