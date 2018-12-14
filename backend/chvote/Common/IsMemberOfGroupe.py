import os
import sys
import unittest
from gmpy2 import jacobi

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.Utils.Utils           import AssertNumeric, AssertClass
from chvote.Common.SecurityParams import SecurityParams

def IsMemberOfGroupe(x, param):
    """
    Algorithm 7.2 extended: Checks if x is in the same groupe as param .
    The core of the algorithm is the computation of the Jacobi symbol for which we refer to existing algorithms

    Args:
       x (mpz):                             The number to test x \in N
       param (Element of SecurityParams):   Element of Collection of public security parameters

    Returns:
       bool:                                True if x is in the same groupe as param, False if not
    """

    AssertNumeric(x)
    AssertNumeric(param)

    if 1 <= x and x < param:
        return jacobi(x, param) == 1

    return False

class GetPrimesTest(unittest.TestCase):
    def testOne(self):
        # Test if the numbers 1,3,4,5,9 are recognized as members of G_q for q = 5 and p = 11
        dummySecParams = SecurityParams(4,4,
                11,
                5,
                2,4,9,787,131,6,64,131,8,True)
        self.assertTrue(IsMemberOfGroupe(1,dummySecParams.p))
        self.assertFalse(IsMemberOfGroupe(2, dummySecParams.p))
        self.assertTrue(IsMemberOfGroupe(3, dummySecParams.p))
        self.assertTrue(IsMemberOfGroupe(4, dummySecParams.p))
        self.assertTrue(IsMemberOfGroupe(5, dummySecParams.p))
        self.assertFalse(IsMemberOfGroupe(6, dummySecParams.p))
        self.assertFalse(IsMemberOfGroupe(7, dummySecParams.p))
        self.assertFalse(IsMemberOfGroupe(8, dummySecParams.p))
        self.assertTrue(IsMemberOfGroupe(9, dummySecParams.p))

if __name__ == '__main__':
    unittest.main()
