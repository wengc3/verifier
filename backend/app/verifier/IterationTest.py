from app.verifier.SingleTest import SingleTest

class IterationTest(SingleTest):
    """docstring for IterationTest."""
    def __init__(self,key,test):
        SingleTest.__init__(self, test.getId(),test.getTitle(),test.getDescription(),key)
        self.test = test

    def getTest(self):
        return self.test

    def checkResult(self,results):
        for result in results.values():
            if not result[0]:
                return False
        return True

    def runTest(self,election_data):
        key = self.getKey()
        try:
            vector = election_data[key]
            test = self.getTest()
            test_id=test.getId()
            results = dict()
            for index,item in enumerate(vector):
                res=test.runTest(item)
                results[test_id+"."+str(index+1)]=res
            if not self.checkResult(results):
                return (False,results)
            return (True,results)
        except KeyError:
            return (False,None)
