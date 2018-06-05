import random as rng
class Parents():
    race = 'aaaa'
    def __init__(self, race):
        super(Parents, self).__init__()
        self.race = race

    def KnownParents(self):
        response = ''
        known = False
        roll = rng.randint(1,20)
        if roll < 20:
            response = 'You know who your parents are or were.'
            known = True
        elif roll == 20:
            response = 'You do not know who your parents were.'
        if known:
            response += self.Nonhuman()
        return response

    def HalfElf(self):
        roll = rng.randint(1,8)
        response = ''
        if roll <= 5:
            response = 'One parent was an elf and the other was a human.'
        elif roll == 6:
            response = 'One parent was an elf and the other was a half-elf.'
        elif roll == 7:
            response = 'One parent was a human and the other was a half-elf.'
        elif roll == 8:
            response = 'Both parents were half-elves.'
        return response

    def HalfOrc(self):
        roll = rng.randint(1,8)
        response = ''
        if roll <= 3:
            response = 'One parent was an orc and the other was a human.'
        elif roll == 4 or roll == 5:
            response = 'One parent was an orc and the other was a half-orc.'
        elif roll == 6 or roll == 7:
            response = 'One parent was a human and the other was a half-orc.'
        elif roll == 8:
            response = 'Both parents were half-orcs.'
        return response

    def Tiefling(self):
        roll = rng.randint(1,8)
        response = ''
        if roll <= 4:
            response = 'Both parents were humans, their infernal heritage dormant until you came along.'
        elif roll == 5 or roll == 6:
            response = 'One parent was a tiefling and the other was a human.'
        elif roll == 7:
            response = 'One parent was a tiefling and the other was a devil.'
        elif roll == 8:
            response = 'One parent was a human and the other was a devil.'
        return response

    def Nonhuman(self):
        result = ''
        if self.race=='half-elf':
            result = self.HalfElf()
        if self.race=='half-orc':
            result = self.HalfOrc()
        if self.race=='tiefling':
            result = self.Tiefling()
        return result

def Birthplace():
    roll = rng.randint(1,100)
    response = 'Your birthplace was '
    if roll <= 50:
        response += 'at home.'
    elif roll >= 51 and roll <= 55:
        response += 'the home of a family friend.'
    elif roll >= 56 and roll <= 63:
        response += 'the home of a healer or midwife.'
    elif roll >= 64 and roll <= 65:
        response += 'a carriage, cart, or wagon.'
    elif roll >= 66 and roll <= 68:
        response += 'a barn, shed, or other outbuilding.'
    elif roll >= 69 and roll <= 70:
        response += 'a cave.'
    elif roll >= 71 and roll <= 72:
        response += 'a field.'
    elif roll >= 73 and roll <= 74:
        response += 'forest.'
    elif roll >= 75 and roll <= 77:
        response += 'a temple.'
    elif roll == 78:
        response += 'a battlefield.'
    elif roll == 79 or roll == 80:
        response += 'an alley or street.'
    elif roll == 81 or roll == 82:
        response += 'a brothel, tavern, or inn.'
    elif roll == 83 or roll == 84:
        response += 'a castle, keep, tower, or palace.'
    elif roll == 85:
        response += 'in a sewer or rubbish heap.'
    elif roll >= 86 and roll <= 88:
        response += 'among people of a different race.'
    elif roll >= 89 and roll <= 91:
        response += 'on board a boat or a ship.'
    elif roll >= 92 and roll <= 93:
        response += 'in a prison or in the headquarters of a secret organization.'
    elif roll >= 94 and roll <= 95:
        response += 'in a sage\'s laboratory.'
    elif roll == 96:
        response += 'in the Feywild.'
    elif roll == 97:
        response += 'in the Shadowfell.'
    elif roll == 98:
        response += 'on the Astral Plane or the Ethereal Plane.'
    elif roll == 99:
        response += 'on an Inner Plane of your choice.'
    elif roll == 100:
        response += 'on an Outer Plane of your choice.'
    return response

def NumberOfSiblings():
    roll = rng.randint(1,10)
    ## Racial -2 for Dwarf or Elf
    ## For each one, need occupation, aligment, status, relationship

def Siblings():
    roll = rng.randint(1,6) + rng.randint(1,6)

class FamilyLife():
    """docstring for Family"""
    def __init__(self):
        super(FamilyLife, self).__init__()
    def Family(self):
        roll = rng.randint(1,100)
    def AbsentParent(self):
        roll = rng.randint(1,4)
    def FamilyLifestyle(self):
        roll = rng.randint(1,6) + rng.randint(1,6) + rng.randint(1,6)
    def ChildhoodHome(self, modif):
        roll = rng.randint(1,100) + modif
    def ChildhoodMemories(self):
        roll = rng.randint(1,6) + rng.randint(1,6) + rng.randint(1,6)
        ## Have to then add a Cha modifier.