import os, sys
from functools import wraps
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.verifier.SingleTest import SingleTest
from app.verifier.TestResult import TestResult


#TODO check Completness for other tests
def completness_decorator(func):
    @wraps(func)
    def wrapper(self,election_data,report):
        key = self.key
        try:
            data = election_data[key]
            return self.func(data,report)
        except KeyError:
            setattr(self,key, key+": is not in election data")
            return False
    return wrapper

class SingleCompletnessTest(SingleTest):
    """docstring for a Single CompletnessTest"""
    def __init__(self,id,title,description,key):
        SingleTest.__init__(self, id,title,description,key)

    def runTest(self,election_data,report):
        """
        >>> res = sct.runTest({'test':123},report)
        >>> res.test_result
        'successful'
        >>> res.test_data
        {'test': 123}
        >>> res = sct.runTest({'bla':123},report)
        >>> res.test_result
        'failed'
        >>> res.test_data
        {}
        """
        self._notify("TestRunning")
        self.progress = 0
        key = self.key
        test_data = dict()
        try:
            data = election_data[key]
            test_data[key]=data
            self.progress = 1
            return TestResult(self,"successful",test_data)
        except KeyError:
            self.progress = 1
            return TestResult(self,"failed",test_data)




if __name__ == '__main__':
    import doctest
    from Report import Report
    doctest.testmod(extraglobs={'sct': SingleCompletnessTest("1.1","TEST","TEST","test"),
                                'report': Report('id',None)})
