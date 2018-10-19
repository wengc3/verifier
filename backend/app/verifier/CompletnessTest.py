from app.verifier.Test import Test

class SingleCompletnessTest(Test):
    """Class for a Single CompletnessTest"""
    def __init__(self,id,title,description,election_data,key_chain):
        Test.__init__(self, id,title,description,election_data)
        self.key_chain = key_chain

    def getKeyChain(self):
        return self.key_chain

    def runTest(self):
        key = self.getKeyChain()[0]
        result = self.getData().get(key,False)
        if result:
            result = True
        return result
