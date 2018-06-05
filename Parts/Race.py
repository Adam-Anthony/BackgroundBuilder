import random as rng

def RandomRaceNoWeight():
	result = ''
	roll = rng.randit(1,9)
	if roll == 1:
		result = 'dwarf'
	elif roll == 2:
		result = 'elf'
	elif roll == 3:
		result = 'halfling'
	elif roll == 4:
		result = 'human'
	elif roll == 5:
		result = 'dragonborn'
	elif roll == 6:
		result = 'gnome'
	elif roll == 7:
		result = 'half-elf'
	elif roll == 8:
		result = 'half-orc'
	elif roll == 9:
		result = 'tiefling'
	return result

def RandomRaceWeighted():
	result = ''
	roll = rng.randint(1,100)
	if roll <= 4:
		result = 'dragonborn'
	elif roll >= 5 and roll <= 13:
		result = 'dwarf'
		# Hill Dwarf
	elif roll >= 14 and roll <= 21:
		result = 'dwarf'
		# Mountain Dwarf
	elif roll >= 22 and roll <= 25:
		result = 'elf'
		# Dark Elf
	elif roll >= 26 and roll <= 34:
		result = 'elf'
		# High Elf
	elif roll >= 35 and roll <= 42:
		result = 'elf'
		# Wood Elf
	elif roll >= 43 and roll <= 46:
		result = 'gnome'
		# Forest Gnome
	elif roll >= 47 and roll <= 52:
		result = 'gnome'
		# Rock Gnome
	elif roll >= 53 and roll <= 56:
		result = 'half-elf'
	elif roll >= 57 and roll <= 60:
		result = 'half-orc'
	elif roll >= 61 and roll <= 68:
		result = 'halfling'
		# Lightfood Halfling
	elif roll >= 69 and roll <= 76:
		result = 'halfling'
		# Stout Halfling
	elif roll >= 77 and roll <= 96:
		result = 'human'
	elif roll >= 97:
		result = 'tiefling'
	return result