import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.verifier.SingleTest import SingleTest
from app.verifier.TestResult import TestResult

class IterationTest(SingleTest):
    """docstring for IterationTest."""
    def __init__(self,key,title,test):
        SingleTest.__init__(self, test.id,title+test.title,test.description,key)
        self._test = test

    @property
    def test(self):
        return self._test

    def runTest(self,election_data,report):
        self._notify("TestRunning")
        self.progress = 0
        key = self.key
        test_data = dict()
        try:
            vector = election_data[key]
            test_data[key]=vector
            test = self.test
            test.election_data = election_data
            test_id=test.id
            test_result = "successful"
            for index,item in enumerate(vector):
                test.id = test_id+"."+str(index+1)
                res = test.runTest(item,report)
                test.old_progress = 0
                report.addTestResult(res)
                if res.test_result in {"failed","skipped"}:
                        test_result = "failed"
                prg = (index+1) / len(vector)
                self.progress = prg

            self.progress = 1
            return TestResult(self,test_result,test_data)
        except KeyError:
            self.progress = 1
            return TestResult(self,"skipped",test_data)
