import abc
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from chvote.verifier.Test import Test

class SingleTest(Test,metaclass=abc.ABCMeta):
    """docstring for abstract class """
    def __init__(self,id,title,description,keys):
        Test.__init__(self, id,title,description)
        self._keys = keys

    @property
    def keys(self):
        return self._keys

    @abc.abstractmethod
    def runTest(self,election_data):
        pass
