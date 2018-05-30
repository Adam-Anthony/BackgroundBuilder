## Preamble finished
import random as rng
import Parts.TableHelper as TableHelper
lineBreak = '\n'
blankSpace = ' '
def BardTables(rolls):
    result = 'You are a bard.' + lineBreak
    
    trainRoll = rng.randint(1,6)
    result += (ClassTraining(trainRoll) + lineBreak)
    
    result += 'Your defining work, spoken about for years. Perhaps a work in progress, or a staple of your performance. ' 
    result += (DefiningWork(rolls[0]) + lineBreak)
    
    result += 'Any bard knows an instrument\'s entertainment value is as important as the music it plays. It might not be your only instrument, but it\'s a star. '
    result += (Instrument(rolls[1]) + lineBreak)
    
    result += 'Almost every bard has suffered at least one bad experience in front of an audience. '
    result += (Embarrassments(rolls[2]) + lineBreak)
    
    return result

def DefiningWork(roll):
    emb = []
    emb += ['\"The Three Flambinis\", a ribald song concerning mistaken identities and unfettered desire.']
    emb += ['\"Waltz of the Myconids\", an upbeat tune that children in particular enjoy.']
    emb += ['\"Asmodeus\' Golden Arse\", a dramatic poem you claim was inspired by your personal visit to Avernus.']
    emb += ['\"The Pirates of Luskan\", your firsthand account of being kidnapped by sea reavers as a child.']
    emb += ['\"A Hoop, Two Pigeons, and a Hell Hound\", a subtle parody of an incompetent noble.']
    emb += ['\"A Fool in the Abyss\", a comedic poem about a jester\'s travels among demons.']
    return TableHelper.dSixTable(emb, roll)

def Instrument(roll):
    emb = []
    emb += ['A masterfully crafted halfling fiddle.']
    emb += ['A mithral horn made by elves.']
    emb += ['A zither made with drow spider silk.']
    emb += ['An orcish drum.']
    emb += ['A wooden bullywug croak box.']
    emb += ['A tinker\'s harp of gnomish design.']
    return TableHelper.dSixTable(emb, roll)

def Embarrassments(roll):
    emb = []
    emb += ['The time when your comedic song, \"Big Tom\'s Hijinks\"--which, by the way, you thought was brilliant--did not go over well with Big Tom']
    emb += ['The mantinee performance when a circus\'s owlbear got loose and terrorized the crowd.']
    emb += ['When your opening song was your enthusiastic but universally hated rendition of \"Song of the Froghemoth\"']
    emb += ['The first and last performance of \"Mirt, Man about Town\".']
    emb += ['The time on stage when your wig caught fire and you threw it down--which set fire to the stage.']
    emb += ['When you sat on your lute by mistake during the final stanza of \"Starlight Serenade\".']
    return TableHelper.dSixTable(emb, roll)

def ClassTraining(roll):
    emb = []
    emb += ['you awakened your latent bardic abilities through trial and error.']
    emb += ['you were a gifted performer and attracted the attention of a master bard who schooled you in the old techniques.']
    emb += ['you joined a loose society of scholars and orators to learn new techniques of performance and magic.']
    emb += ['you felt a calling to recount the deeds of champions and heroes, to bring them alive in song and story.']
    emb += ['you joined one of the great colleges to learn old lore, the secrets of magic, and the art of performance.']
    emb += ['you picked up a musical instrument one day and instantly discovered that you could play it.']
    result = 'You became a bard because ' + TableHelper.dSixTable(emb, roll) + lineBreak
    return result