#File 1 (Test.py)
# This file has information about test cases which you need to test.
# 

import unittest

import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()
    def testGutterGame(self):               # simulates roll all gutterballs
        for i in range(0, 20):              
            self.game.rolls.append(0)  
        assert self.game.score()==0         
    def testAllOnes(self):                  # simulates bowling all ones
        self.rollMany(1, 20)
        assert self.game.score()==20
    def testJustPins(self):                 # this test has been adjusted to account for strikes
        self.game.roll(10)         
        self.game.roll(10)      
        self.game.roll(10)             
        self.game.roll(5)            
        self.game.roll(4) 
        self.game.roll(3)                  
        self.game.roll(5)                   # NEW CODE, THIS CHANGED TO CHECK SPARES                   
        self.game.roll(5)   
        self.game.roll(5)         
        self.game.roll(10)      
        self.game.roll(10)
        self.game.roll(4) 
        self.game.roll(6)                      
        assert self.game.score()==165
    def testForStrikesAtLastOfArray(self):  # this test to test for out of index errors when counting strikes/test strike counting working
        self.game.roll(10)                 
        self.game.roll(10)                  
        self.game.roll(10)
        assert self.game.score()==60
    def testOneSpare(self):                 # Testing that the spare calculation is working
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score()==16
    def testOneStrike(self):                # first frame strike, second pin 4, third pin 3/ test scoring after strike
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        assert  self.game.score()==24
    def testNineStrikes(self):              # first nine frames are strikes, last frame gutterballs
         self.rollMany(10,9) 
         self.game.roll(0) 
         self.game.roll(0) 
         assert  self.game.score()==240
    def testNineStrikes(self):              # first ten frames are strikes, extra ball gutterball
         self.rollMany(10,10) 
         self.game.roll(0) 
         assert  self.game.score()==270
    def testPerfectGame(self):              # test for the perfect game, twelve strikes
        self.rollMany(10,12)
        assert self.game.score()==300
    def testSpares(self):                   # test for rolling all pins 5
        self.rollMany(5,21)
        assert self.game.score()==150
    def rollMany(self, pins,rolls):         # this is used for other test methods above.  quick way of populating the rolls list
        for i in range(rolls):
            self.game.rolls.append(pins)
			


if __name__ == '__main__':
    unittest.main()

