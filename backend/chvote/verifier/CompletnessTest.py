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
        [{'test': 'was found in election data'}]
        >>> res = sct.runTest({'bla':123})
        >>> res.test_result
        'failed'
        >>> sct.test_result.test_data
        [{'test': 'was not found in election data'}]
        """
        result = self.test_result
        if completness_test(self,election_data,False):
            res = 'successful'
            result.addTestData(self.keys[-1],'was found in election data')
        else:
            res = 'failed'
            result.addTestData(self.keys[-1],'was not found in election data')
        return res

if __name__ == '__main__':
    import doctest
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    doctest.testmod(extraglobs={'sct': SingleCompletnessTest("1.1","TEST","TEST",["test"])})
