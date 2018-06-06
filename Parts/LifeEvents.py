import random as rng
import Parts.Supplementals as sup
import Parts.ArrayDisassemble as ad

indentSpace = '    '
lineBreak = '\n'
blankSpace = ' '
def EventsByAge(age):
    events = 0
    if age <= 20:
        events = 1
    elif age >= 21 and age <= 30:
        events = rng.randint(1,4)
    elif age >= 31 and age <= 40:
        events = rng.randint(1,6)
    elif age >= 41 and age <= 50:
        events = rng.randint(1,8)
    elif age >= 51 and age <= 60:
        events = rng.randint(1,10)
    elif age >= 61:
        events = rng.randint(1,12)
    return RunningEvents(events)

def AgeRange():
    roll = rng.randint(1,100)
    age = 0
    result = 'Age:' + blankSpace
    if roll <= 20:
        result += '20 years or younger.'
        age = 20
    elif roll >= 21 and roll <= 59:
        result += '21 - 30 years.'
        age = 25
    elif roll >= 60 and roll <= 69:
        result += '31 - 40 years.'
        age = 35
    elif roll >= 70 and roll <= 89:
        result += '41 - 50 years.'
        age = 45
    elif roll >= 90 and roll <= 99:
        result += '51 - 60 years.'
        age = 55
    elif roll == 100:
        result += '61 years or older.'
        age = 65

    result += lineBreak
    result += EventsByAge(age)
    return result

def RunningEvents(events):
    luvVal = False
    result = ''
    for i in range(0,events):
        z = EventsTable(luvVal)
        result += z[0] + lineBreak
        luvVal = z[1]
    return result

def EventsTable(luvVal):
    roll = rng.randint(1,100)
    result = ''
    luv = luvVal
    ## Tragedy only strikes
    if roll <= 10:
        result = 'You suffered a tragedy.' + lineBreak
        ## Roll on the Tragedy table
        result += indentSpace + Tragedies()
    ## The Dice Gods Smiled
    elif roll >= 11 and roll <= 20:
        result = 'You gained a bit of good fortune.' + lineBreak
        ## Roll on the Boons table
        result += indentSpace + Boons()
    ## Love and Marriage
    elif roll >= 21 and roll <= 30:
        if luv == False:
            result = 'You fell in love or got married.'
            luv = True
        else:
            result = 'You fell in love or got married again. You can choose to to have a child instead.'
    ## Adventurer as Foe
    elif roll >= 31 and roll <= 40:
        result = 'You made an enemy of an adventurer,' + blankSpace
        result += sup.CharClass() + lineBreak
        subroll = rng.randint(1,6)
        result += indentSpace
        if (subroll % 2 == 1):
            result += 'You are to blame for rift.'
        else:
            result += 'They are to blame for the rift'
    ## Adventurer as Friend
    elif roll >= 41 and roll <= 50:
        result = 'You made a friend of an adventurer, '
        result += sup.CharClass()
    ## Working a job 
    elif roll >= 51 and roll <= 70:
        result = 'You spent time working in a job related to your background.' + lineBreak
        subroll = rng.randint(1,6) + rng.randint(1,6)
        result += indentSpace
        result += 'You start with an extra ' + str(subroll) + 'gp.'
    ## Met someone important
    elif roll >= 71 and roll <= 75:
        result = 'You met someone important.'
        ## Flesh out a character
    ## Onto an adventure
    elif roll >= 76 and roll <= 80:
        result = 'You went on an adventure.' + lineBreak
        ## Roll on the Adventure table
        result += Adventures()
    ## Supernatural Experience
    elif roll >= 81 and roll <= 85:
        result = 'You had a supernatural experience.' + lineBreak
        ## Roll on the Supernatural table
        result += Supernatural()
    ## Fought in battle
    elif roll >= 86 and roll <= 90:
        result = 'You fought in a battle.' + lineBreak
        ## Roll on the War table
        result += War()
    ## Crime Accussal
    elif roll >= 91 and roll <= 95:
        result = 'You commited a crime or were wrongly accused of doing so.' + lineBreak
        ## Roll on the Crime Table
        result += Crime() + lineBreak
        ## Roll on the Punishment Table
        result += Punishment()
    ## Encounted something magical
    elif roll >= 96 and roll <= 99:
        result = 'You encountered something magical.' + lineBreak
        ## Roll on the Arcane Matters
        result += ArcaneMatters()
    ## Something truly strange
    elif roll == 100:
        result = 'Something truly strange happened to you.' + lineBreak
        ## Roll on the Weird Stuff table
        result += WeirdStuff()
    q = [result, luv]
    return q

