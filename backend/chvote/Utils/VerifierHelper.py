"""
This python file conntains several helper functions to avoid redudant code.
"""
from chvote.verifier.TestResult import TestResult
from functools import wraps

def completness_test(self,election_data,addData):
    """
    Test if key is in election_data.
    """
    try:
        key, data = getData(self.keys,election_data)
        self.test_data = data
        if addData:
            self.test_result.addTestData(key,data)
        return True
    except KeyError:
        return False

def getData(keys,election_data):
    """
    Get the data to the corponding key.
    If keys has multiple values the data is a dictionary
    and wit the last key we get the value
    """
    try:
        data = election_data
        for key in keys:
            data = data[key]
        return (key,data)
    except KeyError:
        raise KeyError('No Data')

def test_run_decorate(func):
    """
    Decorater to start and end the Test.
    There is no completness test
    """
    @wraps(func)
    def func_wrapper(self,election_data):
        result = TestResult(self,"empty Result",None)
        self.test_result = result
        res = func(self,election_data)
        result.test_result = res
        result.progress = 1
        return result
    return func_wrapper


def completness_decorate(addData = True):
    """
    Check if there are test data.
    If not don't run the test and return skipped.
    """
    def completness(func):
        @wraps(func)
        @test_run_decorate
        def func_wrapper(self,election_data):
            com_test = completness_test(self,election_data,addData)
            if com_test:
                return func(self,election_data)
            else:
                return "skipped"
        return func_wrapper
    return completness

def checkResult(self):
    results = [res.test_result for res in self.children if res.test_result in ['skipped','failed']]
    if results:
         return 'failed' if 'failed' in results else 'skipped'
    return "successful"

def updateProgress(res,index,vector):
    prg = (index+1) / len(vector)
    res.progress = prg
