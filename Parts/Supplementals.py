import random as rng

## Key Table
def Alignment():
	roll = rng.randint(1,6) + rng.randint(1,6) + rng.randint(1,6)
	response = ''
	if roll == 3:
		if rng.randint(1,2) == 1:
			response = 'Chaotic evil.'
		else:
			response = 'Chaotic neutral.'
	elif roll == 4 or roll == 5:
		response = 'Lawful evil.'
	elif roll >= 6 and roll <= 8:
		response = 'Neutal Evil.'
	elif roll >= 9 and roll <= 12:
		response = 'Neutral.'
	elif roll >= 13 and roll <= 15:
		response = 'Neutral good.'
	elif roll == 16 or roll == 17:
		if rng.randint(1,2) == 1:
			response = 'Lawful Good.'
		else:
			response = 'Lawful Neutral.'
	elif roll == 18:
		if rng.randint(1,2) == 1:
			response = 'Chaotic Good.'
		else:
			response = 'Chaotic Neutral.'
	return response

## Suboption from Status table
def CauseOfDeath():
	roll = rng.randint(1,12)
	response = ''
	if roll == 1:
		response = 'Unknown.'
	elif roll == 2:
		response = 'Murdered.'
	elif roll == 3:
		response = 'Killed in battle.'
	elif roll == 4:
		response = 'Accident related to class or occupation.'
	elif roll == 5:
		response = 'Accident unrelated to class or occupation.'
	elif roll == 6 or roll == 7:
		response = 'Natural causes, such as disease or old age.'
	elif roll == 8:
		response = 'Apparent Suicide.'
	elif roll == 9:
		response = 'Torn appart by an animal or a natural disaster.'
	elif roll == 10:
		response = 'Consumed by a monster.'
	elif roll == 11:
		response = 'Executed for a crime or tortured to death.'
	elif roll == 12:
		response = 'Bizarre event, such as being hit by a meteroite, struck down by an angry god, or killed by a hatching slaad egg.'

	return response

## Suboption from Occupation table
def CharClass():
	roll = rng.randint(1,100)
	response = ''
	if roll >= 1 and roll <= 7:
		response = 'Barbarian.'
	elif roll >= 8 and roll <= 14:
		response = 'Bard.'
	elif roll >= 15 and roll <= 29:
		response = 'Cleric.'
	elif roll >= 30 and roll <= 36:
		response = 'Druid.'
	## Fight
	elif roll >= 37 and roll <= 52:
		response = 'Fighter.'
	elif roll >= 53 and roll <= 58:
		response = 'Monk.'
	elif roll >= 59 and roll <= 64:
		response = 'Paladin.'
	elif roll >= 65 and roll <= 70:
		response = 'Ranger.'
	elif roll >= 71 and roll <= 84:
		response = 'Rogue.'
	elif roll >= 85 and roll <= 89:
		response = 'Sorcerer.'
	elif roll >= 90 and roll <= 94:
		response = 'Warlock.'
	elif roll >= 95 and roll <= 100:
		response = 'Wizard.'

	return response

## Key Table
def Occupation():
	roll = rng.randint(1,100)
	response = ''
	if roll <= 5:
		response = 'Academic.'
	elif roll >= 6 and roll <= 10:
		response = 'Adventurer.'
		CharClass()
	elif roll == 11:
		response = 'Aristocrat.'
	elif roll >= 12 and roll <= 26:
		response = 'Artisan or guild member.'
	elif roll >= 27 and roll <= 31:
		response = 'Criminal.'
	elif roll >= 32 and roll <= 36:
		response = 'Entertainer.'
	elif roll >= 37 and roll <= 38:
		response = 'Exile, hermit, or refugee'
	elif roll >= 39 and roll <= 43:
		response = 'Explorer or wanderer.'
	elif roll >= 44 and roll <= 55:
		response = 'Farmer or herder.'
	elif roll >= 56 and roll <= 60:
		response = 'Hunter or trapper.'
	elif roll >= 61 and roll <= 75:
		response = 'Laborer.'
	elif roll >= 76 and roll <= 80:
		response = 'Merchant'
	elif roll >= 81 and roll <= 85:
		response = 'Politician or bureaucrat.'
	elif roll >= 86 and roll <= 90:
		response = 'Priest.'
	elif roll >= 91 and roll <= 95:
		response = 'Sailor.'
	elif roll >= 96 and roll <= 100:
		response = 'Soldier.'
	return response

## Key Table
def Race():
	roll = rng.randint(1,100)
	response = ''
	if roll >= 1 and roll <= 40:
		response = 'Human.'
	elif roll >= 41 and roll <= 50:
		response = 'Dwarf.'
	elif roll >= 51 and roll <= 60:
		response = 'Elf.'
	elif roll >= 61 and roll <= 70:
		response = 'Halfling'
	elif roll >= 71 and roll <= 75:
		response = 'Dragonborn'
	elif roll >= 76 and roll <= 80:
		response = 'Gnome'
	elif roll >= 81 and roll <= 85:
		response = 'Half-elf'
	elif roll >= 86 and roll <= 90:
		response = 'Half-orc'
	elif roll >= 91 and roll <= 95:
		response = 'Tiefling'
	elif roll >= 96 and roll >= 100:
		response = 'Dm \'s Choice'
	return response

## Key Table
def Relationship():
	roll = rng.randint(1,4) + rng.randint(1,4) + rng.randint(1,4)
	response = ''
	if roll >= 3 and roll <= 4:
		response = 'Hostile.'
	elif roll >= 5 and roll <= 10:
		response = 'Friendly.'
	elif roll >= 11 and roll <= 12:
		response = 'Indifferent.'
	return response

## Key Table
def Status():
	roll = rng.randint(1,6) + rng.randint(1,6) + rng.randint(1,6)
	response = ''
	roll = 3
	if roll == 3:
		response = 'Dead.'
		CauseOfDeath()
		##We roll on the Cause of Death table from here
	elif roll >= 4 and roll <= 5:
		response = 'Missing or unknown.'
	elif roll >= 6 and roll <= 8:
		response = 'Alive, but doing poorly due to injury, financial trouble, or relationship difficulties.'
	elif roll >= 9 and roll <= 12:
		response = 'Alive and well.'
	elif roll >= 13 and roll <= 15:
		response = 'Alive and quite successful.'
	elif roll >= 16 and roll <= 17:
		response = 'Alive and infamous.'
	elif roll == 18:
		response = 'Alive and famous.'
	return response