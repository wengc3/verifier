import abc
class Test(metaclass=abc.ABCMeta):
    """Declare the interface for objects in the Test structure.
    Implement default behavior for the interface common to all classes,
    as appropriate.
    ."""
    _observers = set()

    def __init__(self, id,title,description):
        self._id = id
        self._title = title
        self._description = description
        self._old_progress = 0

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

    @property
    def progress(self):
        return self._progress

    def _notify(self,state):
        for observer in Test._observers:
            observer.test = self
            observer.update(state)

    def attachAll(self,observers):
        Test._observers.update(observers)

    @progress.setter
    def progress(self,new_progress):
        self._progress = new_progress
        self._notify("newProgress")

    @property
    def old_progress(self):
        return self._old_progress

    @old_progress.setter
    def old_progress(self,old_prg):
        self._old_progress = old_prg
