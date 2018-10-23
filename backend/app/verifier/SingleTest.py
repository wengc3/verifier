import abc
from app.verifier.Test import Test
class SingleTest(Test,metaclass=abc.ABCMeta):
    """docstring for abstract class """
    def __init__(self,id,title,description,election_data,key_chain):
        Test.__init__(self, id,title,description,election_data)
        self.key_chain = key_chain

    def getKeyChain(self):
        return self.key_chain

    @abc.abstractmethod
    def runTest(self):
        pass
