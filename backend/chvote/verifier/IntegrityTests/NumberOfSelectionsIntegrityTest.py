import os, sys
from gmpy2 import mpz
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

# TODO: how to implement ?
class NumberOfSelectionsIntegrityTest(SingleTest):
    """docstring for NumberOfSelectionsIntegrityTest."""

    @completness_decorate
    def runTest(self,election_data):
        """
        Test if k = sum(k_j)
        """
        numberOfSelections = [item['k_j'] for item in self.test_data]
        k = self.election_data['secparams'].k
        return 'successful' if k == sum(numberOfSelections) else 'failed'