## Secondary Tables
def Adventures():
    roll = rng.randint(1,100)
    result = indentSpace
    if roll <= 10:
        sub1 = rng.randint(1,3)
        sub2 = rng.randint(1,4)
        result += 'You nearly died. You have nasty scars on your body, and you are missing an ear, '
        result += (str(sub1) + ' fingers, or ' + str(sub2) + ' toes.')
    elif roll >= 11 and roll <= 20:
        result += 'You suffered a grievous injury. Although the wound healed, it still pains you from time to time.'
    elif roll >= 21 and roll <= 30:
        result += 'You were wounded, but in time you fully recovered.'
    elif roll >= 31 and roll <= 40:
        result += 'You contracted a disease while exploring a filthy warren.'
        result += 'You recovered from the disease, but you have a persistent cough, pockmarks on your skin, or prematurely gray hair.'
    elif roll >= 41 and roll <= 50:
        result += 'You were poisoned by a trap or monster. You recovered, but the next time you must make '
        result += 'a saving throw against poison, you make the saving throw with disadvantage.'
    elif roll >= 51 and roll <= 60:
        result += 'You lost something of sentimental value to you during your adventure. Remove one trinket from your possessions.'
    elif roll >= 61 and roll <= 70:
        result += 'You were terribly frightened by something you encountered and ran away, abandoning your companions to their fate.'
    elif roll >= 71 and roll <= 80:
        result += 'You learned a great deal during your adventure. The next time you make an ability check or saving throw, you have advantage on the roll.'
    elif roll >= 81 and roll <= 90:
        subroll = rng.randint(1,6) + rng.randint(1,6)
        result += 'You found some treasure on your adventure. You have ' + str(subroll) + 'gp left from your share of it.'
    elif roll >= 91 and roll <= 99:
        subroll = rng.randint(1,20) + 50
        result += 'You found a considerable amount of treasure on your adventure.'
        result += 'You have ' + str(subroll) + 'gp left from your share of it.'
    elif roll == 100:
        result += 'You came across a common magic item (of the DM\'s choice).'

    return result

def ArcaneMatters():
    roll = rng.randint(1,10)
    result = indentSpace
    if roll == 1:
        result += 'You were charmed or frightened by a spell.'
    elif roll == 2:
        result += 'You were injured by the effect of a spell.'
    elif roll == 3:
        result += 'You witnessed a powerful spell being cast by a cleric, a druid, a sorcerer, a warlock, or a wizard.'
    elif roll == 4:
        result += 'You drank a potion (of the DM\'s choice).'
    elif roll == 5:
        result += 'You found a spell scroll and succeeded in casting the spell in contained.'
    elif roll == 6:
        result += 'You were affected by teleportation magic.'
    elif roll == 7:
        result += 'You turned invisible for a time.'
    elif roll == 8:
        result += 'You identified an illusion for what it was.'
    elif roll == 9:
        result += 'You saw a creature being conjured by magic.'
    elif roll == 10:
        result += 'Your fortune was read by a diviner. DM picks one of these two as a divined future event.\n'
        result += '[=============================================================================]\n'
        result += EventsTable(luv) + lineBreak
        result += '------------------------------------------------------------------------------\n'
        result += EventsTable(luv) + lineBreak
        result += '[============================================================================]\n'
        ## Roll twice on the life events table, DM picks one as a divined future event.

    return result

def Boons():
    roll = rng.randint(1,10)
    result = indentSpace
    if roll == 1:
        result += 'A friendly wizard gave you a spell scroll containing one cantrip (of the DM\'s choice).'
    elif roll == 2:
        result += 'You saved the life of a commoner, who now owes you a life debt. This individual accompanies you on your travels and performs mundane tasks for you, '
        result += 'but will leave if neglected, abused or imperiled.'
        ## Roll on supplemental tables to flesh out character.
    elif roll == 3:
        result += 'You found a riding horse.'
    elif roll == 4:
        subroll = rng.randint(1,20)
        result += 'You found some money. You have ' + str(subroll) + 'gp in addition to your regular starting funds.'
    elif roll == 5:
        result += 'A relative bequeathed you a simple weapon of your choice.'
    elif roll == 6:
        result += 'You found something interesting. You gain one additional trinket.'
    elif roll == 7:
        result += 'You once performed a service for a local temple. The next time you visit the temple, you can recieve healing up to your hit point maximum.'
    elif roll == 8:
        result += 'A friendly alchemist gifted you with a potion of healing or a flask of acid, as you choose.'
    elif roll == 9:
        result += 'You found a treasure map.'
    elif roll == 10:
        subroll = rng.randint(1,20)
        result += 'A distant relative left you a stipend that enables you to live at the comfortable lifestyle for ' + str(subroll) + ' years. '
        result += 'If you choose to live at a higher lifestyle, you reduce the price of the lifestyle by 2 gp during the time period.'
    return result

