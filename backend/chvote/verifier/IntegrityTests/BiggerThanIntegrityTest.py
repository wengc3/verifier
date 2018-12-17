import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class BiggerThanIntegrityTest(SingleTest):
    """docstring for ListBiggerThanIntegrityTest."""
    def __init__(self,id,title,description,keys,min_size):
        SingleTest.__init__(self, id,title,description,keys)
        self.min_size = min_size

    @completness_decorate
    def runTest(self,election_data):
        """
        >>> res = btit.runTest({'test': 1})
        >>> res.test_result
        'successful'
        >>> res.test_data
        [{'test': 1}, {'min_size': 1}]
        >>> res = btit.runTest({'test': 0})
        >>> res.test_result
        'failed'
        >>> res.test_data
        [{'test': 0}, {'min_size': 1}]
        >>> res = btit.runTest({'bla': 1})
        >>> res.test_result
        'skipped'
        >>> res.test_data
        []
        """
        value = self.test_data
        self.test_result.addTestData('min_size',self.min_size)
        return 'successful' if  value >= self.min_size else 'failed'

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'btit': BiggerThanIntegrityTest("1.1","TEST","TEST",["test"],1)})
