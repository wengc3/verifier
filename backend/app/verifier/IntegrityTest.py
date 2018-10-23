from app.verifier.SingleTest import SingleTest

class VotingCircleIntegrityTest(SingleTest):
    """docstring for ."""
    def __init__(self,id,title,description,key):
        SingleTest.__init__(self, id,title,description,key)

    def runTest(self,election_data):
        key = self.getKey()
        w_bold = election_data.get(key,False)
        res = False
        if w_bold:
            res = max(w_bold) >= 1
        return res
