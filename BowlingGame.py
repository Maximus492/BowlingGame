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
        upperLimitOfList = lengthOfRolls - 1   # create the limit of the 'while' loop
        self.rolls.append(0)                    # IMPORTANT - THIS LINE AND THE LINE BELOW NEEDS TO BE PLACED AFTER THE ABOVE TWO LINES
        self.rolls.append(0)                    # this line and the line above creates a buffer in the rolls list so it does not create a out of index problem.  
        while rollIndex <= upperLimitOfList:
            if frameCount < 10:                                         # score under 9 frames
                if self.isStrike(rollIndex):                            # checks to see if strike
                    result += self.strikeScore(rollIndex)   # scores strike
                    rollIndex +=1                                       # only advances one because strike takes 1 index position
                    frameCount +=1                                      # one frame accomplished
                elif self.isSpare(rollIndex):         # checks to see if spare
                    result += self.spareScore(rollIndex)    # scores the spare
                    rollIndex +=2                                       # the rollIndex jumps 2 because spare takes 2 index position
                    frameCount +=1                                      # one frame accomplished
                else: 
                    result += self.frameScore(rollIndex)    # scores the pins, 2 index positions
                    rollIndex +=1                                       # changed 1 to 2 because it needs to count 2 because there are two pins to a frame
                    frameCount +=0.5                                    # half a frame accomlished
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


# Below is homemade test code - doesn't count strikes or spares
'''
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
'''
'''
def BowlStrike():
    print("**************************************")
    print("")
    game = BowlingGame()
    print("working so far")
    game.roll(5)                  # 10
    game.roll(5)                  # 30

    game.roll(3)                  # 60
    game.roll(3)                  # 60

    game.roll(3)                  # 60
    game.roll(3)                  # 60

    game.roll(3)                  # 60
    game.roll(3)                  # 60

    game.roll(3)                  # 60
    game.roll(3)                  # 60

    game.roll(3)                  # 60
    game.roll(3)                  # 60

    game.roll(3)                  # 60
    game.roll(3)                  # 60

    game.roll(3)                  # 60
    game.roll(3)                  # 60

    game.roll(3)                  # 60
    game.roll(3)                  # 60

    game.roll(3)                  # 60
    game.roll(3)                  # 60



    print(game.rolls)
    results = game.score()
    print(results)

BowlStrike()
'''
'''
def BowlStrike():
    print("**************************************")
    print("")
    game = BowlingGame()
    print("working so far")
    game.roll(10)                  # 10
    game.roll(10)                  # 10
    game.roll(10)                  # 10
    game.roll(10)                  # 10
    game.roll(10)                  # 10

    game.roll(10)                  # 10
    game.roll(10)                  # 10
    game.roll(10)                  # 10
    game.roll(5)                  # 10   
    game.roll(5)                  # 10

    
    #game.roll(10)                  # 10
    #game.roll(10)                  # 10 
    

    print(game.rolls)
    results = game.score()
    print(results)

BowlStrike()
'''

'''
def BowlStrike():
    print("**************************************")
    print("")
    game = BowlingGame()

    game.roll(10)
    game.roll(4)
    game.roll(3)
    
 
    game.roll(5)
    game.roll(5) 
    game.roll(5)
    game.roll(5)
    game.roll(5) 

    game.roll(5)
    game.roll(5) 
    game.roll(5)
    game.roll(5)
    game.roll(5) 

    game.roll(5)
    game.roll(5) 
    game.roll(5)
    game.roll(5)
    game.roll(5) 

    game.roll(5)
    game.roll(5) 
    game.roll(5)
    game.roll(5)
    game.roll(5)

    game.roll(5)
    #game.roll(3)

    print(game.rolls)
    results = game.score()
    print(results)

BowlStrike()
   '''

def BowlStrike():
    print("**************************************")
    print("")
    game = BowlingGame()

    game.roll(10)         
    game.roll(10)      
    game.roll(10)      
         
    game.roll(5)            
    game.roll(4) 
    game.roll(3)                  
    game.roll(1)                  
    game.roll(5)   
    game.roll(5)         
    game.roll(10)      
    game.roll(10)
    #game.roll(4) 
    #game.roll(6)  
    #game.roll(1)
     

    print(game.rolls)
    results = game.score()
    print(results)

BowlStrike()

