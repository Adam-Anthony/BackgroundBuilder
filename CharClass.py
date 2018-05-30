import random as rng 
#import Barbarian
#import Bard
#import Cleric

import Parts.Druid
import Parts.Fighter
import Parts.Monk

import Parts.Paladin
import Parts.Ranger
import Parts.Rogue

import Parts.Sorcerer
import Parts.Warlock
import Parts.Wizard

import Parts.TableHelper
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
        result = Barbarian().BarbarianTables(rolls)
        print(result)
    elif cc == 'Bard':
        result = Bard().BardTables(rolls)
        print(result)
    elif cc == 'Cleric':
        result = Cleric().ClericTables(rolls)
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

################################################################################




##### ##### #####       Barbarian   ##### ##### #####
class Barbarian():
    def __init__(self):
        super(Barbarian, self).__init__()
    def BarbarianTables(self,rolls):
        ## Probably want to add more details to these class details
        result = 'You are a barbarian.' + lineBreak
        #
        trainRoll = rng.randint(1,6)
        result += (self.ClassTraining(trainRoll) + lineBreak)
        #
        result += 'You have a personal totem, a small item that holds special significance.' + blankSpace
        result += (self.PersonalTotems(rolls[0]) + lineBreak)
        #
        ## Probably want this to flow better
        result += 'You have a tattoo.' + blankSpace
        result += (self.Tattoos(rolls[1]) + lineBreak)
        #
        result += 'You have a superstitious belief. If it comes from personal experience or the family/clan that raised you is for your to decide.' + blankSpace
        result += (self.Superstitions(rolls[2]) + lineBreak)
        #
        return result
    #
    def PersonalTotems(self,roll):
        emb = []
        emb += ['A tuft of fur from a solitary wolf that you befriended during a hunt.']
        emb += ['Three eagle feathers given to you by a wise shaman, who told you they would play a role in determining your fate.']
        emb += ['A necklace made from the claws of a young cave bear that you slew singlehandedly as a child.']
        emb += ['A small leather pouch holding three stones that reresent your ancestors.']
        emb += ['A few small bones from the first beast you killed, tied together with coloured woool.']
        emb += ['An egg-sized stone in the shape of your spirit animal that appeared one day in your belt pouch.']
        return TableHelper.dSixTable(emb, roll)
    #
    ## Thinking about accepting arguments because all classes use the result of 3 d6 rolls.
    def Tattoos(self,roll):
        emb = []
        emb += 'The wings of an eagle are spread wide across your upper back.'
        emb += 'Etched on the backs of your hands are the paws of a cave bear.'
        emb += 'The symbols of your clan are displayed in viny patterns along your arms.'
        emb += 'The antlers of an elk are inked across your back.'
        emb += 'Images of your spirit animal are tattooed along your weapon arm and hand.'
        emb += 'The eyes of a wolf are marked on your back to help yu see and ward off evil spirits.'
        return TableHelper.dSixTable(emb, roll)
    #
    def Superstitions(self,roll):
        emb = []
        emb += ['If you disturb the bones of the dead, you inherit all the troubles that plagued them in life.']
        emb += ['Never trust a wizard. They\'re all devils in disguise, especially the friendly ones.']
        ##Should I put a thing to prevent a dwarf from rolling this, or have a self hating dwarf.
        emb += ['Dwarves have lost their spirits, and are almost like the undead. That\'s why they live underground.']
        emb += ['Magical things bring you trouble. Never sleep with a magic object within ten feet of you.']
        emb += ['When you walk through a graveyward, be sure to wear silver, or a ghost might jump into your body.']
        emb += ['If an elf looks you in the eyes, she''s trying to read your thoughts.']
        return TableHelper.dSixTable(emb, roll)
    #
    def ClassTraining(self,roll):
        emb = []
        emb += ['your devotion to your people lifted you in battle, making you powerful and dangerous.']
        emb += ['the spirits of your ancestors called on you to carry out a great task.']
        emb += ['you lost control in battle one day, and it was as if something else was manipulating your body, forcing it to kill every foe you could reach.']
        emb += ['you went on a spiritual journey to find yourself and instead found a spirit animal to guide, protect and inspire you.']
        emb += ['you were struck by lightning and lived. Afterward, you found a new strength within you that let you push beyond your limitations.']
        emb += ['your anger needed to be channeled into battle, or you risked becoming an indiscriminate killer.']
        result = 'You became a barbarian because ' + TableHelper.dSixTable(emb, roll) + lineBreak
        return result
################################################################################




