import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class VectorLengthConsistenyTest(SingleTest):
    """
    docstring for VectorLengthConsistenyTest.
    """
    def __init__(self,id,title,description,key, test_key):
        SingleTest.__init__(self, id,title,description,key)
        self.refer_key = test_key

    @completness_decorate
    def runTest(self,election_data):
        """
        Check if vector has required lenght.
        >>> res = lect.runTest({'test':[1,1,1,1],'t': 4})
        >>> res.test_result
        'successful'
        >>> res.test_data
        [{'test': [1, 1, 1, 1]}, {'t': 4}]
        >>> res = lect.runTest({'test':[1,1,1],'t': 4})
        >>> res.test_result
        'failed'
        >>> res.test_data
        [{'test': [1, 1, 1]}, {'t': 4}]
        >>> res = lect.runTest({'bla':[1,1,1],'t': 4})
        >>> res.test_result
        'skipped'
        >>> res = lect.runTest({'test':[1,1,1],'bla': 4})
        >>> res.test_result
        'skipped'
        """
        try:
            sec = self.test_data
            if hasattr(self,'election_data'):
                election_data = self.election_data
            size = election_data[self.refer_key]
            self.test_result.addTestData(self.refer_key,size)
            return 'successful' if len(sec) == size else 'failed'
        except KeyError:
            return 'skipped'


if __name__ == '__main__':
    import doctest
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    doctest.testmod(extraglobs={'lect': VectorLengthConsistenyTest("1.1","TEST","TEST",["test"],"t")})
