import random as rng
import TableHelper
lineBreak = '\n'
blankSpace = ' '
def BarbarianTables(rolls):
    ## Probably want to add more details to these class details
    result = 'You are a barbarian.' + lineBreak

    trainRoll = rng.randint(1,6)
    result += (ClassTraining(trainRoll) + lineBreak)

    result += 'You have a personal totem, a small item that holds special significance.' + blankSpace
    result += (PersonalTotems(rolls[0]) + lineBreak)

    ## Probably want this to flow better
    result += 'You have a tattoo.' + blankSpace
    result += (Tattoos(rolls[1]) + lineBreak)

    result += 'You have a superstitious belief. If it comes from personal experience or the family/clan that raised you is for your to decide.' + blankSpace
    result += (Superstitions(rolls[2]) + lineBreak)

    return result

def PersonalTotems(roll):
    if roll == 1:
        response = 'A tuft of fur from a solitary wolf that you befriended during a hunt.'
    elif roll == 2:
        response = 'Three eagle feathers given to you by a wise shaman, who told you they would play a role in determining your fate.'
    elif roll == 3:
        response = 'A necklace made from the claws of a young cave bear that you slew singlehandedly as a child.'
    elif roll == 4:
        response = 'A small leather pouch holding three stones that reresent your ancestors.'
    elif roll == 5:
        response = 'A few small bones from the first beast you killed, tied together with coloured woool.'
    elif roll == 6:
        response = 'An egg-sized stone in the shape of your spirit animal that appeared one day in your belt pouch.'

    return response

## Thinking about accepting arguments because all classes use the result of 3 d6 rolls.
def Tattoos(roll):
    if roll == 1:
        response = 'The wings of an eagle are spread wide across your upper back.'
    elif roll == 2:
        response = 'Etched on the backs of your hands are the paws of a cave bear.'
    elif roll == 3:
        response = 'The symbols of your clan are displayed in viny patterns along your arms.'
    elif roll == 4: 
        response = 'The antlers of an elk are inked across your back.'
    elif roll == 5:
        response = 'Images of your spirit animal are tattooed along your weapon arm and hand.'
    elif roll == 6:
        response = 'The eyes of a wolf are marked on your back to help yu see and ward off evil spirits.'

    return response

def Superstitions(roll):
    if roll == 1:
        response = 'If you disturb the bones of the dead, you inherit all the troubles that plagued them in life.'
    elif roll == 2:
        response = 'Never trust a wizard. They\'re all devils in disguise, especially the friendly ones.'
    elif roll == 3:
        ##Should I put a thing to prevent a dwarf from rolling this, or have a self hating dwarf.
        response = 'Dwarves have lost their spirits, and are almost like the undead. That\'s why they live underground.'
    elif roll == 4:
        response = 'Magical things bring you trouble. Never sleep with a magic object within ten feet of you.'
    elif roll == 5:
        response = 'When you walk through a graveyward, be sure to wear silver, or a ghost might jump into your body.'
    elif roll == 6:
        response = 'If an elf looks you in the eyes, she''s trying to read your thoughts.'

    return response

def ClassTraining(roll):
    emb = []
    emb += ['your devotion to your people lifted you in battle, making you powerful and dangerous.']
    emb += ['the spirits of your ancestors called on you to carry out a great task.']
    emb += ['you lost control in battle one day, and it was as if something else was manipulating your body, forcing it to kill every foe you could reach.']
    emb += ['you went on a spiritual journey to find yourself and instead found a spirit animal to guide, protect and inspire you.']
    emb += ['you were struck by lightning and lived. Afterward, you found a new strength within you that let you push beyond your limitations.']
    emb += ['your anger needed to be channeled into battle, or you risked becoming an indiscriminate killer.']
    result = 'You became a barbarian because ' + TableHelper.dSixTable(emb, roll) + lineBreak
    return result