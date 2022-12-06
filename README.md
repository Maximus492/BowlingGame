# BowlingGame
# mk 3 of second step
#
# note - from now on array will be called list
#
# To stop the roll out of index problem, after the rolls list is created with 
# scores, when the     def score(self): method is called up the code adds
#           self.rolls.append(0) 
#           self.rolls.append(0)
#
# These 2 lines create in essence a buffer.  
#
# For example if the self.rolls list is [1,3,10,10] the above code adds two zero's 
# making the list [1,3,10,10,0,0].  Now when the rollIndex gets to index position   
# 2 to read, reads the value 10 and then tries to read the next postion
# [rollIndex# +1] there is now something to read and doesn't throw a out of index 
# error.  Then on [rollIndex +2] there is also something to read.  Because the 
# value is 0 nothing is added.  
# after the scoring is concluded the buffer is removed by the lines
#           self.rolls.pop()
#           self.rolls.pop()
#
#
#