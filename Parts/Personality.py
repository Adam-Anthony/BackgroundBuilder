import Parts.TableHelper as TableHelper
import random as rng

indentSpace = '    '
newLine = '\n'

def Traits(emb):
	r1 = rng.randint(1,8)
	r2 = rng.randint(1,8)
	while r2==r1:
		r2 = rng.randint(1,8)
	rolls = [r1, r2]
	result = TableHelper.XdEightTable(emb, rolls)
	ret = 'Trait:' + newLine
	ret += indentSpace + result[0] + newLine
	ret += indentSpace + result[1] + newLine
	return ret

def Ideals(emb, ideal):
	roll = rng.randint(1,6)
	result = 'Ideal:' + newLine
	result += indentSpace + TableHelper.dSixTable(emb, roll) + newLine 
	result += indentSpace + TableHelper.dSixTable(ideal, roll) + newLine
	return result

def Bonds(emb):
	roll = rng.randint(1,6)
	result = 'Bond:' + newLine
	result += indentSpace + TableHelper.dSixTable(emb, roll) + newLine
	return result

def Flaws(emb):
	roll = rng.randint(1,6)
	result = 'Flaw:' + newLine
	result += indentSpace + TableHelper.dSixTable(emb, roll) + newLine
	return result