import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class EligibilityMatrixIntegrityTest(SingleTest):
    """docstring for EligibilityMatrixIntegrityTest."""

    @completness_decorate
    def runTest(self,election_data):
        """
        Test if sum(e_ij) >= 1
        >>> res = emit.runTest({'e_i': [True]})
        >>> res.test_result
        'successful'
        """
        e_j_list = self.test_data
        return 'successful' if sum(e_j_list) >= 1 else 'failed'

if __name__ == '__main__':
    import doctest
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    doctest.testmod(extraglobs={'emit': EligibilityMatrixIntegrityTest("1.1","TEST","TEST",["e_i"])})
