import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate

class LenghtEqualityConsistenyTest(SingleTest):
    """
    docstring for LenghtEqualityTest. Check if two sequences has the same lenght
    """
    def __init__(self,id,title,description,key, test_key):
        SingleTest.__init__(self, id,title,description,key)
        self.refer_key = test_key

    @completness_decorate
    def runTest(self,election_data):
        """
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
        >>> res.test_data
        []
        """
        sec_1 = self.test_data
        size = election_data.get(self.refer_key)
        if not size:
            size = self.election_data[self.refer_key]
        self.test_result.addTestData(self.refer_key,size)
        return 'successful' if len(sec_1)== size else 'failed'

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'lect': LenghtEqualityConsistenyTest("1.1","TEST","TEST",["test"],"t")})
