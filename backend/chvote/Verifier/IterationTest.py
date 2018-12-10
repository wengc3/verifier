import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.SingleTest import SingleTest
from chvote.Utils.VerifierHelper import completness_decorate, checkResult, updateProgress

class IterationTest(SingleTest):
    """docstring for IterationTest."""
    def __init__(self,key,title,test):
        SingleTest.__init__(self, test.id,title+test.title,test.description,key)
        if 'multi' not in self.id:
            self.id = self.id[:-2]
        self._test = test

    @property
    def test(self):
        return self._test

    @completness_decorate
    def runTest(self,election_data):
        key = self.key
        vector = election_data[key]
        test = self.test
        test.election_data = election_data
        iter_result = "successful"
        for index,item in enumerate(vector):
            test.id = test.id[:-1] + str(index+1)
            res = test.runTest(item)
            self.test_result.addChild(res)
            iter_result = checkResult(res)
            updateProgress(self.test_result,index,vector)
        return iter_result
