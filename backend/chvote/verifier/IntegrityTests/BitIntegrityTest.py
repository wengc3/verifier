import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class BitIntegrityTest(SingleTest):
    """docstring for BitIntegrityTest."""

    @completness_decorate
    def runTest(self,election_data):
        """
        Test if element is in [0,1]
        >>> res = biit.runTest({'e_j': True})
        >>> res.test_result
        'successful'
        """
        key = self.key
        bit = election_data[key]
        return 'successful' if isinstance(bit,bool) else 'failed'

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'biit': BitIntegrityTest("1.1","TEST","TEST","e_j")})
