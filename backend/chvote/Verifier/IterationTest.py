import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from chvote.verifier.SingleTest import SingleTest
from chvote.verifier.TestResult import TestResult

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
        iter_result = TestResult(self,"successful",None)
        try:
            vector = election_data[key]
            test = self.test
            test.election_data = election_data
            test_id=test.id

            test_result = "successful"
            for index,item in enumerate(vector):
                test.id = test_id+"."+str(index+1)
                res = test.runTest(item,report)
                report.addTestResult(res)
                iter_result.children[test.id]=res
                self.old_progress = 0
                if res.test_result in {"failed","skipped"}:
                        iter_result.test_result = "failed"
                prg = (index+1) / len(vector)
                self.progress = prg

            self.progress = 1
            return iter_result
        except KeyError as error:
            self.progress = 1
            return TestResult(self,"skipped",test_data)
