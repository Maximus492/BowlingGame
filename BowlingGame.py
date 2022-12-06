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
        lengthOfRolls = len(self.rolls)             # this takes the length of the array created
        upperLimitOfArray = lengthOfRolls - 1       # this takes the length of the array and minus one.  This is for the while loop, so we don't get a out of bound index problem.
        while rollIndex <= upperLimitOfArray:       # while loop created.  Old loop removed.  'While' loops may not be the best but it is functional.
            result += self.frameScore(rollIndex)    # this counts the score at that particular frame.
            rollIndex +=1                           # this moves the rollIndex to the next index in the rolls array.
        return result
    
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    def stickeScore(self,rollIndex):
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
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
    game.roll(10)
    game.roll(10) 
    game.roll(10)
    game.roll(5)   
    game.roll(4)
    game.roll(3)   
    game.roll(1)
    game.roll(5)   # should add up to 48
    print(game.rolls)
    results = game.score()
    print(results)

BowlStrike()            # this works 