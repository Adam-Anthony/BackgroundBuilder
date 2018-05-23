import random as rng
lineBreak = '\n'
blankSpace = ' '
def ClericTables(rolls):
	result = 'You are a cleric.' + lineBreak

	result += (Temple(rolls[0]) + lineBreak)

	result += 'You have a keepsake, meant to symbolize their faith.' + blankSpace
	result += (Keepsake(rolls[1]) + lineBreak)

	result += 'Every cleric must grapple with a dark secret, you are no different.' + blankSpace
	result += (Secret(rolls[2]) + lineBreak)
	
	return result

def Temple(roll):
	if roll == 1:
		response = 'Your temple is said to be the oldest surviving structure built to honor your god.'
	elif roll == 2:
		response = 'Acolytes of several like-minded deities all received instruction together in your temple.'
	elif roll == 3:
		response = 'You come from a temple famed for the brewery it operates. Some say you smell like one of its ales.'
	elif roll == 4:
		response = 'Your temple is a fortress and a proving ground that trains warrior-priests.'
	elif roll == 5:
		response = 'Your temple is a peaceful, humble place, filled with vegetable gardens and simple priests.'
	elif roll == 6:
		response = 'You served in a temple in the Outer Planes.'

	return response


def Keepsake(roll):
	if roll == 1:
		response = 'The finger bone of a saint.'
	elif roll == 2:
		response = 'A metal-bound book that tells how to hunt and destroy infernal creatures.'
	elif roll == 3:
		response = 'A pig\'s whistle that reminds you of your humble and beloved mentor.'
	elif roll == 4:
		response = 'A braid of hair woven from the tail of a unicorn.'
	elif roll == 5:
		response = 'A scroll that describes how best to rid the world of necromancers.'
	elif roll == 6:
		response = 'A runestone said to be blessed by your god.'

	return response


def Secret(roll):
	if roll == 1:
		response = 'An imp offers you counsel. You try to ignore the creature, but sometimes its advice is helpful.'
	elif roll == 2:
		response = 'You believe that, in the final analysis, the gods are nothing more than ultrapoweful mortal creatures.'
	elif roll == 3:
		response = 'You acknowledge the power of the gods, but you think that most events are dictated by pure chance.'
	elif roll == 4:
		response = 'Even though you can work divine magic, you have never truly felt the presence of a divine essence within yourself.'
	elif roll == 5:
		response = 'You are plagued by nightmares that you believe are sent by your god as punishment for some unknown transgression.'
	elif roll == 6:
		response = 'In times of despair, you feel that you are but a plaything of the gods, and you resent their remoteness.'

	return response