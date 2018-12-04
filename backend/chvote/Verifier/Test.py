import abc
class Test(metaclass=abc.ABCMeta):
    """Declare the interface for objects in the Test structure.
    Implement default behavior for the interface common to all classes,
    as appropriate.
    ."""


    def __init__(self, id,title,description):
        self._id = id
        self._title = title
        self._description = description


    @abc.abstractmethod
    def runTest(self,election_data,report):
        pass

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description
