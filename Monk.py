## Preamble not finished
import random as rng
import TableHelper
lineBreak = '\n'
blankSpace = ' '

def MonkTables(rolls):
    result = 'You are a monk.' + lineBreak

    trainRoll = rng.randint(1,6)
    result += (ClassTraining(trainRoll) + lineBreak)

    result += ('Monasteries:' + blankSpace)
    result += (Monasteries(rolls[0]) + lineBreak)

    result += ('Monastic Icons:' + blankSpace)
    result += (MonasticIcons(rolls[1]) + lineBreak)

    result += ('Master:' + blankSpace)
    result += (Masters(rolls[2]) + lineBreak)
    return result

def Monasteries(roll):
    emb = []
    emb += ['Your monastery is carved out of a mountainside, where it looms over a treacherous pass.']
    emb += ['Your monastery is high in the branches of an immense tree in the Feywild.']
    emb += ['Your monastery was founded long ago by a cloud giant and is inside a cloud castle that can be reached only by flying.']
    emb += ['Your monastery is built beside a volcanic system of hot springs, geysers, and sulfur pools. You regularly received visits from azer traders.']
    emb += ['Your monastery was founded by gnomes and is an underground labyrinth of tunnels and rooms.']
    emb += ['Your monastery was carved from an iceberg in the frozen reaches of the world.']

    return TableHelper.dSixTable(emb, roll)

def MonasticIcons(roll):
    emb = []
    emb += ['Monkey. Quick reflexes and the ability to travel through the treetops are two of the reasons why your order admires the monkey.']
    emb += ['Dragon Turtle. The monks of your seaside monastery venerate the dragon turtle, reciting ancient prayers and offering garlands of flowers to honor this living spirit of the sea.']
    emb += ['Ki-rin. Your monastery sees its main purpose as watching over and protecting the land in the manner of the ki-rin.']
    emb += ['Owlbear.. The monks of your monastery revere a family of owlbears and have coexisted with them for generations.']
    emb += ['Hydra. Your order singles out the hydra for its ability to unleash several attacks simultaneously.']
    emb += ['Dragon. A dragon once laired within your monastery. Its influence remains long after its departure.']
    return TableHelper.dSixTable(emb, roll)

def Masters(roll):
    emb = []
    emb += ['Your master was a tyrant whom you had to defeat in single combat to complete your instruction.']
    emb += ['Your master was kindly and taught you to pursue the cause of peace']
    emb += ['Your master was merciless in pushing you to your limits. You nearly lost an eye during one especially brutal practice session.']
    emb += ['Your master seemed goodhearted while tutoring you, but betrayed your monastery in the end.']
    emb += ['Your master was cold and distant. You suspect that the two of you might be related.']
    emb += ['Your master was kind and generous, never critical of your progress. Nevertheless, you feel you never fully lived up to the expectations placed on you.']
    
    return TableHelper.dSixTable(emb, roll)

def ClassTraining(roll):
    emb = []
    emb += ['you were chosen to study at a secluded monastery. There, you were taught the fundamental techniques required to eventually master a tradition.']
    emb += ['you sought instruction to gain a deeper understanding of existence and your place in the world.']
    emb += ['you stumbled into a portal to the Shadowfell and took refuge in a strange monastery, where you learned how to defend yourself against the forces of darkness.']
    emb += ['you were overwhelmed with grief after losing someone close to you, and you sought the advice of philosophers to help your cope with your loss.']
    emb += ['you could feel that a special sort of power lay within you, so you sought out those who could help you call it forth and master it.']
    emb += ['you were wild and undisciplined as a youngster, but then you realized the error of your ways. You applied to a monastery and became a monk as a way to live a life of discipline.']
    result = 'You became a monk because ' + TableHelper.dSixTable(emb, roll) + lineBreak
    return result