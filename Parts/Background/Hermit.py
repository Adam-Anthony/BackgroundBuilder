## Hermit
import random as rng
import Parts.TableHelper as TableHelper
import Parts.Personality as Personality
newLine = '\n'
blankSpace = ' '
indentSpace = '    '

def GetResults():
    result = 'Your background is a hermit.' + newLine
    result += Decision()
    result += Trait()
    result += Ideal()
    result += Bond()
    result += Flaw()
    result += LifeSeclusion()
    return result

def Trait():
    emb = []
    emb += ['I\'ve been isolated for so long that I rarely speak, preferring gestures and the occasional grunt.']
    emb += ['I am utterly serene, even in the face of disaster.']
    emb += ['The leader of my community had something wise to say on every topic, and I am eager to share that wisdom.']
    emb += ['I feel tremendous empathy for all who suffer.']
    emb += ['I\'m oblivious to etiquette and social expectations.']
    emb += ['I connect everything that happens to me to a grand, cosmic plan.']
    emb += ['I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings.']
    emb += ['I am working on a grand philosophical theory and love sharing my ideas.']
    return Personality.Traits(emb)

def Ideal():
    emb = []
    align = []
    emb += ['Greater Good. My gifts are meant to be shared with all, not used for my own benefit.']
    emb += ['Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking.']
    emb += ['Free Thinking. Inquiry and curiosity are the pillars of progress.']
    emb += ['Power. Solitude and contemplation are paths toward mystical or magical power.']
    emb += ['Live and Let Live. Meddling in the affairs of others only causes trouble.']
    emb += ['Self-Knowledge. If you know yourself, there\'s nothing left to know.']
    #
    align += ['(Good)']
    align += ['(Lawful)']
    align += ['(Chaotic)']
    align += ['(Evil)']
    align += ['(Neutral)']
    align += ['(Any)']
    return Personality.Ideals(emb, align)

def Bond():
    emb = []
    emb += ['Nothing is more important than the other members of my hermitage, order, or association.']
    emb += ['I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.']
    emb += ['I\'m still seeking the enlightenment I pursued in my seclusion, and it still eludes me.']
    emb += ['I entered seclusion because I loved someone I could not have.']
    emb += ['Should my discovery come to light, it could bring ruin to the world.']
    emb += ['My isolation gave me great insight into a great evil that only I can destroy.']
    return Personality.Bonds(emb)

def Flaw():
    emb = []
    emb += ['Now that I\'ve returned to the world, I enjoy its delights a little too much.']
    emb += ['I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell.']
    emb += ['I am dogmatic in my thoughts and philosophy.']
    emb += ['I let my need to win arguments overshadow friendships and harmony.']
    emb += ['I\'d risk too much to uncover a lost bit of knowledge.']
    emb += ['I like keeping secrets and won\'t share them with anyone.']
    return Personality.Flaws(emb)

def LifeSeclusion():
    roll = rng.randint(1,8)
    emb = []
    emb += ['I was searching for spiritual enlightenment.']
    emb += ['I was partaking of communal living in accordance with the dictates of a religious oder.']
    emb += ['I was exiled for a crime I didn\'t commit.']
    emb += ['I retreated from socity after a life-altering event.']
    emb += ['I needed a quiet place to work on my art, literature, music, or manifesto.']
    emb += ['I needed to commune with nature, far from civilization.']
    emb += ['I was the caretaker of an ancient ruin or relic.']
    emb += ['I was a pilgrim in search of a person, place, or relic of spiritual significance.']
    return ('Life of Seclusion:' + newLine + indentSpace + TableHelper.dEightTable(emb,roll) + newLine)

def Decision():
    roll = rng.randint(1,6)
    emb = []
    emb += ['my enemies ruined my reputation, and I fled to the wilds to avoid further disparagement.']
    emb += ['I am comfortable with being isolated, as I seek inner peace.']
    emb += ['I never liked the people I called my friends, so it was easy for me to strike out on my own.']
    emb += ['I felt compelled to forsake my past, but did so with great reluctance, and sometimes I regret making that decision.']
    emb += ['I lost everything--my home, my family, my friends. Going it alone was all I could do.']
    emb += ['Society\'s decadence disgusted me, so I decided to leave it behind.']
    return ('I became a hermit because ' + TableHelper.dSixTable(emb, roll) + newLine)