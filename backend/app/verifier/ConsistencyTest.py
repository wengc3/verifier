import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.verifier.SingleTest import SingleTest
from app.verifier.TestResult import TestResult

class LenghtEqualityConsistenyTest(SingleTest):
    """
    docstring for LenghtEqualityTest. Check if two sequences has the same lenght
    """
    def __init__(self,id,title,description,key, test_key):
        SingleTest.__init__(self, id,title,description,key)
        self.refer_key = test_key

    def runTest(self,election_data,report):
        """
        >>> res = lect.runTest({'test':[1,1,1,1],'test_val':[2,2,2,2]},report)
        >>> res.test_result
        'successful'
        >>> res.test_data
        {'test': [1, 1, 1, 1], 'test_val': [2, 2, 2, 2]}
        >>> res = lect.runTest({'test':[1,1,1],'test_val':[2,2,2,2]},report)
        >>> res.test_result
        'failed'
        >>> res.test_data
        {'test': [1, 1, 1], 'test_val': [2, 2, 2, 2]}
        >>> res = lect.runTest({'test':[1,1,1],'bla':[2,2,2,2]},report)
        >>> res.test_result
        'skipped'
        >>> res.test_data
        {'test': [1, 1, 1]}
        """
        self._notify("TestRunning")
        self.progress = 0
        key = self.key
        test_data = dict()
        try:
            sec_1 = election_data[key]
            test_data[key] = sec_1
            sec_2 = election_data[self.refer_key]
            test_data[self.refer_key] = sec_2
            self.progress = 1
            test_result = 'successful' if len(sec_1)==len(sec_2) else 'failed'
            return TestResult(self,test_result,test_data)
        except KeyError:
            self.progress = 1
            return TestResult(self,'skipped',test_data)

if __name__ == '__main__':
    import doctest
    from Report import Report
    doctest.testmod(extraglobs={'lect': LenghtEqualityConsistenyTest("1.1","TEST","TEST","test","test_val"),
                                'report': Report('id',None)})
