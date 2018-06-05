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
        ## Roll Class
        self.RunBuilder('human', 'Cleric', 'noble')
    #
    def BuildRC(self, race, clas):
        self.RunBuilder(race, clas, 'noble')
    #
    def BuildRCB(self, race, clas, back):
        self.RunBuilder(race, clas, back)
    #
    def BuildCB(self, clas, back):
        self.RunBuilder('human', clas, back)
    #
    def RunBuilder(self, race, clas, back):
        result = ''
        ## Race Choose
        race = Race.RandomRaceWeighted()
        result += race
        result += lineBreak
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
        result += Origins.Birthplace()
        result += Origins.NumberOfSiblings(race)
        result += lineBreak
        ## Life Events
        ## Generates an age range, doesn't take in an age
        result += LifeEvents.AgeRange()
        result += lineBreak
        print(result)
        popResult = result + lineBreak + lineBreak + 'Would you like to save this character?'
        ##
        ## We can probably make that question look better.
        buttonRes = ctypes.windll.user32.MessageBoxW(0,popResult,'Your Character', 4)
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
