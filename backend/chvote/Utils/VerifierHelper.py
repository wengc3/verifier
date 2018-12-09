from chvote.verifier.TestResult import TestResult
from functools import wraps

def completness_test(self,election_data):
    key = self.key
    try:
        data = election_data[key]
        self.test_result.addTestData(key,data)
        return True
    except KeyError:
        return False

def test_run_decorate(func):
    @wraps(func)
    def func_wrapper(self,election_data):
        result = TestResult(self,"empty Result",None)
        self.test_result = result
        res = func(self,election_data)
        result.test_result = res
        result.progress = 1
        return result
    return func_wrapper


def completness_decorate(func):
    @wraps(func)
    @test_run_decorate
    def func_wrapper(self,election_data):
        com_test = completness_test(self,election_data)
        if com_test:
            return func(self,election_data)
        else:
            return "skipped"
    return func_wrapper

def checkResult(res):
    if res.test_result in {"failed","skipped"}:
         return "failed"
    return "successful"

def updateProgress(res,index,vector):
    prg = (index+1) / len(vector)
    res.progress = prg