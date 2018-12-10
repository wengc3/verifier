import abc
from chvote.verifier.Test import Test

class SingleTest(Test,metaclass=abc.ABCMeta):
    """docstring for abstract class """
    def __init__(self,id,title,description,key):
        Test.__init__(self, id,title,description)
        self._key = key

    @property
    def key(self):
        return self._key

    @abc.abstractmethod
    def runTest(self,election_data):
        pass
