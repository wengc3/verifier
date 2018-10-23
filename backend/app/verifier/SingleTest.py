import abc
from app.verifier.Test import Test
class SingleTest(Test,metaclass=abc.ABCMeta):
    """docstring for abstract class """
    def __init__(self,id,title,description,key):
        Test.__init__(self, id,title,description)
        self.key = key

    def getKey(self):
        return self.key

    @abc.abstractmethod
    def runTest(self,election_data):
        pass
