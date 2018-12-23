import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate, checkResult, updateProgress

class IterationTest(SingleTest):
    """docstring for IterationTest."""
    def __init__(self,keys,title,test,range_key):
        SingleTest.__init__(self, test.id,title+test.title,test.description,keys)
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
        vector = self.test_data
        if hasattr(self,'election_data'):
            rng = self.election_data.get(self.range_key,0)
        else:
            rng = election_data.get(self.range_key,0)
        test = self.test
        test.election_data = election_data
        try:
            for index in range(rng):
                test.id = test.id[:-1] + str(index+1)
                res = test.runTest(vector[index])
                self.test_result.addChild(res)
                updateProgress(self.test_result,index,vector)
            return checkResult(self.test_result)
        except IndexError:
            return 'failed'
