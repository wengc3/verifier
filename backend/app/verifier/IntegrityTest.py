class VotingCircleIntegrityTest(SingleTest):
    """docstring for ."""
    def __init__(self,id,title,description,election_data,key_chain):
        SingleTest.__init__(self, id,title,description,election_data,key_chain)

    def runTest(self):
        key = self.getKeyChain()[0]
        w_bold = self.getData().get(key,False)
        res = False
        if w_bold:
            res = max(w_bold) >= 1
        return res
