import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class MatrixLengthConsistenyTest(SingleTest):
    """
    docstring for MatrixLengthConsistenyTest.
    """
    def __init__(self,id,title,description,key, test_keys):
        SingleTest.__init__(self, id,title,description,key)
        self.refer_keys = test_keys

    @completness_decorate
    def runTest(self,election_data):
        """
        Check if vector has required lenght.
        >>> res = mlct.runTest({'test':[{'e_i': [True]}, {'e_i': [True]}, {'e_i': [True]}],'Ne': 3, 't': 1})
        >>> res.test_result
        'successful'
        >>> res = mlct.runTest({'test':[{'e_i': [True]}, {'e_i': [True]}, {'e_i': [True]}],'Ne': 2, 't': 1})
        >>> res.test_result
        'failed'
        """
        try:
            key_0, key_1, elem_key = self.refer_keys
            matrix = [elem[elem_key] for elem in self.test_data]
            if hasattr(self,'election_data'):
                election_data = self.election_data
            size_0 = election_data[key_0]
            size_1 = election_data[key_1]
            self.test_result.addTestData(key_0, size_0)
            self.test_result.addTestData(key_1 , size_1)
            res_sec_0 = len(matrix) == size_0
            res_sec_1 = all([len(elem) == size_1 for elem in matrix])
            return 'successful' if res_sec_0 and res_sec_1 else 'failed'
        except KeyError:
            return 'skipped'


if __name__ == '__main__':
    import doctest
    from chvote.verifier.TestResult import TestResult
    from app.verifier.Report import Report
    TestResult.setReport(Report("1"))
    doctest.testmod(extraglobs={'mlct': MatrixLengthConsistenyTest("1.1","TEST","TEST",["test"],["Ne","t",'e_i'])})
