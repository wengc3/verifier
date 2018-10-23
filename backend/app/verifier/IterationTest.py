from app.verifier.SingleTest import SingleTest

class IterationTest(SingleTest):
    """docstring for IterationTest."""
    def __init__(self,id,title,description,key,test):
        SingleTest.__init__(self, id,title,description,key)
        self.test = test

    def getTest(self):
        return self.test

    def runTest(self,election_data):
        vector = election_data[self.getKey()]
        test = self.getTest()
        test_id=test.getId()
        results = {test_id:list()}
        for index,item in enumerate(vector):
            res=test.runTest(item)
            results[test_id].append((test_id+"."str(index),res))
        return results
