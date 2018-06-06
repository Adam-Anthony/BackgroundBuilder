import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Parts.LifeEvents as LifeEvents
import Parts.Supplementals as Supplementals
import Parts.Origins as Origins
import Parts.Race as Race
import Parts.CharClass as CharClass
import Parts.Backgrounds as Backgrounds
import ctypes

lineBreak = '\n'
blankSpace = ' '
fileLocation = 'Characters/'
fileName = 'character'
fileType = '.txt'
class CharBuild():
    """docstring for main"""
    def __init__(self):
        super(CharBuild, self).__init__()
    #
    def Build(self):
        ## Roll Race
        race = Race.RandomRaceWeighted()
        ## Roll Class
        clas = CharClass.RollClassNotWeighted()
        print(clas)
        ## Roll Background
        back = Backgrounds.ChooseRandom()
        self.RunBuilder(race, clas, back)
    # Race Class 
    def BuildRC(self, race, clas):
        back = Backgrounds.ChooseRandom()
        self.RunBuilder(race, clas, back)
    # Race Class Background
    def BuildRCB(self, race, clas, back):
        self.RunBuilder(race, clas, back)
    #      Class Background
    def BuildCB(self, clas, back):
        race = Race.RandomRaceWeighted()
        self.RunBuilder(race, clas, back)
    #
    def RunBuilder(self, race, clas, back):
        # Need to intilizae a way to get a cha mod from user.
        chaMod = 0
        #
        result = ''
        #    
        ## Race Weight and Height
        #
        ## Background Choose
        result += Backgrounds.RunBackgrounds(back)
        result += lineBreak
        #
        ## Class Choose
        result += CharClass.CheckClass(clas)
        result += lineBreak
        ## Origins
        parent = Origins.Parents(race)
        result += parent.KnownParents()
        #
        result += Origins.Birthplace()
        result += Origins.NumberOfSiblings(race)
        #
        family = Origins.FamilyLife(chaMod)
        result += family.getResults()
        result += lineBreak
        ## Life Events
        ## Generates an age range, doesn't take in an age
        result += LifeEvents.AgeRange()
        print(result)
        popResult = result + lineBreak + lineBreak + 'Would you like to save this character?'
        ##
        ## We can probably make that question look better.
        buttonRes = ctypes.windll.user32.MessageBoxW(0,popResult,'Your Character, the ' + race + ' ' + clas, 4)
        if buttonRes == 6:
            newPath = fileLocation + fileName + fileType
            if os.path.exists(newPath):
                count = 1
                breaker = True
                while breaker:
                    if count/10 < 1:
                        num = '0' + str(count)
                    else:
                        num = str(count)
                    newPath = fileLocation + fileName + num + fileType
                    if os.path.exists(newPath):
                        count += 1
                    else:
                        breaker = False
            #
            saved = open(newPath, 'w')
            saved.write(result)
            saved.close()
        ## More

def MultipleRuns(num):
    charBuild = CharBuild()
    for i in range (0, num):
        charBuild.Build()
        print('------------------------------------------------------')

def MultipleRunsGiven(race, clas, num):
    charBuild = CharBuild()
    for i in range (0, num):
        charBuild.BuildGiven(race, clas)
