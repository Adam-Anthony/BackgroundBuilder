import Parts.TableHelper as TableHelper
def Traits(emb):
	r1 = rng.randint(1,8)
	r2 = rng.randint(1,8)
	while r2==r1:
		r2 = rng.randint(1,8)
	rolls = [r1, r2]
	print(' ')
	foo = TableHelper.XdEightTable(emb, rolls)

def Ideals(emb):
	roll = rng.randint(1,6)
	print(' ')
	foo = TableHelper.dSixTable(emb, roll)

def Bonds(emb):
	roll = rng.randint(1,6)
	print(' ')
	foo = TableHelper.dSixTable(emb, roll)

def Flaws(emb):
	roll = rng.randint(1,6)
	print(' ')
	foo = TableHelper.dSixTable(emb, roll)