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
        self.rolls.append(0)
        self.rolls.append(0)  # this line and the line above creates a buffer in the rolls list so it does not create a out of index problem.     
        lengthOfRolls = len(self.rolls)
        upperLimitOfArray = lengthOfRolls - 1
        print(self.rolls)
        while rollIndex <= upperLimitOfArray:
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex +=1
                print("Strike" +str(result))
                print("Strike RollIndex" +str(rollIndex))
            elif self.isSpare(rollIndex,upperLimitOfArray):
                result += self.spareScore(rollIndex)
                rollIndex +=2 # the rollIndex jumps 2 this time because we have already counted the two together because they are a spare.
                print("spare" +str(result))
                print("spare RollIndex" +str(rollIndex))
            else: 
                result += self.frameScore(rollIndex)
                rollIndex +=1
                print("pin" +str(result))
                print("pin RollIndex" +str(rollIndex))
        self.rolls.pop()
        self.rolls.pop() # this line and the line above removes the buffer 
        print(self.rolls)
        return result
    
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex,upperLimitOfArray): 
        if rollIndex == upperLimitOfArray: 
            print("Hopefully working isSpare RollIndex" +str(rollIndex)) 
            return 0            
        else:
            return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10  # this line counts the 2 pins together to determine if its a spare

    def strikeScore(self,rollIndex):          
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):             
        return  10+ self.rolls[rollIndex+2]     # changed the +2 to +1

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

    game.roll(1)                   # 75
  
    game.roll(5)                   # 83
    
    game.roll(5)                   # 86

    game.roll(1)                   # 87

    game.roll(5)                   # 92
    
    game.roll(5)                   # 

    game.roll(10)                  # 

    game.roll(5)    

    game.roll(5)              
    '''  '''       
    print(game.rolls)
    results = game.score()
    print(results)

BowlStrike()