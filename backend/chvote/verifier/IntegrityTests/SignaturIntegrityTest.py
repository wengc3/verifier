import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class SignaturIntegrityTest(SingleTest):
    """docstring for SignaturAuthenticityTest."""

    @completness_decorate()
    def runTest(self,election_data):
        """
        Signatures are not in election_data
        """
        pass
