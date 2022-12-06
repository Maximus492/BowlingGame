#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest


import BowlingGame



class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(0, 20):              # one in twenty simultates the 20 rolls
            self.game.rolls(0)  
        assert self.game.score()==0         # this test needs adjstment
    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score()==20
    def testJustPins(self):                 #  this test has been adjusted to account for strikes
        self.game.roll(10)         
        self.game.roll(10)      
        self.game.roll(10)             
        self.game.roll(5)            
        self.game.roll(4) 
        self.game.roll(3)                  
        self.game.roll(1)                  
        self.game.roll(5)   
        self.game.roll(10)         
        self.game.roll(10)      
        self.game.roll(10)                
        assert self.game.score()==152
    def testForStrikesAtLastOfArray(self):  # this test to test for out of index errors when counting strikes
        self.game.roll(10)                 
        self.game.roll(10)                  
        self.game.roll(10)
        assert self.game.score()==60
    def testOneSpare(self):
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0,17)
        assert self.game.score()==16
    def testOneStrike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0,16)
        assert  self.game.score()==24
    def testPerfectGame(self):
        self.rollMany(10,12)
        assert self.game.score()==300
    def testOneSpare(self):
        self.rollMany(5,21)
        assert self.game.score()==150
    def rollMany(self, pins,rolls):
        for i in range(rolls):
            self.game.rolls(pins)
			
# rolls is every throw

if __name__ == '__main__':
    unittest.main()

