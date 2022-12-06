# BowlingGame
# third step - add counting the spares
#
# note - from now on array will be called list
#
# added the 
#               if self.isSpare(rollIndex):
#                   result += self.spareScore(rollIndex,upperLimitOfArray)
#                   rollIndex +=2 # the rollIndex jumps 2 this time because we have already counted the two in the order in the list together because they are a spare.
#
#
# added the 
#               def isSpare(self, rollIndex):
#                   if rollIndex == upperLimitOfArray:     # this code is to stop going out of index error     
#                       return 0               
#                   else:  
#                       return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10  # this line counts the 2 pins together to determine if its a spare
#
#
# These two methods determine if the next two values in the list add up to 10 then it counts those two values and advances the rollIndex 2 this 
# this time (instead of 1 with the other methods) because those two values have been counted. 
#
#
# realised the pins have to count in doubles as well