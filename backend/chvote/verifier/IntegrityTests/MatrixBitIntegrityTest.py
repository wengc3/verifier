import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class MatrixBitIntegrityTest(SingleTest):
    """docstring for BitIntegrityTest."""
    def __init__(self,id,title,description,keys,param):
        SingleTest.__init__(self, id,title,description,keys)
        self.param = param

    @completness_decorate
    def runTest(self,election_data):
        """
        Test if element is in [0,1]
        >>> res = mbit.runTest({'e_i': [True]})
        >>> res.test_result
        'successful'
        >>> res = mbit.runTest({'e_i': [1]})
        >>> res.test_result
        'successful'
        >>> res = mbit.runTest({'e_i': [0]})
        >>> res.test_result
        'successful'
        >>> res = mbit.runTest({'e_i': [2]})
        >>> res.test_result
        'failed'
        """
        try:
            bit_arr = self.test_data
            rng = self.election_data[self.param]
            res = 'successful'
            self.test_result.addTestData(self.param,rng)
            for j in range(rng):
                if not (isinstance(bit_arr[j],bool) or int(bit_arr[j]) in range(2)):
                    res = 'failed'
            return res
        except IndexError:
            return 'failed'


if __name__ == '__main__':
    import doctest
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    mbi_test = MatrixBitIntegrityTest("1.1","TEST","TEST",["e_i"],'t')
    mbi_test.election_data = {'t':1}
    doctest.testmod(extraglobs={'mbit': mbi_test })