##### ##### #####       Bard       ##### ##### #####
class Bard():
    def __init__():
        super(Bard, self).__init__()
    def BardTables(rolls):
        result = 'You are a bard.' + lineBreak
        #
        trainRoll = rng.randint(1,6)
        result += (ClassTraining(trainRoll) + lineBreak)
        #
        result += 'Your defining work, spoken about for years. Perhaps a work in progress, or a staple of your performance. ' 
        result += (DefiningWork(rolls[0]) + lineBreak)
        #
        result += 'Any bard knows an instrument\'s entertainment value is as important as the music it plays. It might not be your only instrument, but it\'s a star. '
        result += (Instrument(rolls[1]) + lineBreak)
        #
        result += 'Almost every bard has suffered at least one bad experience in front of an audience. '
        result += (Embarrassments(rolls[2]) + lineBreak)
        #
        return result
    #
    def DefiningWork(roll):
        emb = []
        emb += ['\"The Three Flambinis\", a ribald song concerning mistaken identities and unfettered desire.']
        emb += ['\"Waltz of the Myconids\", an upbeat tune that children in particular enjoy.']
        emb += ['\"Asmodeus\' Golden Arse\", a dramatic poem you claim was inspired by your personal visit to Avernus.']
        emb += ['\"The Pirates of Luskan\", your firsthand account of being kidnapped by sea reavers as a child.']
        emb += ['\"A Hoop, Two Pigeons, and a Hell Hound\", a subtle parody of an incompetent noble.']
        emb += ['\"A Fool in the Abyss\", a comedic poem about a jester\'s travels among demons.']
        return TableHelper.dSixTable(emb, roll)
    #
    def Instrument(roll):
        emb = []
        emb += ['A masterfully crafted halfling fiddle.']
        emb += ['A mithral horn made by elves.']
        emb += ['A zither made with drow spider silk.']
        emb += ['An orcish drum.']
        emb += ['A wooden bullywug croak box.']
        emb += ['A tinker\'s harp of gnomish design.']
        return TableHelper.dSixTable(emb, roll)
    #
    def Embarrassments(roll):
        emb = []
        emb += ['The time when your comedic song, \"Big Tom\'s Hijinks\"--which, by the way, you thought was brilliant--did not go over well with Big Tom']
        emb += ['The mantinee performance when a circus\'s owlbear got loose and terrorized the crowd.']
        emb += ['When your opening song was your enthusiastic but universally hated rendition of \"Song of the Froghemoth\"']
        emb += ['The first and last performance of \"Mirt, Man about Town\".']
        emb += ['The time on stage when your wig caught fire and you threw it down--which set fire to the stage.']
        emb += ['When you sat on your lute by mistake during the final stanza of \"Starlight Serenade\".']
        return TableHelper.dSixTable(emb, roll)
    #
    def ClassTraining(roll):
        emb = []
        emb += ['you awakened your latent bardic abilities through trial and error.']
        emb += ['you were a gifted performer and attracted the attention of a master bard who schooled you in the old techniques.']
        emb += ['you joined a loose society of scholars and orators to learn new techniques of performance and magic.']
        emb += ['you felt a calling to recount the deeds of champions and heroes, to bring them alive in song and story.']
        emb += ['you joined one of the great colleges to learn old lore, the secrets of magic, and the art of performance.']
        emb += ['you picked up a musical instrument one day and instantly discovered that you could play it.']
        result = 'You became a bard because ' + TableHelper.dSixTable(emb, roll) + lineBreak
        return result
################################################################################




##### ##### #####       Cleric      ##### ##### #####
class Cleric():
    def __init__(self):
        super(Cleric, self).__init__()
    #
    def ClericTables(self, rolls):
        result = 'You are a cleric.' + lineBreak
        #
        trainRoll = rng.randint(1,6)
        result += (self.ClassTraining(trainRoll) + lineBreak)
        #
        result += (self.Temple(rolls[0]) + lineBreak)
        #
        result += 'You have a keepsake, meant to symbolize their faith.' + blankSpace
        result += (self.Keepsake(rolls[1]) + lineBreak)
        #
        result += 'Every cleric must grapple with a dark secret, you are no different.' + blankSpace
        result += (self.Secret(rolls[2]) + lineBreak)
        #
        return result

    def Temple(self, roll):
        emb = []
        emb += ['Your temple is said to be the oldest surviving structure built to honor your god.']
        emb += ['Acolytes of several like-minded deities all received instruction together in your temple.']
        emb += ['You come from a temple famed for the brewery it operates. Some say you smell like one of its ales.']
        emb += ['Your temple is a fortress and a proving ground that trains warrior-priests.']
        emb += ['Your temple is a peaceful, humble place, filled with vegetable gardens and simple priests.']
        emb += ['You served in a temple in the Outer Planes.']
        return TableHelper.dSixTable(emb, roll)

    def Keepsake(self, roll):
        emb = []
        emb += ['The finger bone of a saint.']
        emb += ['A metal-bound book that tells how to hunt and destroy infernal creatures.']
        emb += ['A pig\'s whistle that reminds you of your humble and beloved mentor.']
        emb += ['A braid of hair woven from the tail of a unicorn.']
        emb += ['A scroll that describes how best to rid the world of necromancers.']
        emb += ['A runestone said to be blessed by your god.']
        return TableHelper.dSixTable(emb, roll)

    def Secret(self, roll):
        emb = []
        emb += ['An imp offers you counsel. You try to ignore the creature, but sometimes its advice is helpful.']
        emb += ['You believe that, in the final analysis, the gods are nothing more than ultrapoweful mortal creatures.']
        emb += ['You acknowledge the power of the gods, but you think that most events are dictated by pure chance.']
        emb += ['Even though you can work divine magic, you have never truly felt the presence of a divine essence within yourself.']
        emb += ['You are plagued by nightmares that you believe are sent by your god as punishment for some unknown transgression.']
        emb += ['In times of despair, you feel that you are but a plaything of the gods, and you resent their remoteness.']
        return TableHelper.dSixTable(emb, roll)

    def ClassTraining(self, roll):
        emb = []
        emb += ['a suppernatural being in service to the gods called you to become a divine agent in the world.']
        emb += ['you saw the injustice and horror in the world and felt moved to take a stand against them.']
        emb += ['your god gave you an unmistakable sign. You dropped everything to serve the divine.']
        emb += ['although you were always devout, it wasn\'t until you completed a pilgrimage that you knew your true calling.']
        emb += ['you used to serve in your religion\'s bureaucracy but found you needed to work in the world, to bring the message of your faith to the darkest corners of the land.']
        emb += ['you realize that your god works through you, and you do as commanded, even though you don\'t know why you were chosen to serve.']
        result =  'You became a cleric because ' + TableHelper.dSixTable(emb, roll) + lineBreak
        return result
################################################################################




##### ##### #####       Druid      ##### ##### #####