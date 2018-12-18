import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class CertificateAuthenticityTest(SingleTest):
    """docstring for CertificateTest."""

    @completness_decorate
    def runTest(self,election_data):
        """
        Certificates are not in election_data
        >>> res = cauth.runTest({})
        >>> res.test_result
        'skipped'
        >>> res.test_data
        []
        >>> res.progress
        1
        """
        pass

class SignaturAuthenticityTest(SingleTest):
    """docstring for SignaturAuthenticityTest."""

    @completness_decorate
    def runTest(self,election_data):
        """
        Signatures are not in election_data
        >>> res = sigauth.runTest({})
        >>> res.test_result
        'skipped'
        >>> res.test_data
        []
        >>> res.progress
        1
        """
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs = {'cauth': CertificateAuthenticityTest("1.1","TEST","TEST","adminCert"),
                                  'sigauth': SignaturAuthenticityTest("1.1","TEST","TEST","sigParam1")})