def Crime():
    roll = rng.randint(1,8)
    result = indentSpace
    if roll == 1:
        result += 'Murder.'
    elif roll == 2:
        result += 'Theft'
    elif roll == 3:
        result += 'Burglary'
    elif roll == 4:
        result += 'Assault'
    elif roll == 5:
        result += 'Smuggling'
    elif roll == 6:
        result += 'Kidnapping'
    elif roll == 7:
        result += 'Extortion'
    elif roll == 8:
        result += 'Counterfeiting'
    return result

def Punishment():
    roll = rng.randint(1,12)
    result = indentSpace
    if roll >= 1 and roll <= 3:
        result += 'You did not commit the crime and were exonerated after being accused.'
    elif roll >= 4 and roll <= 6:
        result += 'You commited the crime or helped do so, but nonetheless the authorities found you not guilty.'
    elif roll >= 7 and roll <= 8:
        result += 'You were nearly caught in the act. You had to flee and are wanted in the community where the crime occurred.'
    elif roll >= 9 and roll <= 12:
        subroll = rng.randint(1,4)
        result += 'You were caught and convicted. You spent time in jail, chained to an oar, or performing hard labor.'
        result += 'You served a sentence of ' + str(subroll) + ' years or succeeded in escaping after that much time.'
    return result

def Supernatural():
    roll = rng.randint(1,100)
    result = indentSpace
    if roll >= 1 and roll <= 5:
        subroll = rng.randint(1,6)
        result += 'You were ensorcelled by a fey and enslaved for ' + str(subroll) + ' years before you escaped.'
    elif roll >= 6 and roll <= 10:
        result += 'You saw a demon and ran away before it could do anything to you.'
    elif roll >= 11 and roll <= 15:
        subroll = rng.randint(1,20) + 50
        result += 'A devil tempted you. Make a DC 10 Wisdom Saving throw. On a failed save, your alignment shifts one step toward evil (if it\'s not evil already), '
        result += 'and you start the game with an additional ' + str(subroll) + 'gp.'
    elif roll >= 16 and roll <= 20:
        result += 'You woke up one morning miles from your home, with no idea how you got there.'
    elif roll >= 21 and roll <= 30:
        result += 'You visited a holy site and felt the presence of the divine there.'
    elif roll >= 31 and roll <= 40:
        result += 'You witnessed a falling red star, a face appearing in the frost, or some other bizarre happening. '
        result += 'You are certain that it was an omen of some sort.'
    elif roll >= 41 and roll <= 50:
        result += 'You escaped certain death and believe it was the intervention of a god that saved you.'
    elif roll >= 51 and roll <= 60:
        result += 'You witnessed a minor miracle.'
    elif roll >= 61 and roll <= 70:
        result += 'You explored an empty house and found it to be haunted.'
    elif roll >= 71 and roll <= 75:
        result += 'You were briefly possessed by a '
        subroll = rng.randint(1,6)
        if subroll == 1:
            result += 'celestial.'
        elif subroll == 2:
            result += 'devil.'
        elif subroll == 3:
            result += 'demon.'
        elif subroll == 4:
            result += 'fey.'
        elif subroll == 5:
            result += 'elemental.'
        elif subroll == 6:
            result += 'undead.'
    elif roll >= 76 and roll <= 80:
        result += 'You saw a ghost.'
    elif roll >= 81 and roll <= 85:
        result += 'You saw a ghoul feeding on a corpse.'
    elif roll >= 86 and roll <= 90:
        result += 'A celestial or a fiend visited you in your dreams to give a warning of dangers to come.'
    elif roll >= 91 and roll <= 95:
        result += 'You briefly visited the Feywild or the Shadowfell.'
    elif roll >= 96:
        result += 'You saw a portal that you believe leads to another plane of existence.'
    return result

