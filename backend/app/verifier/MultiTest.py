from app.verifier.Test import Test

class MultiTest(Test):
    """ Define behavior for Test having a List of Testsself.
        Store in test_list.
        Implement child-related operations like addTest."""
    def __init__(self, self, id,title,description,election_data):
        Test.__init__(self, id,title,description,election_data)
        self._test_list = List()

    def getTestList(self):
        return self._test_list

    def addTest(self,test):
        self.getTestList().add(test)

    def runTest(self):
        for test in self.getTestList():
            res = test.runTest()
            Test.current_test = test
            Test.return_methode(res)
