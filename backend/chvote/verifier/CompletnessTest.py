import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import test_run_decorate, completness_test


class SingleCompletnessTest(SingleTest):
    """docstring for a Single CompletnessTest"""
    
    @test_run_decorate
    def runTest(self,election_data):
        """
        >>> res = sct.runTest({'test':123})
        >>> res.test_result
        'successful'
        >>> sct.test_result.test_data
        [{'test': 123}]
        >>> res = sct.runTest({'bla':123})
        >>> res.test_result
        'failed'
        >>> sct.test_result.test_data
        []
        """
        return 'successful' if completness_test(self,election_data) else 'failed'

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'sct': SingleCompletnessTest("1.1","TEST","TEST",["test"])})
