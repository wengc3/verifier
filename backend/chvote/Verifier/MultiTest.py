import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.Test import Test
from chvote.Utils.VerifierHelper import test_run_decorate, checkResult, updateProgress

class MultiTest(Test):
    """ Define behavior for Test having a List of Tests.
        Store in test_list.
        Implement child-related operations like addTest."""
    def __init__(self,id,title,description):
        Test.__init__(self, id,title,description)
        self._test_list = list()

    @property
    def test_list(self):
        return self._test_list

    def addTest(self,test):
        self.test_list.append(test)

    def addTests(self,*args):
        for test in args:
            self.addTest(test)

    @test_run_decorate
    def runTest(self,election_data):
        multi_result = "successful"
        for index,test in enumerate(self.test_list):
            if self.id == "no id":
                test.id = test.id[:-1] + str(index+1)
            res = test.runTest(election_data)
            self.test_result.addChild(res)
            multi_result = checkResult(res)
            updateProgress(self.test_result,index,self.test_list)
        return multi_result