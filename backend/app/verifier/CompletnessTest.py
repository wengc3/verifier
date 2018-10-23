from app.verifier.SingleTest import SingleTest

class SingleCompletnessTest(SingleTest):
    """Class for a Single CompletnessTest"""
    def __init__(self,id,title,description,key):
        SingleTest.__init__(self, id,title,description,key)

    def runTest(self,election_data):
        key = self.getKey()
        result = election_data.get(key,False)
        if result:
            result = True
        return result
