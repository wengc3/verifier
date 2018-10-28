import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.verifier.SingleTest import SingleTest

class SingleCompletnessTest(SingleTest):
    """docstring for a Single CompletnessTest"""
    def __init__(self,id,title,description,key):
        SingleTest.__init__(self, id,title,description,key)

    def runTest(self,election_data):
        """
        >>> sct.runTest({'test':123})
        (True, 123)
        >>> sct.runTest({'bla':123})
        (False, None)
        """
        key = self.getKey()
        try:
            res = election_data[key]
            return (True,res)
        except KeyError:
            return (False,None)


if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'sct': SingleCompletnessTest("1.1","TEST","TEST","test")})
