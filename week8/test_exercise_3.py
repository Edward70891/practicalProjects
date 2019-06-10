'''
Created on 1 Dec 2016

@author: Lilian
'''
import unittest
import inspect
from recursion import sum_all

class TestExercise3(unittest.TestCase):
    
    def testSumNormal(self):
        self.assertEqual(10, sum_all([0,1,2,3,4]), "sum_all([0,1,2,3,4]) incorrect")
         
    def testSumEmpty(self):
        self.assertEqual(0, sum_all([]), "sum_all([]) incorrect!")
        
    def testSumIgnoreEmpty(self):
        self.assertEqual(10, sum_all([0,1,2,3,4,[]]), "sum_all([0,1,2,3,4,[]]) incorrect, should ignore []!")
        self.assertEqual(10, sum_all([0,[1,[2,3,[]]],4,[]]), "sum_all([0,[1,[2,3,[]]],4,[]]) incorrect, should ignore []!")
        
    def testSumNested(self):
        self.assertEqual(10, sum_all([0,[1,[2,3]],4]), "sum_all([0,[1,[2,3]],4]) incorrect!")
        

if __name__ == "__main__":
    unittest.main()
