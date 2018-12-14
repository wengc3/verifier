import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class InRangeIntegrityTest(SingleTest):
    """docstring for InRangeIntegrityTest."""
    def __init__(self,id,title,description,key,param):
        SingleTest.__init__(self, id,title,description,key)
        self.param = param

    @completness_decorate
    def runTest(self,election_data):
        """
        Test if element is in range(1,param + 1)
        >>> res = irit.runTest({'w_i': 1})
        >>> res.test_result
        'successful'
        """
        key = self.key
        value = election_data[key]
        param = self.election_data[self.param]
        return 'successful' if value in range(1,param + 1) else 'failed'

if __name__ == '__main__':
    import doctest
    iri_test = InRangeIntegrityTest("1.1","TEST","TEST","w_i",'w')
    iri_test.election_data = {'w': 1}
    doctest.testmod(extraglobs={'irit': iri_test})
