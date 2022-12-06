#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        self.rolls=[]
        # any array (might be a list) is created called rolls
    def roll(self,pins):
        self.rolls.append(pins)
        # this method adds to the roll array
    def score(self):
        result = 0
        rollIndex=0
        lengthOfRolls = len(self.rolls)
        upperLimitOfArray = lengthOfRolls - 1
        while rollIndex <= upperLimitOfArray:
            # for strikes below
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex,upperLimitOfArray)
                print("result" +str(result))
                rollIndex +=1
            # for counting pins below - similar to previous branch but put into else:
            else: 
                result += self.frameScore(rollIndex)
                rollIndex +=1
        return result
    
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10
    def isSpare(self, rollIndex):               # not used
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10

    def strikeScore(self,rollIndex,upperLimitOfArray):          # this code is to make sure that it does not go out of index error
        almostupperLimitOfArray =  upperLimitOfArray - 1
        if rollIndex == upperLimitOfArray:
            return 10
        elif rollIndex == almostupperLimitOfArray:
            return  10+ self.rolls[rollIndex+1]
        else:    
            return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):             # not used
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):            
        return self.rolls[rollIndex] # removing + self.rolls[rollIndex + 1] to this line.  We only need to count the score at the index, don't need to count the next score on the next index.
		

#Your tasks for code parts:
#1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
#2: Refactor the code (Improve its structure without changing external behaviour).
#3: Report everything using github commits and versioning control.


###### Important #####
# Please complete your project and all tasks according to assessment description provided in CANVAS.


# Below is homemade test code - doesn't count strikes or spares

def BowlStrike():
    print("**************************************")
    print("")
    game = BowlingGame()
    print("working so far")
    game.roll(10)                  # 10

    game.roll(10)                  # 30

    game.roll(10)                  # 60
    '''  
    game.roll(5)                   # 75
  
    game.roll(4)                   # 83
    
    game.roll(3)                   # 86

    game.roll(1)                   # 87

    game.roll(5)                   # 92
    '''   
    print(game.rolls)
    results = game.score()
    print(results)

BowlStrike()