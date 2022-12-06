# BowlingGame
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

# def testForStrikesAtLastOfArray(self):  test created to check for out of index error when testing for strikes
# this test case is just to test if it is reading counting and scoring the frames correctly
# the assert line would have to be different on the finished code.
