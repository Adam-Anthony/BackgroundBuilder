## Preamble not finished
import random as rng
import TableHelper
lineBreak = '\n'
blankSpace = ' '

def RogueTables(rolls):
    result = 'You are a rogue.' + lineBreak
    #
    trainRoll = rng.randint(1,6)
    result += (ClassTraining(trainRoll) + lineBreak)
    #
    ## first
    result += ('Guilty Pleasure:' + blankSpace)
    result += (GuiltyPleasures(rolls[0]) + lineBreak)
    #
    ## Homelands
    result += ('Adversary:' + blankSpace)
    result += (Adversaries(rolls[1]) + lineBreak)
    #
    ## SwornEnemys
    result += ('Benefactor:' + blankSpace)
    result += (Benefactors(rolls[2]) + lineBreak)
    #
    return result

def GuiltyPleasures(roll):
    emb = []
    emb += ['Large gems.']
    emb += ['A smile from a pretty face.']
    emb += ['A new ring for your finger.']
    emb += ['The chance to deflate someone\'s ego.']
    emb += ['The finest food and drink.']
    emb += ['Adding to your collection of exotic coins.']
    #
    return TableHelper.dSixTable(emb, roll)

def Adversaries(roll):
    emb = []
    emb += ['The pirate captain on whose ship you once served; what you call moving on, the captain calls mutiny.']
    emb += ['A master spy to whom you unwittingly fed bad information, which led to the assassination of the wrong target.']
    emb += ['The master of the local thieves\' guild, who wants you to join the organization or leave town.']
    emb += ['An art collector who uses illegal means to acquire masterpieces.']
    emb += ['A fence who uses you as a messenger to set up illicit meetings.']
    emb += ['The proprietor of an illegal pit fighting arena where you once took bets.']
    #
    return TableHelper.dSixTable(emb, roll)

def Benefactors(roll):
    emb = []
    emb += ['A smuggler kept you from getting caught but lost a valuable shipment in doing so. Now you owe that person an equally valuable favor.']
    emb += ['The Beggar King has hidden you from your pursuers many times, in return for future considerations.']
    emb += ['A magistrate once kept you out of jail in return for information on a powerful crime lord.']
    emb += ['Your parents used their savings to bail you out of trouble in your younger days and are now destitute.']
    emb += ['A dragon didn\'t eat you when it had a chance, and in return you promised to set aside choice pieces of treasure for it']
    emb += ['A druid once helped you out of a tight spot; now any random animal you see could be that benefactor, perhaps come to claim a return favor.']
    #
    return TableHelper.dSixTable(emb, roll)

def ClassTraining(roll):
    emb = []
    emb += ['You have always been nimble and quick of wit, so you decided to use those talents to help you make your way in the world.']
    emb += ['An assassin or a thief wronged you, so you focused your training on mastering the skills of your enemy to better combat foes of that sort.']
    emb += ['An experienced rogue saw something in you and taught you several useful tricks.']
    emb += ['you decided to turn your natural lucky streak into the basis of a career, though you still realize that improving your skills is essential.']
    emb += ['you took up with a group of ruffians who showed you how to get what you want through sneakiness rather than direct confrontation.']
    emb += ['you are a sucker for a shiny bauble or a sack of coins, as long as you can get your hands on it without risking life and limb.']
    result = 'You became a rogue because ' + TableHelper.dSixTable(emb, roll) + lineBreak
    return result