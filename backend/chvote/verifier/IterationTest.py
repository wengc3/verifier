import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate, checkResult, updateProgress

class IterationTest(SingleTest):
    """docstring for IterationTest."""
    def __init__(self,key,title,test,range_key):
        SingleTest.__init__(self, test.id,title+test.title,test.description,key)
        if 'multi' not in test.id:
            self.id = self.id[:-2]
        self._test = test
        self._range_key = range_key

    @property
    def test(self):
        return self._test

    @property
    def range_key(self):
        return self._range_key

    @completness_decorate
    def runTest(self,election_data):
        key = self.key
        vector = election_data[key]
        rng = election_data[self.range_key]
        test = self.test
        test.election_data = election_data
        iter_result = "successful"
        for index in range(rng):
            test.id = test.id[:-1] + str(index+1)
            res = test.runTest(vector[index])
            self.test_result.addChild(res)
            iter_result = checkResult(res)
            updateProgress(self.test_result,index,vector)
        return iter_result
