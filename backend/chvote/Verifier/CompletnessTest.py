import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import test_run_decorate


class SingleCompletnessTest(SingleTest):
    """docstring for a Single CompletnessTest"""
    def __init__(self,id,title,description,key):
        SingleTest.__init__(self, id,title,description,key)

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
        key = self.key
        try:
            data = election_data[key]
            self.test_result.addTestData(key,data)
            return "successful"
        except KeyError:
            return "failed"




if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'sct': SingleCompletnessTest("1.1","TEST","TEST","test")})