def Tragedies():
    roll = rng.randint(1,12)
    result = indentSpace
    if roll == 1 or roll == 2:
        result += 'A family member or a close friend died.'
        ## Roll on the Cause of Death table
        result += sup.CauseOfDeath()
    elif roll == 3:
        result += 'A friendship ended bitterly, and the other person is now hostile to you. The cause might have been a misunderstanding or something you or the former friend did.'
    elif roll == 4:
        result += 'You lost all your possessions in a disaster, and you had to rebuild your life.'
    elif roll == 5:
        subroll = rng.randint(1,6)
        result += 'You were imprisoned for a crime you didn\'t commit and spent ' + str(subroll)
        result += ' years at hard labor, in jail, or shackled to an oar in a slave gallery.'
    elif roll == 6:
        result += 'War ravaged your home community, reducing everything to rubble and ruin. In the aftermath, you either helped your town rebuild moved somewhere else.'
    elif roll == 7:
        result += 'A lover disappeared without a trace. You have been looking for that person ever since.'
    elif roll == 8:
        result += 'A terrible blight in your home community caused crops to fail, and many starved. You lost a sibling or some other family member.'
    elif roll == 9:
        result += 'You did something that brought terrible shame to you in the eyes of your family. You might have been involved in a scandal, dabbled in dark magic, or offended someone important.'
        result += 'The attitude of your family members toward you becomes indifferent at best, though they might eventually forgive you.'
    elif roll == 10:
        result += 'For a reason you were never told, you were exiled from your community. You then either wandered in the wilderness for a time or promptly found a new place to live.'
    elif roll == 11:
        result += 'A romantic relationship ended.' + blankSpace
        if (rng.randint(1,2)==1):
            result += 'It ended with bad feelings.'
        else:
            result += 'It ended amicably.'
    elif roll == 12:
        result += 'A current or prospective romantic partner of yours died.'
        result += blankSpace
        ## Roll Cause of death.
        res = sup.CauseOfDeath()
        result += res
        ## If result is murder, roll a d12 and on a 1, you were responsible.
        if res == 'Murdered.':
            subroll = rng.randint(1,12)
            if subroll == 1:
                result += lineBreak + indentSpace
                result += 'You were responsible'
    return result

def War():
    roll = rng.randint(1,12)
    result = indentSpace
    if roll == 1:
        result += 'You were knocked out and left for dead. You woke up hours later with no recollection of the battle.'
    elif roll == 2 or roll == 3:
        result += 'You were badly injured in the fight, and you still bear the awful scars of those wounds.'
    elif roll == 4:
        result += 'You ran away from the battle to save your life, but you still feel shame for your cowardice.'
    elif roll >= 5 and roll <= 7:
        result += 'You suffered only minor injuries, and the wounds all healed without leaving scars.'
    elif roll == 8 or roll == 9:
        result += 'You survived the battle, but you suffer from terrible nightmares in which you relive the experience.'
    elif roll == 10 or roll == 11:
        result += 'You escaped the battle unscathed, though many of your friends were injured or lost.'
    elif roll == 12:
        result += 'You acquitted yourself well in battle and are remembered as a hero. You might have received a medal for your bravery.'
    #
    return result

def WeirdStuff():
    roll = rng.randint(1,12)
    result = indentSpace
    if roll == 1:
        subroll = rng.randint(1,4)
        result += 'You were turned into a toad and remained in that form for ' + str(subroll) + ' weeks.'
    elif roll == 2:
        result += 'You were petrified and remained a stone statue for a time until someone freed you.'
    elif roll == 3:
        subroll = rng.randint(1,6)
        result += 'You were enslaved by a hag, a satyr, or some other being and lived in that creature\'s thrall for ' +str(subroll)+ ' years.'
    elif roll == 4:
        subroll = rng.randint(1,4)
        result += 'A dragon held you as a prisoner for ' + str(subroll) + ' months until adventurers killed it.'
    elif roll == 5:
        result += 'You were taken captive by a race of evil humanoids such as drow, kuo-toa, or quaggoths. You lived as a slave in the Underdark until you escaped.'
    elif roll == 6:
        result += 'You served a powerful adventurer as a hireling. You have only recently left that service.'
        ## Roll on Supplemental tables for the adventurer
    elif roll == 7:
        subroll = rng.randint(1,6)
        result += 'You went insane for ' +str(subroll)+ ' years and recently regained your sanity. A tic or some other bit of odd behavior might linger.'
    elif roll == 8:
        result += 'A lover of yours was secretly a silver dragon.'
    elif roll == 9:
        result += 'You were captured by a cult and nearly sacrificed on an altar to the foul being the cultists served. You escaped, but you fear they will find you.'
    elif roll == 10:
        result += 'You met a demigod, an archdevil, an archfey, a demon lord, or a titan, and you lived to tell the tale.'
    elif roll == 11:
        result += 'You were swallowed by a giant fish and spent a month in its gullet before you escaped.'
    elif roll == 12:
        result += 'A powerful being granted you a wish, but you squandered it on something frivolous.'
    return result