import random as rng
import TableHelper
lineBreak = '\n'
blankSpace = ' '
def BardTables(rolls):
    result = 'You are a bard.' + lineBreak

    result += 'Your defining work, spoken about for years. Perhaps a work in progress, or a staple of your performance. ' 
    result += (DefiningWork(roll[0]) + lineBreak)

    result += 'Any bard knows an instrument\'s entertainment value is as important as the music it plays. It might not be your only instrument, but it\'s a star. '
    result += (Instrument(roll[1]) + lineBreak)

    result += 'Almost every bard has suffered at least one bad experience in front of an audience. '
    result += (Embarrassments(roll[2]) + lineBreak)

    return result

def DefiningWork(roll):
    if roll == 1:
        result = '\"The Three Flambinis\", a ribald song concerning mistaken identities and unfettered desire.'
    elif roll == 2:
        result = '\"Waltz of the Myconids\", an upbeat tune that children in particular enjoy.'
    elif roll == 3:
        result = '\"Asmodeus\' Golden Arse\", a dramatic poem you claim was inspired by your personal visit to Avernus.'
    elif roll == 4:
        result = '\"The Pirates of Luskan\", your firsthand account of being kidnapped by sea reavers as a child.'
    elif roll == 5:
        result = '\"A Hoop, Two Pigeons, and a Hell Hound\", a subtle parody of an incompetent noble.'
    elif rolls == 6:
        result = '\"A Fool in the Abyss\", a comedic poem about a jester\'s travels among demons.'

    return result

def Instrument(roll):
    if roll == 1:
        result = 'A masterfully crafted halfling fiddle.'
    elif roll == 2:
        result = 'A mithral horn made by elves.'
    elif roll == 3:
        result = 'A zither made with drow spider silk.'
    elif roll == 4:
        result = 'An orcish drum.'
    elif roll == 5:
        result = 'A wooden bullywug croak box.'
    elif roll == 6:
        result = 'A tinker\'s harp of gnomish design.'

    return result

def Embarrassments(roll):
    emb = []
    emb += ['The time when your comedic song, \"Big Tom\'s Hijinks\"--which, by the way, you thought was brilliant--did not go over well with Big Tom']
    emb += ['The mantinee performance when a circus\'s owlbear got loose and terrorized the crowd.']
    emb += ['When your opening song was your enthusiastic but universally hated rendition of \"Song of the Froghemoth\"']
    emb += ['The first and last performance of \"Mirt, Man about Town\".']
    emb += ['The time on stage when your wig caught fire and you threw it down--which set fire to the stage.']
    emb += ['When you sat on your lute by mistake during the final stanza of \"Starlight Serenade\".']
    return TableHelper.dSixTable(emb, roll)