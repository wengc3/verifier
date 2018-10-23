from app.verifier.SingleTest import SingleTest

class SingleCompletnessTest(SingleTest):
    """Class for a Single CompletnessTest"""
    def __init__(self,id,title,description,election_data,key_chain):
        SingleTest.__init__(self, id,title,description,election_data,key_chain)

    def runTest(self):
        key = self.getKeyChain()[0]
        result = self.getData().get(key,False)
        if result:
            result = True
        return result
