# BowlingGame
# mk 2 of second step
# Previously code was just reading pins.  Now code is added to read strikes.
#       def testJustPins(self): test adjusted to account for strike counting
#       def testForStrikesAtLastOfArray(self):  test created to check for out of index error when testing for strikes
#       
# it is counting the strikes 
# however if the last or second to last value in the array is 10 it produces a out of index error,
#
# because in the code below the rollIndex+1 and rollIndex+2 is out of index on the array it is checking.
#     def strikeScore(self,rollIndex):            
#        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]
#
#
# changed     if self.isStrike(rollIndex):
#                   result += self.strikeScore(rollIndex,upperLimitOfArray)
#                   rollIndex +=1
#
#
# changed     def StrikeScore(self,rollIndex,upperLimitOfArray):
#                   almostupperLimitOfArray =  upperLimitOfArray - 1
#                   if rollIndex == upperLimitOfArray:
#                       return 10
#                   elif rollIndex == almostupperLimitOfArray:
#                       return  10+ self.rolls[rollIndex+1]
#                   else:    
#                       return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]
#
#   The code above makes sure it does not get an out of index error.  
#   However it is very complex so I might try and think of another way to remove the error.
#
# def testForStrikesAtLastOfArray(self):  test created to check for out of index error when testing for strikes
# this test case is just to test if it is reading counting and scoring the frames correctly
# the assert line would have to be different on the finished code.
#
# 
# on unittest it passed the test code I created - 
# 
#    def testJustPins(self): 
#    def testForStrikesAtLastOfArray(self): 
#
#
#   Also I noticed that I think this test needs adjsutment
#
#            def testGutterGame(self):
#                   for i in range(0, 20):              # one in twenty simultates the 20 rolls
#                   self.game.rolls(0)  
#                        assert self.game.score()==0         # this test needs adjustment in what the score should be,   I think.
#
