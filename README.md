
# Fourth step - get everything together and fix counting frames
#
# note - from now on array will be called list
#
# I realiased that when counting frames it needs to count in 2 increments.
# for example -
# 
# self.rolls[10,1,5,5,1]
#
# the way I had the counting was that it would count 10 as a strike, then count the 
# 1, then it would count the 5 and 5 together.  Unforunately in reality the 5 and 5 
# score are not in the same frame.  Therefore I need to count the 1 and 5 together, 
# and count the 5 and 1 together.  Having the buffer appending into the self.rolls 
# list will hopefully make the code I am thinking work.
#
# Also need to test the counting spare code.  Needd to check that the 
# upperlimtiarray works.




