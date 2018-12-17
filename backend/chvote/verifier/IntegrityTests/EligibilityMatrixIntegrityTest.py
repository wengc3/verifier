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
        >>> res = emit.runTest({'e_i': [{'e_j': True}]})
        >>> res.test_result
        'successful'
        """
        e_j_list = [ item['e_j'] for item in self.test_data]
        return 'successful' if sum(e_j_list) >= 1 else 'failed'

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'emit': EligibilityMatrixIntegrityTest("1.1","TEST","TEST",["e_i"])})
