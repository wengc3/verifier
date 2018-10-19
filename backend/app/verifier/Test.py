import abc
class Test(metaclass=abc.ABCMeta):
    """Declare the interface for objects in the Test structure.
    Implement default behavior for the interface common to all classes,
    as appropriate.
    ."""
    current_test = None
    return_methode = print
    
    def __init__(self, id,title,description,election_data):
        self.id = id
        self.title = title
        self.description = description
        self.election_data = election_data

    @abc.abstractmethod
    def runTest(self):
        pass

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getData(self):
        return self.election_data
