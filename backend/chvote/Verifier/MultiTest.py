import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.Test import Test
from chvote.verifier.TestResult import TestResult

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

    def runTest(self,election_data,report):
        self._notify("TestRunning")
        self.progress = 0
        test_result = "successful"
        for index,test in enumerate(self.test_list):
            res = test.runTest(election_data,report)
            report.addTestResult(res)
            if res.test_result in {"failed","skipped"}:
                    test_result = "failed"
            prg = (index+1) / len(self.test_list)
            self.progress = prg
        if self.id != "0":
            self.progress = 1
            return TestResult(self,test_result,None)
