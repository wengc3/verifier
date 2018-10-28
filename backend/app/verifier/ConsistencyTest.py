import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.verifier.SingleTest import SingleTest

class LenghtEqualityConsistenyTest(SingleTest):
    """
    docstring for LenghtEqualityTest. Check if two sequences has the same lenght
    """
    def __init__(self,id,title,description,key, test_key):
        SingleTest.__init__(self, id,title,description,key)
        self.test_key = test_key

    def runTest(self,election_data):
        """
        >>> lect.runTest({'test':[1,1,1,1],'test_val':[2,2,2,2]})
        (True, [1, 1, 1, 1], [2, 2, 2, 2])
        >>> lect.runTest({'test':[1,1,1],'test_val':[2,2,2,2]})
        (False, [1, 1, 1], [2, 2, 2, 2])
        >>> lect.runTest({'bla':[1,1,1],'test_val':[2,2,2,2]})
        (False, None)
        """
        key = self.getKey()
        try:
            sec_1 = election_data[key]
            sec_2 = election_data[self.test_key]
            return (len(sec_1)==len(sec_2),sec_1,sec_2)
        except KeyError:
            return (False,None)

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'lect': LenghtEqualityConsistenyTest("1.1","TEST","TEST","test","test_val")})
