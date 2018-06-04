## Sailor
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '

def GetResults():
    result = 'Your background is a sailor.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    return result

def Trait():
    emb = []
    emb += ['My friends know they can rely on me, no matter what.']
    emb += ['I work hard so that I can play hard when the work is done.']
    emb += ['I enjoy sailing into new ports and making new friends over a flagon of ale.']
    emb += ['I stretch the truth for the sake of a good story.']
    emb += ['To me, a tavern brawl is a nice way to get to know a new city.']
    emb += ['I never pass up a friendly wager.']
    emb += ['My language is as foul as an otyugh nest.']
    emb += ['I like a job well done, especially if I can convince someone else to do it.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    align = []
    emb += ['Respect. The thing that keeps a ship together is mutual respect between captain and crew.']
    emb += ['Fairness. We all do the work, so we all share in the rewards.']
    emb += ['Freedom. The sea is freedom--the freedom to go anywhere and do anything.']
    emb += ['Mastery. I\'m a predator, and the other ships on the sea are my prey.']
    emb += ['People. I\'m committed to my crewmates, not to ideals.']
    emb += ['Aspiration. Someday I\'ll own my own ship and chart my own destiny.']
    #
    align += ['(Good)']
    align += ['(Lawful)']
    align += ['(Chaotic)']
    align += ['(Evil)']
    align += ['(Neutral)']
    align += ['(Any)']
    #
    return Personality.Ideals(emb, align)

def Bond():
    emb = []
    emb += ['I\'m loyal to my captain first, everything else second.']
    emb += ['The ship is most important--crewmates and captains come and go.']
    emb += ['I\'ll always remember my first ship.']
    emb += ['In a harbor town, I have a paramour whose eyes nearly stole me from the sea.']
    emb += ['I was cheated out of my fair share of the profits, and I want to get my due.']
    emb += ['Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance will be mine.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['I follow orders, even if I think they\'re wrong.']
    emb += ['I\'ll say anything to avoid having to do extra work.']
    emb += ['Once someone questions my courage, I never back down no matter how dangerous the situation.']
    emb += ['Once I start drinking, it\'s hard for me to stop.']
    emb += ['I can\'t help but pocket loose coins and other trinkets I come across.']
    emb += ['My pride will probably lead to my destruction.']
    return Personality.Flaws(emb)

def Decision():
    roll = rng.randint(1,6)
    emb = []
    emb += ['I was press-ganged by pirates and forced to serve on their ship until I finally escaped.']
    emb += ['I wanted to see the world, so I signed on as a deckhand for a merchant ship.']
    emb += ['one of my relatives was a sailor who took me to sea.']
    emb += ['I needed to escape my community quickly, so I stowed away on a ship. When the crew found me, I was forced to work for my passage.']
    emb += ['Reavers attacked my community, so I found refuge on a ship until I could seek vengeance.']
    emb += ['I had few prospects where I was living, so I left to find my fortune elsewhere.']
    return ('I became a sailor because ' + TableHelper.dSixTable(emb, roll) + newLine)