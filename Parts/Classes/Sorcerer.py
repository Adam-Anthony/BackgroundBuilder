## Preamble is not finished
import random as rng
import Parts.TableHelper as TableHelper
lineBreak = '\n'
blankSpace = ' '

def SorcererTables(rolls):
	result = 'You are a sorcerer.' + lineBreak

	trainRoll = rng.randint(1,6)
	result += (ClassTraining(trainRoll) + lineBreak)
	
	## Arcane Origins
	result += (ArcaneOrigins(rolls[0]) + lineBreak)

	## Reactions
	result += (Reaction(rolls[1]) + lineBreak)

	## Supernatural Marks
	result += 'Many sorcerers have a subtle but telling physical trait that sets them apart from other folk.'
	result += (SupernaturalMarks(rolls[2]) + lineBreak)
	
	## Signs of Sorcery
	signRoll = rng.randint(1,6)
	result += (SignsOfSorcery(signRoll) + lineBreak)
	
	return result

def ArcaneOrigins(roll):
	emb = []
	emb += ['Your power arises from your family\'s bloodline. You are related to some powerful creature, or you inherited a blessing or a curse.']
	emb += ['You are the reincarnation of a being from another plane of existance.']
	emb += ['A powerful entity entered the world. Its magic changed you.']
	emb += ['Your birth was prophesied in an ancient text, and you are foretold to use your power for terrible ends.']
	emb += ['You are the product of generations of careful, selective breeding.']
	emb += ['You were made in a vat by an alchemist.']
	return TableHelper.dSixTable(emb, roll)

def Reaction(roll):
	emb = []
	emb += ['Your powers are seen as a great bleesing by those around you, and you are expected to use them in service to your community.']
	## Can roll on the inprison table.
	emb += ['Your powers caused destruction and even a death when they became evident, and you were treated as a criminal.']
	emb += ['Your neighbors hate and fear your power, causing them to shun you.']
	emb += ['You came to the attention of a sinister cult that plans on exploiting your abilities.']
	emb += ['People around you believe that your powers are a curse levied on your family for a past transgression.']
	emb += ['Your powers are believed to be tied to an ancient line of mad kings that supposedly ended in a bloody revolt over a century ago.']
	return TableHelper.dSixTable(emb, roll)

def SupernaturalMarks(roll):
	emb = []
	emb += ['Your eyes are an unusual colour, such as red.']
	emb += ['You have an extra toe on one foot.']
	emb += ['One of your ears is noticeably larger than the other.']
	emb += ['Your hair grows at a prodigious rate.']
	emb += ['You wrinkle your nose repeatedly while you are chewing.']
	emb += ['A red splotch appears on your neck once a day, then vanishes after an hour.']

	return TableHelper.dSixTable(emb, roll)

def SignsOfSorcery(roll):
	emb = []
	emb += ['You deliver the verbal components of your spells in the booming voice of a titan.']
	emb += ['For a moment after you cast a spell, the area around you grows dark and gloomy.']
	emb += ['You sweat profusely while casting a spell and for a few seconds thereafter.']
	emb += ['Your hair and garments are briefly buffeted about, as if by a breeze, whenever you call forth a spell.']
	emb += ['If you are standing when you cast a spell, you rise six inches into the air and gently float back down.']
	emb += ['Illusory blue flames wreathe your head as you begin your casting, then abruptly disappear.']
	return TableHelper.dSixTable(emb, roll)

def ClassTraining(roll):
	emb = []
	emb += ['when you were born, all the water in the house froze solid, the milk spoiled, or all the iron turned to copper. Your family is convinced that this event was a harbringer of stranger things to come for you.']
	emb += ['you suffered a terrible emotional or physical strain, which brought forth your latent magical power. You have fought to control it ever since.']
	emb += ['your immediate family never spoke of your ancestors, and when you asked, they would change the subject. It wasn\'t until you started displaying strange talents that the full truth of your heritage came out.']
	emb += ['when a monster threatened one of your friends, you became filled with anxiety. You lashed out instinctively and blasted the wretched thing with a force that came from within you.']
	## Want to roll for this stranger.
	emb += ['sensing something special in you, a stranger taught you how to control your gift.']
	emb += ['after you escaped from a magical conflagration, you realized that though you were unharmed, you were not unchanged. You began to exhibit unusual abilities that you are just beginning to understand.']
	result =  'You became a sorcerer because ' + TableHelper.dSixTable(emb, roll) + lineBreak
	return result