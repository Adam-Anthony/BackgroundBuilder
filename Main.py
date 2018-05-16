import LifeEvents
import Supplementals
import Origins

class CharBuild():
    """docstring for main"""
    def __init__(self):
        super(CharBuild, self).__init__()
        
    def Build(self):
        ## Roll Race
        ## Roll Class
        self.RunBuilder('human', 'monk')

    def BuildGiven(self, race, clas):
        self.RunBuilder(race, clas)

    def RunBuilder(self, race, clas):
        ## Race Choose

        ## Class Choose

        ## Origins
        parent = Origins.Parents('human')
        parent.KnownParents()
        Origins.Birthplace()
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
