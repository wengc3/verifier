import abc
class Test(metaclass=abc.ABCMeta):
    """Declare the interface for objects in the Test structure.
    Implement default behavior for the interface common to all classes,
    as appropriate.
    ."""
    report = None #pointer to Report object

    def __init__(self, id,title,description):
        self.id = id
        self.title = title
        self.description = description

    @abc.abstractmethod
    def runTest(self,election_data):
        pass

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getReport(self):
        return Test.report
