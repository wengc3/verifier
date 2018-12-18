import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class EligibilityMatrixBitIntegrityTest(SingleTest):
    """docstring for BitIntegrityTest."""

    @completness_decorate
    def runTest(self,election_data):
        """
        Test if element is in [0,1]
        >>> res = embit.runTest({'e_i': [True]})
        >>> res.test_result
        'successful'
        """
        bit_arr = self.test_data
        rng = self.election_data['t']
        res = 'successful'
        for j in range(rng):
            if not isinstance(bit_arr[j],bool):
                res = 'failed'
        return res

if __name__ == '__main__':
    import doctest
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    embi_test = EligibilityMatrixBitIntegrityTest("1.1","TEST","TEST",["e_i"])
    embi_test.election_data = {'t':1}
    doctest.testmod(extraglobs={'embit': embi_test })
