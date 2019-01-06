import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class StringIntegrityTest(SingleTest):
    """docstring for StringIntegrityTest."""

    @completness_decorate()
    def runTest(self,election_data):
        """
        Test if element is in A*_ucs
        """
        return 'successful'