'''

class BowlingGame:
    def __init__(self):
        self.rolls=[]           # any array (might be a list) is created called rolls
       
    def roll(self,pins):        # this method adds to the roll array
        self.rolls.append(pins)
        
    def score(self):
        result = 0                              
        rollIndex=0
        frameCount=0                            # this counts the frame going into 
        lengthOfRolls = len(self.rolls)         # get length of self.rolls.list
        upperLimitOfArray = lengthOfRolls - 1   # create the limit of the 'while' loop
        self.rolls.append(0)  # IMPORTANT - THIS LINE AND THE LINE BELOW NEEDS TO BE PLACED AFTER THE ABOVE TWO LINES
        self.rolls.append(0)  # this line and the line above creates a buffer in the rolls list so it does not create a out of index problem.  
        print(self.rolls)
        while rollIndex <= upperLimitOfArray:
            #if frameCount < 9:                                         # score under 9 frames
                if self.isStrike(rollIndex):                            # checks to see if strike
                    result += self.strikeScore(rollIndex, frameCount)   # scores strike
                    rollIndex +=1                                       # only advances one because strike takes 1 index position
                    frameCount +=1                                      # one frame accomplished

                elif self.isSpare(rollIndex,upperLimitOfArray):         # checks to see if spare
                    result += self.spareScore(rollIndex, frameCount)    # scores the spare
                    rollIndex +=2                                       # the rollIndex jumps 2 because spare takes 2 index position
                    frameCount +=1                                      # one frame accomplished
                else: 
                    result += self.frameScore(rollIndex, frameCount)    # scores the pins, 2 index positions
                    rollIndex +=2                                       # changed 1 to 2 because it needs to count 2 because there are two pins to a frame
                    frameCount +=1                                      # one frame accomplished
            #elif frameCount >= 10:
                #if self.isStrike(rollIndex): 
                #    result += 10
                #    rollIndex +=1
                #    frameCount +=1 
        self.rolls.pop()
        self.rolls.pop()                                    # this line and the line above removes the buffer 
        print(self.rolls)                                   # testing purposes
        print("framecount " + str(frameCount))              # testing purposes
        return result
    
    def isStrike(self, rollIndex):                          
        return self.rolls[rollIndex] == 10                  # if index position = 10 then it is a strike

    def isSpare(self, rollIndex,upperLimitOfArray):         # if 2 index position = 10, then it is a spare
        if rollIndex == upperLimitOfArray:                  # This prevents out of index position
            return 0            
        else:
            return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10  # this line counts the 2 pins together to determine if its a spare

    def strikeScore(self,rollIndex, frameCount): 
        if frameCount <= 9:                         # because frameCount starts at 0.  If frameCount starts as 1 the 9 should be 10    
            return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]
        elif frameCount >= 10:                      # because the scoring changes at the end 
            print("over")
            return 10

    def spareScore(self,rollIndex, frameCount):  
        if frameCount <= 9:          
            return  10+ self.rolls[rollIndex+2]     # have to check this either 2 or 1
        elif frameCount >= 10:
            return self.rolls[rollIndex]
            #return self.rolls[rollIndex+2]

    def frameScore(self, rollIndex, frameCount):    
        #  need a if statement here        
        return self.rolls[rollIndex]# removing + self.rolls[rollIndex + 1] to this line.  We only need to count the score at the index, don't need to count the next score on the next index.
		



class BowlingGame:
    def __init__(self):
        self.rolls=[]           # any array (might be a list) is created called rolls
       
    def roll(self,pins):        # this method adds to the roll array
        self.rolls.append(pins)
        
    def score(self):
        result = 0                              
        rollIndex=0
        frameCount=0                            # this counts the frame going into 
        lengthOfRolls = len(self.rolls)         # get length of self.rolls.list
        upperLimitOfArray = lengthOfRolls - 1   # create the limit of the 'while' loop
        self.rolls.append(0)  # IMPORTANT - THIS LINE AND THE LINE BELOW NEEDS TO BE PLACED AFTER THE ABOVE TWO LINES
        self.rolls.append(0)  # this line and the line above creates a buffer in the rolls list so it does not create a out of index problem.  
        print(self.rolls)
        while rollIndex <= upperLimitOfArray:
            print(result)
            print("frameCount start" + str(frameCount))
            if frameCount <= 9:                                         # score under 9 frames
                if self.isStrike(rollIndex):                            # checks to see if strike
                    result += self.strikeScore(rollIndex, frameCount)   # scores strike
                    rollIndex +=1                                       # only advances one because strike takes 1 index position
                    frameCount +=1                                      # one frame accomplished
                elif self.isSpare(rollIndex,upperLimitOfArray):         # checks to see if spare
                    result += self.spareScore(rollIndex, frameCount)    # scores the spare
                    rollIndex +=2                                       # the rollIndex jumps 2 because spare takes 2 index position
                    frameCount +=1                                      # one frame accomplished
                else: 
                    result += self.frameScore(rollIndex, frameCount)    # scores the pins, 2 index positions
                    rollIndex +=1                                       # changed 1 to 2 because it needs to count 2 because there are two pins to a frame
                    frameCount +=1                                      # one frame accomplished
            elif frameCount >= 10:
                result += self.rolls[rollIndex]
                rollIndex +=1 
                print("result wroking" + str(result))



        self.rolls.pop()
        self.rolls.pop()                                    # this line and the line above removes the buffer 
        print(self.rolls)                                   # testing purposes
        print("rollIndex" + str(rollIndex))
        print("upperLimitOfArray " +str(upperLimitOfArray))
        print("framecount " + str(frameCount))              # testing purposes
        return result
    
    def isStrike(self, rollIndex):                          
        return self.rolls[rollIndex] == 10                  # if index position = 10 then it is a strike

    def isSpare(self, rollIndex,upperLimitOfArray):         # if 2 index position = 10, then it is a spare
        #if rollIndex == upperLimitOfArray:                  # This prevents out of index position
            #return 0            
        #else:
            return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10  # this line counts the 2 pins together to determine if its a spare

    def strikeScore(self,rollIndex, frameCount): 
        #if frameCount <= 9:                         # because frameCount starts at 0.  If frameCount starts as 1 the 9 should be 10    
            return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]
        #elif frameCount >= 10:                      # because the scoring changes at the end 
            #print("over")
            #return 10

    def spareScore(self,rollIndex, frameCount):  
        #if frameCount <= 9:          
            return  10+ self.rolls[rollIndex+2]     # have to check this either 2 or 1
        #elif frameCount >= 10:
        #    return self.rolls[rollIndex]
            #return self.rolls[rollIndex+2]

    def frameScore(self, rollIndex, frameCount):    
        #  need a if statement here        
        return self.rolls[rollIndex]# removing + self.rolls[rollIndex + 1] to this line.  We only need to count the score at the index, don't need to count the next score on the next index.
		


'''