from app.verifier.SingleTest import SingleTest

class VotingCircleIntegrityTest(SingleTest):
    """docstring for ."""
    def __init__(self,id,title,description,key):
        SingleTest.__init__(self, id,title,description,key)

    def runTest(self,election_data):
        key = self.getKey()
        try:
            w_bold = election_data[key]
            return (max(w_bold) >= 1,w_bold)
        except KeyError:
            return (False,None)

class ClassName(object):
    """docstring for ."""
    def __init__(self, arg):
        pass
