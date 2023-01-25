#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        self.rolls=[]                           # any array (might be a list) is created called rolls
       
    def roll(self,pins):                        # this method adds to the roll array
        self.rolls.append(pins)
        
    def score(self):                            # this method score the game
        result = 0                              
        rollIndex=0
        frameCount=1                            # this counts the frame going into 
        lengthOfRolls = len(self.rolls)         # get length of self.rolls.list
        upperLimitOfList = lengthOfRolls - 1    # create the limit of the 'while' loop
        self.rolls.append(0)                    # IMPORTANT - THIS LINE AND THE LINE BELOW NEEDS TO BE PLACED AFTER THE ABOVE TWO LINES
        self.rolls.append(0)                    # this line and the line above creates a buffer in the rolls list so it does not create a out of index problem. 

        # NEW CODE
        self.rolls.append(0) 
        # NEW CODE 
         
        while rollIndex <= upperLimitOfList:
            if frameCount < 10:                                         # score under 9 frames
                if self.isStrike(rollIndex):                            # checks to see if strike
                    result += self.strikeScore(rollIndex)               # scores strike
                    rollIndex +=1                                       # only advances one because strike takes 1 index position
                    frameCount +=1                                      # one frame accomplished
                elif self.isSpare(rollIndex):                           # checks to see if spare
                    result += self.spareScore(rollIndex)                # scores the spare
                    rollIndex +=2                                       # the rollIndex jumps 2 because spare takes 2 index position
                    frameCount +=1                                      # one frame accomplished

                # NEW CODE
                else:
                    result += self.rolls[rollIndex] + self.rolls[rollIndex+1]
                    rollIndex +=2 
                    frameCount +=1 
                # NEW CODE    

                '''
                else: 
                    result += self.frameScore(rollIndex)                # scores the pins, 2 index positions
                    rollIndex +=1                                       # changed 1 to 2 because it needs to count 2 because there are two pins to a frame
                    frameCount +=0.5                                    # half a frame accomlished
                '''
                    
            elif frameCount >= 10:                                      # score over 9 frames.  On the ten frame the Scoring rules change
                result += self.rolls[rollIndex]
                rollIndex +=1 
        self.rolls.pop()
        self.rolls.pop()                                                # this line and the line above removes the buffer 
        return result
    
    def isStrike(self, rollIndex):                                      # if index position = 10 strike                                    
        return self.rolls[rollIndex] == 10                              # returns value for strike = 10

    def isSpare(self, rollIndex):                                       # if 2 index position = 10, then it is a spare
            return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10   # this line counts the 2 pins together to determine if its a spare

    def strikeScore(self,rollIndex):                                    # if index position is 10. it is a strike
            return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2] # scoring for a strike

    def spareScore(self,rollIndex):                                     # if 2 index position adds to 10 it is a spare   
            return  10+ self.rolls[rollIndex+2]                         # This counts the spare (10) plus next value on index

    def frameScore(self, rollIndex):                                    # if not a strike or spare it counts that index position   
        return self.rolls[rollIndex]                                    # returns that value
		

#Your tasks for code parts:
#1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
#2: Refactor the code (Improve its structure without changing external behaviour).
#3: Report everything using github commits and versioning control.


###### Important #####
# Please complete your project and all tasks according to assessment description provided in CANVAS.

