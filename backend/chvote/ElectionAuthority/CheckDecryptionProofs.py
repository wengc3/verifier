import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chvote.Utils.Utils                                import AssertList, AssertClass
from chvote.Types                                      import *
from chvote.Common.SecurityParams import SecurityParams
from chvote.ElectionAuthority.CheckDecryptionProof     import CheckDecryptionProof

def CheckDecryptionProofs(pi_prime_bold, pk_bold, e_bold, B_prime_bold, secparams):
    """
    Algorithm 7.51: Checks if the decryption proofs generated by s different authorities are
    correct.

    Args:
        pi_prime_bold (list of DecryptionProof):    Decryption proofs
        pk_bold (list of mpz):                      Encryption key shares
        e_bold (list of ElGamalEncryption):         ElGamal encryptions
        B_prime_bold (list):                        Partial decryptions
        secparams (SecurityParams):                 Collection of public security parameters

    Returns:
        bool
    """
    AssertList(pi_prime_bold)
    AssertList(pk_bold)
    AssertList(e_bold)
    AssertList(B_prime_bold)
    AssertClass(secparams, SecurityParams)

    s = len(pk_bold)
    for j in range(s):
        if not CheckDecryptionProof(pi_prime_bold[j], pk_bold[j], e_bold, B_prime_bold[j], secparams):
            return False
    return True


class CheckDecryptionProofsTest(unittest.TestCase):
    def testCheckDecryptionProofs(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
