## Entertainer
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '
indentSpace = '    '

def GetResults():
    result = 'Your background is an entertainer.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    result += Routines()
    return result

def Trait():
    emb = []
    emb += ['I know a story relevant to almost every situation.']
    emb += ['Whenever I come to a new place, I collect local rumors and spread gossip.']
    emb += ['I\'m a hopeless romantic, always searching for that \"special someone.\"']
    emb += ['Nobody stays angry at me or around me for long, since I can defuse any amount of tension.']
    emb += ['I love a good insult, even one directed at me.']
    emb += ['I get bitter if I\'m not the center of attention.']
    emb += ['I\'ll settle for nothing less than perfection.']
    emb += ['I change my mood or my mind as quickly as I change key in a song.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    emb += ['Beauty. When I perform, I make the world better than it was.']
    emb += ['Tradition. The stories, legends, and songs of the past must never be forgotten, for they teach us who we are.']
    emb += ['Creativity. The world is in need of new ideas and bold action.']
    emb += ['Greed. I\'m only in it for the money and fame.']
    emb += ['People. I like seeing the smiles on people\'s faces when I perform. That\'s all that matters.']
    emb += ['Honesty. Art should reflect the soul; it should come from within and reveal who we really are.']
    align = []
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
    emb += ['My instrument is my most treasured possession, and it reminds me of someone I love.']
    emb += ['Someone stole my precious instrument, and someday I\'ll get it back.']
    emb += ['I want to be famous, whatever it takes.']
    emb += ['I idolize a hero of the old tales and measure my deeds against that person\'s.']
    emb += ['I will do anything to prove myself superior to my hated rival.']
    emb += ['I would do anything for the other members of my old troupe.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['I\'ll do anything to win fame and renown.']
    emb += ['I\'m a sucker for a pretty face.']
    emb += ['A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.']
    emb += ['I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.']
    emb += ['I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.']
    emb += ['Despite my best efforts, I am unreliable to my friends.']
    return Personality.Flaws(emb)

def Routines():
    roll = rng.randint(1,10)
    emb = []
    emb += ['Actor']
    emb += ['Dancer']
    emb += ['Fire-eater']
    emb += ['Jester']
    emb += ['Juggler']
    emb += ['Instrumentalist']
    emb += ['Poet']
    emb += ['Singer']
    emb += ['Storyteller']
    emb += ['Tumbler']
    return ('Entertainer Routine:' + newLine + indentSpace + TableHelper.dTenTable(emb,roll) + newLine)

def Decision():
    roll = rng.randint(1,6)
    emb = []
    emb += ['members of my family made ends meet by performing, so it was fitting for me to follow their example.']
    emb += ['I always had a keen insight into other people, enough so that I could make them laugh or cry with my stories or songs.']
    emb += ['I ran away from home to follow a minstrel troupe.']
    emb += ['I saw a bard perform once, and I knew from that moment on what I was born to do.']
    emb += ['I earned coin by performing on street corners and eventually made a name for myself.']
    emb += ['a traveling entertainer took me in and taught me the trade.']
    return ('I became an entertainer because ' + TableHelper.dSixTable(emb, roll) + newLine)