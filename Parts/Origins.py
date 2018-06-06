import random as rng
lineBreak = '\n'
indentSpace = '    '
class Parents():
	race = 'aaaa'
	known = False
	def __init__(self, race):
		super(Parents, self).__init__()
		self.race = race

	def KnownParents(self):
		response = ''
		roll = rng.randint(1,20)
		if roll < 20:
			response = 'You know who your parents are or were.'
			self.known = True
		elif roll == 20:
			response = 'You do not know who your parents were.'
		if self.known:
			response += self.Nonhuman()
		response += lineBreak
		response += self.Family()
		return response + lineBreak

	def Family(self):
		response = 'Family: '
		if self.known == False:
			roll = rng.randint(1,35)
		else:
			roll = rng.randint(1,100)
		parentMissing = False
		bothMissing = False
		#
		#
		if roll == 1:
			response += 'None.'
			parentMissing = True
			bothMissing = True
		elif roll == 2:
			response += 'Institution, such as an asylum.'
			parentMissing = True
			bothMissing = True
		elif roll == 3:
			response += 'Temple.'
			parentMissing = True
			bothMissing = True
		elif roll >=4 and roll <= 5:
			response += 'Orphanage.'
			parentMissing = True
			bothMissing = True
		elif roll >=6 and roll <= 7:
			response += 'Guardian.'
			parentMissing = True
			bothMissing = True
		elif roll >= 8 and roll <= 15:
			response += 'Paternal or maternal aunt, uncle, or both; or extended family such as a tribe or clan.'
			parentMissing = True
			bothMissing = True
		elif roll >= 16 and roll <= 25:
			response += 'Paternal or maternal grandparent(s).'
			parentMissing = True
			bothMissing = True
		elif roll >= 26 and roll <= 35:
			response += 'Adoptive family (same or different race).'
			parentMissing = True
			bothMissing = True
		elif roll >= 36 and roll <= 55:
			response += 'Single father or stepfather.'
			parentMissing = True
		elif roll >= 56 and roll <= 75:
			response += 'Single mother or stepmother.'
			parentMissing = True
		elif roll >= 76 and roll <= 100:
			response += 'Mother and father.'
		if self.known == False:
			response += lineBreak
		elif parentMissing:
			response += lineBreak + indentSpace
			if bothMissing:
				response += self.AbsentParents(False) + lineBreak + indentSpace
			response += self.AbsentParents(True) + lineBreak
		
		return response
	#
	def AbsentParents(self, both):
		response = ''
		other = ''
		if both:
			other = 'other '
		roll = rng.randint(1,4)
		if roll == 1:
			response = 'Your '+ other +'parent died.'
			#Roll on the cause of death supplemental table
		elif roll == 2:
			response = 'Your '+ other +'parent was imprisoned, enslaved, or otherwise taken away.'
		elif roll == 3:
			response = 'Your '+ other +'parent abandoned you.'
		elif roll == 4:
			response = 'Your '+ other +'parent disappeared to an unknown fate.'
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
			result = self.HalfElf() + lineBreak
		if self.race=='half-orc':
			result = self.HalfOrc() + lineBreak
		if self.race=='tiefling':
			result = self.Tiefling() + lineBreak
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
	return response+lineBreak

def NumberOfSiblings(race):
	roll = rng.randint(1,10)
	res = 0
	result = 'Number of siblings: '
	## Racial -2 for Dwarf or Elf
	if race == 'dwarf' or race == 'elf':
		roll = roll - 2
	if roll <= 2:
		res = 0
	elif roll >= 3 and roll <= 4:
		res = rng.randint(1,3)
	elif roll >= 5 and roll <= 6:
		res = rng.randint(1,4) + 1
	elif roll >= 7 and roll <= 8:
		res = rng.randint(1,6) + 2
	elif roll >= 9:
		res = rng.randint(1,8) + 3
	result += (str(res) + lineBreak)
	if res > 0:
		ages = [0,0,0]
		for i in range(0, res):
			ageVar = Siblings()
			ages[ageVar] += 1
		if ages[0] > 0:
			result += 'Younger: ' + str(ages[0]) + lineBreak
		if ages[1] > 0:
			result += 'Same Age: ' + str(ages[1]) + lineBreak
		if ages[2] > 0:
			result += 'Older: ' + str(ages[2]) + lineBreak
	return result
		## Younger, Same, Older

	## For each one, need occupation, aligment, status, relationship

def Siblings():
	roll = rng.randint(1,6) + rng.randint(1,6)
	if roll == 2:
		return 1
	elif roll >=3 and roll <= 7:
		return 0
	elif roll >= 8:
		return 2

class FamilyLife():
	"""docstring for Family"""
	modifier = 0
	chaMod = 0
	def __init__(self, chaMod):
		super(FamilyLife, self).__init__()
		self.chaMod = chaMod
	#
	def getResults(self):
		response = self.FamilyLifestyle()
		response += self.ChildhoodHome()
		## response += self.ChildhoodMemories()
		return response
	#
	def FamilyLifestyle(self):
		roll = rng.randint(1,6) + rng.randint(1,6) + rng.randint(1,6)
		result = 'Lifestyle: '
		if roll == 3:
			result += 'Wretched'
			self.modifier = -40
		elif roll >= 4 and roll <= 5:
			result += 'Squalid'
			self.modifier = -20
		elif roll >= 6 and roll <= 8:
			result += 'Poor'
			self.modifier = -10
		elif roll >= 9 and roll <= 12:
			result += 'Modest'
			self.modifier = 0
		elif roll >= 13 and roll <= 15:
			result += 'Comfortable'
			self.modifier = 10
		elif roll >=16 and roll <= 17:
			result += 'Wealthy'
			self.modifier = 20
		elif roll == 18:
			result += 'Aristocratic'
			self.modifier = 40
		return result + lineBreak
	#
	def ChildhoodHome(self):
		roll = rng.randint(1,100) + self.modifier
		result = 'Childhood Home: '
		if roll <= 0:
			result += 'On the streets.'
		elif roll >= 1 and roll <= 20:
			result += 'Rundown shack.'
		elif roll >= 21 and roll <= 30:
			result += 'No permanent residence; you moved around a lot.'
		elif roll >= 31 and roll <= 40:
			result += 'Encampment or village in the wilderness.'
		elif roll >= 41 and roll <= 50:
			result += 'Apartment in a rundown neighborhood.'
		elif roll >= 51 and roll <= 70:
			result +=  'Small house.'
		elif roll >= 71 and roll <= 90:
			result += 'Large house.'
		elif roll >= 91 and roll <= 110:
			result += 'Mansion.'
		elif roll >= 111:
			result += 'Palace or Castle.'
		return result + lineBreak
	#
	def ChildhoodMemories(self):
		roll = rng.randint(1,6) + rng.randint(1,6) + rng.randint(1,6) + self.chaMod
		## Have to then add a Cha modifier.

##Family

##AbsentParent

##Family Lifestyle

##Childhood Home

##Childhood Memories