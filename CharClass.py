import random as rng 
import Barbarian

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
        ##Bard()
        print(result)
    elif cc == 'Cleric':
        ##Cleric()
        print(result)
    elif cc == 'Druid':
        ##Druid()
        print(result)
    elif cc == 'Fighter':
        ##Fighter()
        print(result)
    elif cc == 'Monk':
        ##Monk()
        print(result)
    elif cc == 'Paladin':
        ##Paladin()
        print(result)
    elif cc == 'Ranger':
        ##Ranger()
        print(result)
    elif cc == 'Sorcerer':
        ##Sorcerer()
        print(result)
    elif cc == 'Warlock':
        ##Warlock()
        print(result)
    elif cc == 'Wizard':
        ##Wizard()
        print(result)