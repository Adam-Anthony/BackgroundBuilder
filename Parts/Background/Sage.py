## Sage
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '
indentSpace = '    '

def GetResults():
    result = 'Your background is a sage.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    result += Specialty()
    return result

def Trait():
    emb = []
    emb += ['I use polysyllabic works that convey the impression of great erudition.']
    emb += ['I\'ve read every book in the world\'s greatest libraries--or I like to boast that I have.']
    emb += ['I\'m used to helping out those who aren\'t as smart as I am, and I patiendtly explain anything and everything to others.']
    emb += ['There\'s nothing I like more than a good mystery.']
    emb += ['I\'m willing to listen to every side of an argument before I make my own judgement.']
    emb += ['I...speak...slowly...when talking...to idiots,...which...almost...everyone...is...compared...to me.']
    emb += ['I am horribly, horribly awkward in social situations.']
    emb += ['I\'m convinced that people are always trying to steal my secrets.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    align = []
    emb += ['Knowledge. The path to power and self-improvement is through knowledge.']
    emb += ['Beauty. What is beautiful points us beyond itself toward what is true.']
    emb += ['Logic. Emotions must not cloud our logical thinking.']
    emb += ['No Limits. Nothing should fetter the infinite possibility inherent in all existence.']
    emb += ['Power. Knowledge is the path to power and domination.']
    emb += ['Self-Improvement. The goal of a life of study is the betterment of oneself.']
    #
    align += ['(Neutral)']
    align += ['(Good)']
    align += ['(Lawful)']
    align += ['(Chaotic)']
    align += ['(Evil)']
    align += ['(Any)']
    #
    return Personality.Ideals(emb, align)

def Bond():
    emb = []
    emb += ['It is my duty to protect my students.']
    emb += ['I have an ancient text that holds terrible secrets that must not fall into the wrong hands.']
    emb += ['I work to preserve a library, university, scriptorium, or monastery.']
    emb += ['My life\'s work is a series of tomes related to a specific field of lore.']
    emb += ['I\'ve been searching my whole life for the answer to a certain question.']
    emb += ['I sold my soul for knowledge. I hope to do great deeds and win it back.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['I am easily distracted by the promise of information.']
    emb += ['Most people scream and run when they see a demon. I stop and take notes on its anatomy.']
    emb += ['Unlocking an ancient mystery is worth the price of a civilization.']
    emb += ['I overlook obvious solutions in favor of complicated ones.']
    emb += ['I speak without really thinking through my words, invariably insulting others.']
    emb += ['I can\'t keep a secret to save my life, or anyone else\'s.']
    return Personality.Flaws(emb)

def Specialty():
    roll = rng.randint(1,8)
    emb = []
    emb += ['Alchemist']
    emb += ['Astronomer']
    emb += ['Discredited academic']
    emb += ['Librarian']
    emb += ['Professor']
    emb += ['Researcher']
    emb += ['Wizard\'s apprentice']
    emb += ['Scribe']
    return ('Specialty:' + newLine + indentSpace + TableHelper.dEightTable(emb, roll) + newLine)
    
def Decision():
    roll = rng.randint(1,6)
    emb = []
    emb += ['I was naturally curious, so I packed up and went to a university to learn more about the world.']
    emb += ['my mentor\'s teachings opened my mind to new possibilities in that field of study.']
    emb += ['I was always an avid reader, and I learned much about my favorite topic on my own.']
    emb += ['I discovered an old library and pored over the texts I found there. That experience awakened a hunger for more knowledge.']
    emb += ['I impressed a wizard who told me I was squandering my talents and should seek out an education to take advantage of my gifts.']
    emb += ['One of my parents or a relative gave me a basic education that whetted my appetite, and I left home to build on what I had learned.']
    return ('I became a sage because ' + TableHelper.dSixTable(emb, roll) + newLine)