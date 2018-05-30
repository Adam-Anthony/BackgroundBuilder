import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Parts.LifeEvents as LifeEvents
import Parts.Supplementals as Supplementals
import Parts.Origins as Origins
import Parts.CharClass as CharClass

linebreak = '\n'
blankSpace = ' '

class CharBuild():
    """docstring for main"""
    def __init__(self):
        super(CharBuild, self).__init__()
    
    def Build(self):
        ## Roll Race
        ## Roll Class
        self.RunBuilder('human', 'Cleric')

    def BuildGiven(self, race, clas):
        self.RunBuilder(race, clas)

    def RunBuilder(self, race, clas):
        ## Race Choose
        #
        ## Class Choose
        CharClass.CheckClass(clas)
        ## Origins
        parent = Origins.Parents(race)
        parent.KnownParents()
        Origins.Birthplace()
        print(blankSpace)
        ## Life Events
        ## Generates an age range, doesn't take in an age
        LifeEvents.AgeRange()

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
