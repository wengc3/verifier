import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class InRangeIntegrityTest(SingleTest):
    """docstring for InRangeIntegrityTest."""
    def __init__(self,id,title,description,keys,min,param):
        SingleTest.__init__(self, id,title,description,keys)
        self.param = param
        self._min = min

    @completness_decorate
    def runTest(self,election_data):
        """
        Test if element is in range(min,max + 1)
        >>> res = irit.runTest({'w_i': 1})
        >>> res.test_result
        'successful'
        """
        value = self.test_data
        max = self.election_data[self.param]
        self.test_result.addTestData('min',self._min)
        self.test_result.addTestData('max',max)
        return 'successful' if value in range(self._min,max + 1) else 'failed'

if __name__ == '__main__':
    import doctest
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    iri_test = InRangeIntegrityTest("1.1","TEST","TEST",["w_i"],1,'w')
    iri_test.election_data = {'w': 1}
    doctest.testmod(extraglobs={'irit': iri_test})
