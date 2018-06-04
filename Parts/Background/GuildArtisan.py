## Guild Artisan
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '
indentSpace = '    '

def GetResults():
    result = 'Your background is a guild artisan.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    result += Business()
    return result

def Trait():
    emb = []
    emb += ['I believe that anything worth doing is worth doing right. I can\'t help it--I\'m a perfectionist']
    emb += ['I\'m a snob who looks down on those who can\'t appreciate fine art.']
    emb += ['I always want to know how things work and what makes people tick.']
    emb += ['I\'m full of witty aphorisms and have a proverb for every occasion.']
    emb += ['I\'m rude to people who lack my commitment to hard work and fair play.']
    emb += ['I like to talk at length about my profession.']
    emb += ['I don\'t part with my money easily and will haggle tirelessly to get the best deal possible.']
    emb += ['I\'m well known for my work, and I want to make sure everyone appreciates it. I\'m always taken aback when people haven\'t heard of me.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    emb += ['Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization.']
    emb += ['Generosity. My talents were given to me so that I could use them to benefit the world.']
    emb += ['Freedom. Everyone should be free to pursue his or her own livelihood.']
    emb += ['Greed. I\'m only in it for the money.']
    emb += ['People. I\'m committed to the people I care about, not to ideals.']
    emb += ['Aspiration. I work hard to be the best there is at my craft.']
    #
    ideal = []
    ideal += ['(Lawful)']
    ideal += ['(Good)']
    ideal += ['(Chaotic)']
    ideal += ['(Evil)']
    ideal += ['(Neutral)']
    ideal += ['(Any)']
    return Personality.Ideals(emb, ideal)

def Bond():
    emb = []
    emb += ['The workshop where I learned my trade is the most important place in the world to me.']
    emb += ['I created a great work for someone, and then found them unworthy to receive it. I\'m still looking for someone worthy.']
    emb += ['I owe my guild a great debt for forging me into the person I am today.']
    emb += ['I pursue wealth to secure someone\'s love.']
    emb += ['One day I will return to my guild and prove that I am the greatest artisan of them all.']
    emb += ['I will get revenger on the evil forces that destroyed my place of business and ruined my livelihood.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['I\'ll do anything to get my hands on something rare or priceless.']
    emb += ['I\'m quick to assume that someone is trying to cheat me.']
    emb += ['No one must ever learn that I once stole money from guild coffers.']
    emb += ['I\'m never satisfied with what I have--I always want more.']
    emb += ['I would kill to acquire a noble title.']
    emb += ['I\'m horribly jealous of anyone who can outshine my handiwork. Everywhere I go, I\'m surrounded by rivals.']
    return Personality.Flaws(emb)

def Business():
    roll = rng.randint(1,20)
    emb = []
    emb += ['Alchemists and apothecaries.']
    emb += ['Armorers, locksmiths, and finesmiths.']
    emb += ['Brewers, distillers, and vintners.']
    emb += ['Calligraphers, scribes, and scriveners.']
    emb += ['Carpenters, roofers, and plasterers.']
    emb += ['Cartographers, surveyors, and chart-makers.']
    emb += ['Cobblers and shoemakers.']
    emb += ['Cooks and bakers']
    emb += ['Glassblowers and glaziers.']
    emb += ['Jewelers and gemcutters.']
    emb += ['Leatherworkers, skinners, and tanners.']
    emb += ['Masons and stonecutters.']
    emb += ['Painters, limners, and sign-makers.']
    emb += ['Potters and tile-makers.']
    emb += ['Shipwrights and sailmakers.']
    emb += ['Smiths and metal-forgers.']
    emb += ['Tinkers, pewterers, and casters.']
    emb += ['Wagon=makers and wheelwrights.']
    emb += ['Weavers and dyers.']
    emb += ['Woodcarvers, coopers, and bowyers.']
    return ('Guild Business:' + newLine + indentSpace + TableHelper.dTwentyTable(emb,roll) + newLine)
def Decision():
    roll = rng.randint(1,6)
    emb = []
    emb += ['I was apprenticed to a master who taught me the guild\'s business.']
    emb += ['I helped a guild artisan keep a secret or complete a task, and in return I was taken on as an apprentice.']
    emb += ['one of my family members who belonged to the guild made a place for me.']
    emb += ['I was always good with my hands, so I took the opportunity to learn a trade.']
    emb += ['I wanted to get away from my home situation and start a new life.']
    emb += ['I learned the essentials of my craft from a mentor but had to join the guild to finish my training.']
    return ('I became a guild artisan because ' + TableHelper.dSixTable(emb, roll) + newLine)