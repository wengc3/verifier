from app.verifier.Test import Test

class MultiTest(Test):
    """ Define behavior for Test having a List of Testsself.
        Store in test_list.
        Implement child-related operations like addTest."""
    def __init__(self,id,title,description):
        Test.__init__(self, id,title,description)
        self._test_list = list()

    def getTestList(self):
        return self._test_list

    def addTest(self,test):
        self.getTestList().append(test)

    def runTest(self,election_data):
        for test in self.getTestList():
            res = test.runTest(election_data)
            self.getReport().addResult((test,res))
        if self.id != "0":
            return self.getReport().getStat(self.getId())
